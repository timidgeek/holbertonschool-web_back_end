export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  // displayFullCurrency method implementation
  displayFullCurrency() {
    return (`${this._name} (${this._code})`);
  }

  // code getter, setter, initialization
  get code() {
    return this._code;
  }

  set code(newCode) {
    if (typeof newCode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = newCode;
  }

  // name getter, setter, initialization
  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName;
  }
}
