export default class Car {
  constructor(brand, motor, car) {
    this._brand = brand;
    this._motor = motor;
    this._car = car;
  }

  cloneCar() {
    return new this.constructor();
  }
}
