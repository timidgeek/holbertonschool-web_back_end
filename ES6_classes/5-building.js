export default class Building {
  constructor(sqft) {
    // warning message method
    if (this.constructor !== Building
      && typeof this.evacuationWarningMessage !== 'function') {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  // sqft getter, setter, implementation
  get sqft() {
    return this.sqft;
  }

  set sqft(newSqft) {
    if (typeof newSqft !== 'number') {
      throw new TypeError('Sqft must be a number');
    }
    this._sqft = newSqft;
  }
}
