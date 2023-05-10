export default function concatArrays(array1, array2, string) {
  const cat = [...array1, ...array2, ...string];
  return cat;
}
