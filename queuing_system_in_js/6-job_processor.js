// task seven - my little kue
// job processor
import kue from 'kue';
const queue = kue.createQueue();

function sendNotification(phoneNumber, message){
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
};

queue.process('push_notification_code', (job, done) => {
  // extract data from the job
  const { phoneNumber, message } = job.data;
  // call notification function
  sendNotification(phoneNumber, message);

  done();
});
