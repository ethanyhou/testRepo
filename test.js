/**
 * Test suite for handleSendToJob function
 */

const {
  handleSendToJob,
  clearProcessedJobs,
  getProcessedJobCount,
  hasJobBeenProcessed,
} = require('./jobHandler');

// Simple test runner
let testsPassed = 0;
let testsFailed = 0;

function assert(condition, message) {
  if (condition) {
    console.log(`✓ ${message}`);
    testsPassed++;
  } else {
    console.error(`✗ ${message}`);
    testsFailed++;
  }
}

function assertEqual(actual, expected, message) {
  if (actual === expected) {
    console.log(`✓ ${message}`);
    testsPassed++;
  } else {
    console.error(`✗ ${message}`);
    console.error(`  Expected: ${expected}`);
    console.error(`  Actual: ${actual}`);
    testsFailed++;
  }
}

// Mock send function
const mockSendFunction = (job) => {
  return { sent: true, jobId: job.id };
};

console.log('\n=== Testing handleSendToJob with Deduplication ===\n');

// Test 1: Valid job should be sent successfully
console.log('Test 1: Valid job should be sent successfully');
clearProcessedJobs();
const result1 = handleSendToJob({ id: 'job1', data: 'test' }, mockSendFunction);
assert(result1.success === true, 'Job should be sent successfully');
assert(result1.status === 'sent', 'Status should be "sent"');
assert(result1.jobId === 'job1', 'Job ID should be "job1"');

// Test 2: Duplicate job should be rejected
console.log('\nTest 2: Duplicate job should be rejected');
const result2 = handleSendToJob({ id: 'job1', data: 'test' }, mockSendFunction);
assert(result2.success === false, 'Duplicate job should fail');
assert(result2.status === 'duplicate', 'Status should be "duplicate"');
assert(result2.message.includes('already been processed'), 'Message should indicate duplicate');

// Test 3: Different job should be sent successfully
console.log('\nTest 3: Different job should be sent successfully');
const result3 = handleSendToJob({ id: 'job2', data: 'test2' }, mockSendFunction);
assert(result3.success === true, 'Different job should be sent successfully');
assert(result3.status === 'sent', 'Status should be "sent"');

// Test 4: Invalid job (missing ID) should be rejected
console.log('\nTest 4: Job without ID should be rejected');
const result4 = handleSendToJob({ data: 'test' }, mockSendFunction);
assert(result4.success === false, 'Job without ID should fail');
assert(result4.message.includes('Job ID is required'), 'Message should indicate missing ID');

// Test 5: Invalid job (null) should be rejected
console.log('\nTest 5: Null job should be rejected');
const result5 = handleSendToJob(null, mockSendFunction);
assert(result5.success === false, 'Null job should fail');
assert(result5.message.includes('Invalid job object'), 'Message should indicate invalid job');

// Test 6: Missing send function should be rejected
console.log('\nTest 6: Missing send function should be rejected');
const result6 = handleSendToJob({ id: 'job3', data: 'test' }, null);
assert(result6.success === false, 'Missing send function should fail');
assert(result6.message.includes('send function is required'), 'Message should indicate missing send function');

// Test 7: Error in send function should be caught
console.log('\nTest 7: Error in send function should be caught');
clearProcessedJobs();
const errorSendFunction = () => {
  throw new Error('Send failed');
};
const result7 = handleSendToJob({ id: 'job4', data: 'test' }, errorSendFunction);
assert(result7.success === false, 'Job with error should fail');
assert(result7.status === 'error', 'Status should be "error"');
assert(result7.message.includes('Failed to send job'), 'Message should indicate send failure');

// Test 8: clearProcessedJobs should reset deduplication
console.log('\nTest 8: clearProcessedJobs should reset deduplication');
clearProcessedJobs();
const result8a = handleSendToJob({ id: 'job5', data: 'test' }, mockSendFunction);
assert(result8a.success === true, 'First send should succeed');
clearProcessedJobs();
const result8b = handleSendToJob({ id: 'job5', data: 'test' }, mockSendFunction);
assert(result8b.success === true, 'After clear, same job should succeed again');

// Test 9: getProcessedJobCount should return correct count
console.log('\nTest 9: getProcessedJobCount should return correct count');
clearProcessedJobs();
assertEqual(getProcessedJobCount(), 0, 'Initial count should be 0');
handleSendToJob({ id: 'job6', data: 'test' }, mockSendFunction);
assertEqual(getProcessedJobCount(), 1, 'Count should be 1 after one job');
handleSendToJob({ id: 'job7', data: 'test' }, mockSendFunction);
assertEqual(getProcessedJobCount(), 2, 'Count should be 2 after two jobs');
handleSendToJob({ id: 'job6', data: 'test' }, mockSendFunction); // Duplicate
assertEqual(getProcessedJobCount(), 2, 'Count should stay 2 after duplicate');

// Test 10: hasJobBeenProcessed should work correctly
console.log('\nTest 10: hasJobBeenProcessed should work correctly');
clearProcessedJobs();
assert(hasJobBeenProcessed('job8') === false, 'Job8 should not be processed initially');
handleSendToJob({ id: 'job8', data: 'test' }, mockSendFunction);
assert(hasJobBeenProcessed('job8') === true, 'Job8 should be marked as processed');
assert(hasJobBeenProcessed('job9') === false, 'Job9 should not be processed');

// Test 11: Multiple jobs in sequence
console.log('\nTest 11: Multiple jobs in sequence');
clearProcessedJobs();
const jobs = [
  { id: 'seq1', data: 'data1' },
  { id: 'seq2', data: 'data2' },
  { id: 'seq3', data: 'data3' },
  { id: 'seq1', data: 'data1' }, // Duplicate
  { id: 'seq4', data: 'data4' },
];

let successCount = 0;
let duplicateCount = 0;

jobs.forEach((job) => {
  const result = handleSendToJob(job, mockSendFunction);
  if (result.success) successCount++;
  if (result.status === 'duplicate') duplicateCount++;
});

assertEqual(successCount, 4, 'Should successfully send 4 unique jobs');
assertEqual(duplicateCount, 1, 'Should detect 1 duplicate');
assertEqual(getProcessedJobCount(), 4, 'Should track 4 unique jobs');

// Summary
console.log('\n=== Test Summary ===');
console.log(`Tests Passed: ${testsPassed}`);
console.log(`Tests Failed: ${testsFailed}`);

if (testsFailed === 0) {
  console.log('\n✓ All tests passed!');
  process.exit(0);
} else {
  console.log(`\n✗ ${testsFailed} test(s) failed`);
  process.exit(1);
}
