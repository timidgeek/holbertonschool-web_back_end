// task one - calculator function
module.exports = function calculateNumber(type, a, b) {
  // check if args are not a number
  // else - throw errors
  if (isNaN(a) || isNaN(b)) {
    throw TypeError('Type must be a number');
  }
  // return number result if applicable
  if (type === 'SUM') return Math.round(a) + Math.round(b);
  if (type === 'SUBTRACT') return Math.round(a) - Math.round(b);
  if (type === 'DIVIDE') {
    if (Math.round(a) === 0 || Math.round(b) === 0) {
      return 'Error';
    }
    return Math.round(a) / Math.round(b);
  }
}
