// task three - totally spies with sinon and chai
const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('checks to see if the math used in sendPaymentRequestToApi(100, 20) is the same as Utils.calculateNumber("SUM", 100, 20)', () => {
    const calcSpy = sinon.spy(Utils, 'calculateNumber');
    const consoleSpy = sinon.spy(console, 'log');

    const result = sendPaymentRequestToApi(100, 20);

    expect(calcSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledWithExactly('The total is: 120')).to.be.true;
    expect(Utils.calculateNumber('SUM', 100, 20)).to.equal(result);

    calcSpy.restore();
    consoleSpy.restore();
  });
});