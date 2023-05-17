export default class Building {
  constructor(sqft) {
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

  // warning message method
  evacuationWarningMessage() {
    if (typeof this.evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }
}
