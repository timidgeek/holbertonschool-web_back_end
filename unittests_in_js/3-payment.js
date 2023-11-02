// task three - totally spies
// import calc module
const Utils = require('./utils');

const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
  const result = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${result}`);
  return result;
};

module.exports = sendPaymentRequestToApi;