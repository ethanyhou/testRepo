/**
 * Job Handler Module
 * Handles sending jobs to a processing queue with deduplication support
 */

// Store for tracking processed job IDs to prevent duplicates
const processedJobs = new Set();

/**
 * Handles sending a job to the job processing queue with deduplication
 * @param {Object} job - The job object to process
 * @param {string} job.id - Unique identifier for the job
 * @param {*} job.data - Job data/payload
 * @param {Function} sendFunction - Function to actually send the job (e.g., to queue/API)
 * @returns {Object} Result object with status and message
 */
function handleSendToJob(job, sendFunction) {
  // Validate input
  if (!job || typeof job !== 'object') {
    return {
      success: false,
      status: 'error',
      message: 'Invalid job object provided',
    };
  }

  if (!job.id) {
    return {
      success: false,
      status: 'error',
      message: 'Job ID is required for deduplication',
    };
  }

  // Check if job has already been processed (deduplication)
  if (processedJobs.has(job.id)) {
    return {
      success: false,
      status: 'duplicate',
      message: `Job with ID ${job.id} has already been processed`,
      jobId: job.id,
    };
  }

  // Validate send function
  if (!sendFunction || typeof sendFunction !== 'function') {
    return {
      success: false,
      status: 'error',
      message: 'Valid send function is required',
    };
  }

  try {
    // Send the job using the provided function
    const result = sendFunction(job);
    
    // Mark job as processed for deduplication
    processedJobs.add(job.id);
    
    return {
      success: true,
      status: 'sent',
      message: `Job ${job.id} sent successfully`,
      jobId: job.id,
      result: result,
    };
  } catch (error) {
    return {
      success: false,
      status: 'error',
      message: `Failed to send job: ${error.message}`,
      jobId: job.id,
      error: error,
    };
  }
}

/**
 * Clears the deduplication cache
 * Useful for testing or when you want to reset the tracking
 */
function clearProcessedJobs() {
  processedJobs.clear();
}

/**
 * Gets the count of processed jobs
 * @returns {number} Number of jobs that have been processed
 */
function getProcessedJobCount() {
  return processedJobs.size;
}

/**
 * Checks if a job ID has been processed
 * @param {string} jobId - The job ID to check
 * @returns {boolean} True if the job has been processed
 */
function hasJobBeenProcessed(jobId) {
  return processedJobs.has(jobId);
}

module.exports = {
  handleSendToJob,
  clearProcessedJobs,
  getProcessedJobCount,
  hasJobBeenProcessed,
};
