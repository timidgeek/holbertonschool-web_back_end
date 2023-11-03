// task six - my little kue
// job creator
import kue from 'kue';
const queue = kue.createQueue();

// object containing job data / keys
const jobData = {
  phoneNumber: '6789998212',
  message: 'Job related message data'
};

// create queue named push_notification_code
const jobQueue = queue.create('push_notification_code', jobData);

// log when job is created without error
jobQueue.on('enqueue', () => {
  console.log(`Notification job created: ${jobQueue.id}`)
});

// log when job is completed
jobQueue.on('complete', () => {
  console.log('Notification job completed')
});

// log when job is failed
jobQueue.on('failed', () => {
  console.log('Notification job failed')
});
