# testRepo

Job Handler with Deduplication Support

## Overview

This repository provides a `handleSendToJob` function that handles sending jobs to a processing queue with built-in deduplication support. It prevents duplicate jobs from being processed by tracking job IDs.

## Features

- **Deduplication**: Automatically prevents duplicate jobs from being sent based on job ID
- **Error Handling**: Comprehensive error handling for invalid inputs and send failures
- **Tracking**: Utilities to check processed job count and status
- **Simple API**: Easy-to-use function interface with clear return values

## Installation

```bash
npm install
```

## Usage

### Basic Usage

```javascript
const { handleSendToJob } = require('./jobHandler');

// Define a function that sends jobs to your queue/API
function sendToQueue(job) {
  // Your implementation here (e.g., HTTP request, queue push, etc.)
  console.log('Sending job:', job.id);
  return { success: true };
}

// Send a job
const result = handleSendToJob(
  { id: 'job123', data: { task: 'process-data' } },
  sendToQueue
);

console.log(result);
// Output: { success: true, status: 'sent', message: 'Job job123 sent successfully', jobId: 'job123', result: {...} }
```

### Deduplication in Action

```javascript
const { handleSendToJob } = require('./jobHandler');

function sendToQueue(job) {
  console.log('Processing job:', job.id);
  return { processed: true };
}

// First attempt - succeeds
const result1 = handleSendToJob({ id: 'job123', data: 'test' }, sendToQueue);
console.log(result1.success); // true
console.log(result1.status); // 'sent'

// Second attempt with same ID - fails (duplicate)
const result2 = handleSendToJob({ id: 'job123', data: 'test' }, sendToQueue);
console.log(result2.success); // false
console.log(result2.status); // 'duplicate'
console.log(result2.message); // 'Job with ID job123 has already been processed'
```

### Utility Functions

```javascript
const {
  handleSendToJob,
  clearProcessedJobs,
  getProcessedJobCount,
  hasJobBeenProcessed,
} = require('./jobHandler');

// Check if a job has been processed
if (hasJobBeenProcessed('job123')) {
  console.log('Job already processed');
}

// Get count of processed jobs
console.log('Processed jobs:', getProcessedJobCount());

// Clear the deduplication cache (useful for testing or reset)
clearProcessedJobs();
```

## API Reference

### `handleSendToJob(job, sendFunction)`

Sends a job to the processing queue with deduplication.

**Parameters:**
- `job` (Object): The job object to process
  - `id` (string, required): Unique identifier for the job
  - `data` (any): Job data/payload
- `sendFunction` (Function): Function to send the job (e.g., to queue/API)

**Returns:**
- Object with the following properties:
  - `success` (boolean): Whether the operation succeeded
  - `status` (string): Status code ('sent', 'duplicate', or 'error')
  - `message` (string): Human-readable message
  - `jobId` (string): The job ID
  - `result` (any): Result from the send function (if successful)
  - `error` (Error): Error object (if failed)

### `clearProcessedJobs()`

Clears the deduplication cache. Useful for testing or when you want to reset tracking.

### `getProcessedJobCount()`

Returns the number of jobs that have been processed.

**Returns:** `number`

### `hasJobBeenProcessed(jobId)`

Checks if a job ID has been processed.

**Parameters:**
- `jobId` (string): The job ID to check

**Returns:** `boolean`

## Testing

Run the test suite:

```bash
npm test
```

## Implementation Details

The deduplication mechanism uses a `Set` to track processed job IDs in memory. This provides:
- O(1) lookup time for checking duplicates
- Efficient memory usage
- Simple and reliable deduplication

**Note:** The deduplication cache is stored in memory and will be cleared when the process restarts. For persistent deduplication across restarts, consider using a database or external cache (Redis, etc.).

## Error Handling

The function handles various error scenarios:
- Invalid job object (null, undefined, or not an object)
- Missing job ID
- Missing or invalid send function
- Exceptions thrown by the send function

All errors return a structured response with `success: false` and descriptive error messages.

## License

ISC