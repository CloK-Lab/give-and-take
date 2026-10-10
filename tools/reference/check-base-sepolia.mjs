// SPDX-License-Identifier: Apache-2.0
// External reference observation, independent of the project's Lean runtime.
import { parseArgs } from 'node:util';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

// Official network and token registries, checked on 2026-10-09:
// https://docs.base.org/get-started/connect-to-base
// https://developers.circle.com/stablecoins/usdc-contract-addresses
export const baseSepolia = Object.freeze({
  chainId: 84532n,
  network: 'eip155:84532',
  rpcUrl: 'https://sepolia.base.org',
  usdc: '0x036CbD53842c5426634e7929541eC2318f3dCF7e',
  decimals: 6,
});

function requireValue(condition, message) {
  if (!condition) throw new Error(message);
}

function quantity(value, label) {
  requireValue(typeof value === 'string' && /^0x(?:0|[1-9a-fA-F][0-9a-fA-F]*)$/.test(value),
    `Invalid ${label} from RPC.`);
  return BigInt(value);
}

function uint256(value, label) {
  requireValue(typeof value === 'string' && /^0x[0-9a-fA-F]{64}$/.test(value),
    `Invalid ABI result for ${label}.`);
  return BigInt(value);
}

function formatUsdc(units) {
  const digits = units.toString().padStart(baseSepolia.decimals + 1, '0');
  return `${digits.slice(0, -baseSepolia.decimals)}.${digits.slice(-baseSepolia.decimals)}`;
}

/** Read an RPC-reported snapshot at one block number; no finality assertion. */
export async function inspectBaseSepolia({
  rpcUrl = baseSepolia.rpcUrl, address, fetchImpl = fetch,
} = {}) {
  let endpoint;
  try { endpoint = new URL(rpcUrl); } catch { throw new Error('Invalid RPC URL.'); }
  requireValue(['https:', 'http:'].includes(endpoint.protocol), 'RPC URL must use HTTP or HTTPS.');
  requireValue(address === undefined || /^0x[0-9a-fA-F]{40}$/.test(address),
    '--address must be a public EVM address (0x followed by 40 hex characters).');

  let nextId = 1;
  async function rpc(method, params) {
    const id = nextId++;
    let response;
    try {
      response = await fetchImpl(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ jsonrpc: '2.0', id, method, params }),
        signal: AbortSignal.timeout(15_000),
        redirect: 'error',
      });
    } catch {
      throw new Error(`Could not reach RPC for ${method}; check connectivity and GIVE_AND_TAKE_RPC_URL.`);
    }
    requireValue(response.ok, `RPC HTTP failure for ${method} (status ${response.status}).`);
    let message;
    try { message = await response.json(); } catch { throw new Error(`Invalid JSON for ${method}.`); }
    requireValue(message?.jsonrpc === '2.0' && message.id === id,
      `Invalid JSON-RPC envelope for ${method}.`);
    requireValue(!message.error && Object.hasOwn(message, 'result'), `RPC rejected ${method}.`);
    return message.result;
  }

  const chainId = quantity(await rpc('eth_chainId', []), 'chain ID');
  requireValue(chainId === baseSepolia.chainId,
    `Wrong network: expected Base Sepolia (84532), received ${chainId}.`);
  const block = await rpc('eth_getBlockByNumber', ['latest', false]);
  const blockNumber = quantity(block?.number, 'block number');
  requireValue(typeof block?.hash === 'string' && /^0x[0-9a-fA-F]{64}$/.test(block.hash),
    'Invalid block hash from RPC.');

  const code = await rpc('eth_getCode', [baseSepolia.usdc, block.number]);
  requireValue(typeof code === 'string' && /^0x(?:[0-9a-fA-F]{2})+$/.test(code),
    'No valid contract code at the configured USDC address.');
  // ERC-20 decimals() and balanceOf(address), with fixed read-only ABI selectors.
  const decimals = uint256(await rpc('eth_call', [
    { to: baseSepolia.usdc, data: '0x313ce567' }, block.number,
  ]), 'decimals');
  requireValue(decimals === BigInt(baseSepolia.decimals), 'Unexpected USDC decimal precision.');

  const report = {
    purpose: 'external-reference',
    mode: 'read-only',
    network: baseSepolia.network,
    chainId: chainId.toString(),
    token: { address: baseSepolia.usdc, decimals: baseSepolia.decimals, codeBytes: (code.length - 2) / 2 },
    block: { number: blockNumber.toString(), hash: block.hash, finality: 'not checked' },
    testTokensHaveFinancialValue: false,
  };
  if (address !== undefined) {
    const units = uint256(await rpc('eth_call', [
      { to: baseSepolia.usdc, data: `0x70a08231${address.slice(2).toLowerCase().padStart(64, '0')}` },
      block.number,
    ]), 'balanceOf');
    report.account = { address, usdcBaseUnits: units.toString(), testUsdc: formatUsdc(units) };
  }

  // Detect a reorganization during the reads; a later reorganization is still possible.
  const checkedBlock = await rpc('eth_getBlockByNumber', [block.number, false]);
  requireValue(checkedBlock?.hash === block.hash,
    'Block changed during inspection; rerun to obtain a consistent snapshot.');
  return report;
}

async function main() {
  const { values } = parseArgs({ options: {
    address: { type: 'string' }, help: { type: 'boolean', short: 'h' },
  } });
  if (values.help) {
    console.log('Usage: npm run check:reference-chain -- [--address 0xPUBLIC_ADDRESS]\n'
      + 'Optional external reference probe; independent of the project runtime.\n'
      + 'Reads Base Sepolia chain identity, USDC code and decimals, and optionally a balance.\n'
      + 'Set GIVE_AND_TAKE_RPC_URL to use another RPC endpoint for the same network.\n'
      + 'No private key, signature, token approval, or transaction is used.');
    return;
  }
  const report = await inspectBaseSepolia({
    rpcUrl: process.env.GIVE_AND_TAKE_RPC_URL || baseSepolia.rpcUrl,
    address: values.address,
  });
  console.log(JSON.stringify(report, null, 2));
}

if (process.argv[1] && pathToFileURL(resolve(process.argv[1])).href === import.meta.url) {
  main().catch(error => {
    console.error(`Chain check failed: ${error.message}`);
    process.exitCode = 1;
  });
}
