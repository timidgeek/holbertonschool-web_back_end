export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  // sqft getter
  get sqft() {
    return this.sqft;
  }

  // warning message method
  evacuationWarningMessage() {
    if (typeof this.evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }
}
