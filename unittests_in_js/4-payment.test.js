// task four - stubs
const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./4-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('checks to see if the math used in sendPaymentRequestToApi(100, 20) is the same as Utils.calculateNumber("SUM", 100, 20)', () => {
    const calcSpy = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleSpy = sinon.spy(console, 'log');

    const result = sendPaymentRequestToApi(100, 20);

    expect(calcSpy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledWithExactly('The total is: 10')).to.be.true;
    expect(Utils.calculateNumber('SUM', 100, 20)).to.equal(10);
    expect(result).to.equal(10);

    calcSpy.restore();
    consoleSpy.restore();
  });
});