export default function cleanSet(set, startString) {
  // returns empty string when non-String type is passed in
  if (typeof startString !== 'string' || startString.lenght < 1 || !startString) {
    return '';
  }

  const filteredValues = Array.from(set)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length));

  return filteredValues.join('-');
}
