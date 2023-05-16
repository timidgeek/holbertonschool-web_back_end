export default class HolbertonCourse {
  constructor(name, length, students) {
    // check if name is a string
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    // check if length is a number
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    // check if students is an array of strings
    if (!Array.isArray(students) || !students.every((s) => typeof s === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    // initialize / store attributes
    this._name = name;
    this._length = length;
    this._students = students;
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

  // length getter, setter, initialization
  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = newLength;
  }

  // students getter, setter, initialization
  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (!Array.isArray(newStudents) || !newStudents.every((s) => typeof s === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this.__students = newStudents;
  }
}
