// task seven - my little job processor
import kue from 'kue';
import redis from 'redis';
// create kue queue
const queue = kue.createQueue();

// array of numbers blacklisted by job processor
blacklisted = ['4153518780', '4153518781'];

// send notification, track job progress,
// fail to process blacklisted numbers
function sendNotification(phoneNumber, message, job, done){
  job.progress(0, 100);
  // check for blacklisted nums
  if (blacklisted.includes(phoneNumber)) {
    const failure = `Phone number ${phoneNumber} is blacklisted`;
    job.failed().error(new Error(failure));
    return done(new Error(failure));
  }

  // track progress to 50%
  job.progress(50, 100);
  // log notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// process multiple jobs from queue at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});