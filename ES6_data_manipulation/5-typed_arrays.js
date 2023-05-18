export default function createInt8TypedArray(length, position, value) {
  if (position >= length) {
    throw new Error('Position outside range');
  }

  const buffer = new ArrayBuffer(length);
  const array = new DataView(buffer);
  array.setInt8(position, value);

  return array;
}
