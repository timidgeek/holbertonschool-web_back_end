// task seven - my little job creator
import kue from 'kue';
// create kue queue
const queue = kue.createQueue();

// add jobs array
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

// write a loop that will go through the array `jobs`
jobs.forEach((jobData => {
  // create new job with current opject
  // console log job created if no error
  const newJob = queue.create('push_notification_code_2', jobData).save((error) => {
    if (!error) console.log(`Notification job created: ${newJob.id}`)
  });
  newJob.on('complete', () =>
  console.log(`Notification job ${newJob.id} completed`)
  ); // job completion log
  newJob.on('failed', (error) =>
    console.log(`Notification job ${newJob.id} failed: ${error}`)
  ); // job failure log
  newJob.on('progress', (progress) =>
    console.log(`Notification job ${newJob.id} ${progress}% complete`)
  ); // job progress percentage log
}))