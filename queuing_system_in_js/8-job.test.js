// test suite for 8-job's function
import { createPushNotificationsJobs } from './8-job';
import kue from 'kue';
import chai from 'chai';
const expect = chai.expect;
const queue = kue.createQueue();

// create test squite
describe('createPushNotificationsJobs', () => {
  it('should throw an error if jobs is not an array', () => {
    function arrayError() {
      createPushNotificationsJobs('Not an array', {});
    }
    expect(arrayError).to.throw('Jobs is not an array');
  });

  it('should have data of type push_notification_code_3')
    createdJobs.forEach((job, index) => {
    // Check if the job's type and data match the input
    expect(job.type).to.equal('push_notification_code_3');
    expect(job.data).to.deep.equal(jobsToCreate[index]);

});
