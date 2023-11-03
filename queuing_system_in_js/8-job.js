// task ten - my little menty b
// job creation function
import kue from 'kue';
const queue = kue.createQueue();

module.exports = function createPushNotificationsJobs(jobs, queue) {
  // if jobs is not an array, handle existence type error
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  // for each job in jobs, create a job in the queue 
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData);

    // log job id to console when job is created
    job.on('enqueue', function (jobId) {
      console.log(`Notification job created: ${jobId}`);
    });

    // log to console when job is complete
    job.on('complete', function () {
      console.log(`Notification job ${job.id} completed`);
    });

    // log to console when job fails
    job.on('failed', function (error) {
      console.log(`Notification job ${job.id} failed: ${error}`);
    });

    // log job progress
    job.on('progress', function (percent) {
      console.log(`Notification job ${job.id} ${percent}% complete`);
    });

    job.save();
  });
}
