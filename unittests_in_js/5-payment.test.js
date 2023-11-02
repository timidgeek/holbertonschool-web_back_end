// task five - hooks tests
const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  let consoleSpy;
  beforeEach(() => {
    consoleSpy = sinon.spy(console, 'log');
  });
  afterEach(() => {
    consoleSpy.restore();
  });
  // verify console is only called once, logs string total 120
  it('checks if the console.log is called with the right arg', () => {
    const result = sendPaymentRequestToApi(100, 20);
    expect(consoleSpy.calledOnceWithExactly('The total is: 120')).to.be.true;
    expect(result).to.equal(120);
  });
  // verify console is only called once, logs string total 20
  it('checks if the console.log is called with the right arg', () => {
    const result = sendPaymentRequestToApi(10, 10);
    expect(consoleSpy.calledOnceWithExactly('The total is: 20')).to.be.true;
    expect(result).to.equal(20);
  });
});
