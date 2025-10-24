/**
 * Example usage of handleSendToJob with deduplication
 */

const {
  handleSendToJob,
  clearProcessedJobs,
  getProcessedJobCount,
  hasJobBeenProcessed,
} = require('./jobHandler');

// Mock function that simulates sending jobs to a queue/API
function mockJobQueue(job) {
  console.log(`  → Sending job ${job.id} to queue...`);
  // Simulate some processing
  return {
    queuePosition: Math.floor(Math.random() * 100),
    estimatedTime: Math.floor(Math.random() * 60),
    timestamp: new Date().toISOString(),
  };
}

console.log('\n=== Example: handleSendToJob with Deduplication ===\n');

// Clear any previous state
clearProcessedJobs();

// Example 1: Send a new job
console.log('Example 1: Sending a new job');
const result1 = handleSendToJob(
  {
    id: 'task-001',
    data: {
      type: 'data-processing',
      payload: { records: 1000 },
    },
  },
  mockJobQueue
);
console.log('Result:', {
  success: result1.success,
  status: result1.status,
  message: result1.message,
});
console.log('');

// Example 2: Try to send the same job again (should be deduplicated)
console.log('Example 2: Attempting to send duplicate job');
const result2 = handleSendToJob(
  {
    id: 'task-001',
    data: {
      type: 'data-processing',
      payload: { records: 1000 },
    },
  },
  mockJobQueue
);
console.log('Result:', {
  success: result2.success,
  status: result2.status,
  message: result2.message,
});
console.log('');

// Example 3: Send different jobs
console.log('Example 3: Sending multiple different jobs');
const jobs = [
  { id: 'task-002', data: { type: 'email', recipient: 'user@example.com' } },
  { id: 'task-003', data: { type: 'notification', message: 'Hello' } },
  { id: 'task-004', data: { type: 'backup', target: 'database' } },
];

jobs.forEach((job) => {
  const result = handleSendToJob(job, mockJobQueue);
  console.log(`  Job ${job.id}: ${result.status}`);
});
console.log('');

// Example 4: Check processed jobs
console.log('Example 4: Checking processed jobs');
console.log(`Total processed jobs: ${getProcessedJobCount()}`);
console.log(`Has task-001 been processed? ${hasJobBeenProcessed('task-001')}`);
console.log(`Has task-005 been processed? ${hasJobBeenProcessed('task-005')}`);
console.log('');

// Example 5: Handling errors
console.log('Example 5: Handling error scenarios');

// Missing job ID
const result5a = handleSendToJob({ data: 'test' }, mockJobQueue);
console.log(`Missing ID: ${result5a.message}`);

// Invalid job object
const result5b = handleSendToJob(null, mockJobQueue);
console.log(`Null job: ${result5b.message}`);

// Send function that throws error
const errorFunc = () => {
  throw new Error('Connection timeout');
};
const result5c = handleSendToJob({ id: 'task-error', data: 'test' }, errorFunc);
console.log(`Send error: ${result5c.message}`);
console.log('');

// Example 6: Batch processing with deduplication
console.log('Example 6: Batch processing with duplicate detection');
const batchJobs = [
  { id: 'batch-001', data: 'item1' },
  { id: 'batch-002', data: 'item2' },
  { id: 'batch-001', data: 'item1-duplicate' }, // Duplicate
  { id: 'batch-003', data: 'item3' },
  { id: 'batch-002', data: 'item2-duplicate' }, // Duplicate
  { id: 'batch-004', data: 'item4' },
];

let sent = 0;
let duplicates = 0;
let errors = 0;

batchJobs.forEach((job) => {
  const result = handleSendToJob(job, mockJobQueue);
  if (result.status === 'sent') sent++;
  else if (result.status === 'duplicate') duplicates++;
  else if (result.status === 'error') errors++;
});

console.log(`Batch Results:
  - Successfully sent: ${sent}
  - Duplicates detected: ${duplicates}
  - Errors: ${errors}
  - Total attempted: ${batchJobs.length}
`);

console.log('=== Examples Complete ===\n');
