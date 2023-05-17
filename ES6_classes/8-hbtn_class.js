export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // size getter, setter, implementation
  get size() {
    return this._size;
  }

  set size(newSize) {
    if (typeof newSize !== 'number') {
      throw new Error('Size must be a number');
    }
    return this.newSize;
  }

  // location getter, setter, implementation
  get location() {
    return this._location;
  }

  set location(newLocation) {
    if (typeof newLocation !== 'string') {
      throw new Error('Location must be a string');
    }
    return this.newLocation;
  }

  // return the size, so long as value is a number
  valueOf() {
    return this._size;
  }

  // return the location, so long as value is a string
  toString() {
    return this._location;
  }
}
