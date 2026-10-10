// SPDX-License-Identifier: Apache-2.0
// Offline checks for the optional external reference probe.
import test from 'node:test';
import assert from 'node:assert/strict';
import { inspectBaseSepolia } from './check-base-sepolia.mjs';

const hash = `0x${'ab'.repeat(32)}`;
const word = value => `0x${BigInt(value).toString(16).padStart(64, '0')}`;

function endpoint(overrides = {}) {
  const requests = [];
  const fetchImpl = async (_url, options) => {
    const request = JSON.parse(options.body);
    requests.push(request);
    let result;
    switch (request.method) {
      case 'eth_chainId': result = '0x14a34'; break;
      case 'eth_getBlockByNumber': result = { number: '0x10', hash }; break;
      case 'eth_getCode': result = '0x6000'; break;
      case 'eth_call':
        result = request.params[0].data === '0x313ce567' ? word(6) : word(9007199254740993n);
        break;
      default: throw new Error(`Unexpected RPC method ${request.method}`);
    }
    if (Object.hasOwn(overrides, request.method)) result = overrides[request.method](request, requests);
    return { ok: true, json: async () => ({ jsonrpc: '2.0', id: request.id, result }) };
  };
  return { fetchImpl, requests };
}

test('preserves large integer balances and reads all token state at the observed block', async () => {
  const mock = endpoint();
  const address = `0x${'12'.repeat(20)}`;
  const result = await inspectBaseSepolia({ ...mock, address });
  assert.equal(result.account.usdcBaseUnits, '9007199254740993');
  assert.equal(result.account.testUsdc, '9007199254.740993');
  assert.equal(result.block.finality, 'not checked');
  for (const request of mock.requests.filter(r => ['eth_call', 'eth_getCode'].includes(r.method))) {
    assert.equal(request.params[1], '0x10');
  }
  assert.equal(mock.requests.filter(r => r.method === 'eth_call')[1].params[0].data,
    `0x70a08231${address.slice(2).padStart(64, '0')}`);
});

test('rejects the wrong chain before querying the token', async () => {
  const mock = endpoint({ eth_chainId: () => '0x2105' });
  await assert.rejects(inspectBaseSepolia(mock), /Wrong network/);
  assert.equal(mock.requests.length, 1);
});

test('rejects missing code, malformed ABI data, and unexpected decimals', async () => {
  await assert.rejects(inspectBaseSepolia(endpoint({ eth_getCode: () => '0x' })), /contract code/);
  await assert.rejects(inspectBaseSepolia(endpoint({ eth_call: () => '0x6' })), /ABI result/);
  await assert.rejects(inspectBaseSepolia(endpoint({ eth_call: () => word(18) })), /precision/);
});

test('rejects invalid public addresses without any network request', async () => {
  const mock = endpoint();
  await assert.rejects(inspectBaseSepolia({ ...mock, address: `0x${'ab'.repeat(32)}` }), /public EVM address/);
  assert.equal(mock.requests.length, 0);
});

test('detects a block change during inspection', async () => {
  const mock = endpoint({ eth_getBlockByNumber: request => ({
    number: '0x10', hash: request.params[0] === 'latest' ? hash : `0x${'cd'.repeat(32)}`,
  }) });
  await assert.rejects(inspectBaseSepolia(mock), /Block changed/);
});

test('reports provider failure without returning a success report', async () => {
  await assert.rejects(inspectBaseSepolia({ fetchImpl: async () => ({ ok: false, status: 429 }) }), /status 429/);
  await assert.rejects(inspectBaseSepolia({ fetchImpl: async () => ({
    ok: true, json: async () => ({ jsonrpc: '2.0', id: 1, error: { code: -32000 } }),
  }) }), /RPC rejected/);
});
