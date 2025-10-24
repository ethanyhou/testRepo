/**
 * Visual demonstration of deduplication in action
 */

const {
  handleSendToJob,
  clearProcessedJobs,
  getProcessedJobCount,
} = require('./jobHandler');

// Mock queue sender
function sendToQueue(job) {
  return { queued: true, timestamp: Date.now() };
}

console.log('\n╔════════════════════════════════════════════════════════════╗');
console.log('║   handleSendToJob - Deduplication Demonstration           ║');
console.log('╚════════════════════════════════════════════════════════════╝\n');

clearProcessedJobs();

// Simulate receiving jobs (some duplicates)
const incomingJobs = [
  { id: 'order-101', data: { amount: 150.00 } },
  { id: 'order-102', data: { amount: 200.00 } },
  { id: 'order-101', data: { amount: 150.00 } }, // DUPLICATE
  { id: 'order-103', data: { amount: 75.50 } },
  { id: 'order-102', data: { amount: 200.00 } }, // DUPLICATE
  { id: 'order-104', data: { amount: 300.00 } },
  { id: 'order-101', data: { amount: 150.00 } }, // DUPLICATE
  { id: 'order-105', data: { amount: 125.00 } },
];

console.log('Processing incoming jobs...\n');

const stats = {
  sent: 0,
  duplicates: 0,
  errors: 0,
};

incomingJobs.forEach((job, index) => {
  const result = handleSendToJob(job, sendToQueue);
  
  const icon = result.success ? '✓' : '✗';
  const statusColor = result.status === 'sent' ? '🟢' : 
                      result.status === 'duplicate' ? '🟡' : '🔴';
  
  console.log(`${index + 1}. ${statusColor} Job ${job.id}: ${icon} ${result.status.toUpperCase()}`);
  
  if (result.status === 'sent') stats.sent++;
  else if (result.status === 'duplicate') stats.duplicates++;
  else stats.errors++;
});

console.log('\n' + '─'.repeat(60));
console.log('\n📊 Summary:');
console.log(`   Total jobs attempted:  ${incomingJobs.length}`);
console.log(`   Successfully sent:     ${stats.sent}`);
console.log(`   Duplicates blocked:    ${stats.duplicates}`);
console.log(`   Errors:                ${stats.errors}`);
console.log(`   Unique jobs tracked:   ${getProcessedJobCount()}`);

console.log('\n💡 Deduplication prevented ' + stats.duplicates + ' duplicate job(s) from being processed!');
console.log('\n' + '═'.repeat(60) + '\n');
