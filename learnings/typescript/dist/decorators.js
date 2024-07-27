"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
// Method decorators
function logger(target, propertyKey, descriptor) {
    var originalMethod = descriptor.value;
    descriptor.value = function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i] = arguments[_i];
        }
        console.log("start:", propertyKey);
        var result = originalMethod.apply(this, args);
        console.log("end:", propertyKey);
        return result;
    };
}
//class decorators
function created(ctr) {
    ctr.prototype.created = new Date().toISOString();
}
var User = /** @class */ (function () {
    function User(name, age) {
        this.name = name;
        this.age = age;
    }
    User.prototype.greet = function () {
        console.log("Hello brother");
    };
    User.prototype.printAge = function () {
        console.log("My age is " + this.age);
    };
    __decorate([
        logger
    ], User.prototype, "greet", null);
    User = __decorate([
        created
    ], User);
    return User;
}());
var user = new User("SHiv", 28);
user.greet();
console.log(user.created);
//accessor decorators
var Point = /** @class */ (function () {
    function Point(x, y) {
        this._x = x;
    }
    Object.defineProperty(Point.prototype, "x", {
        get: function () {
            return this._x;
        },
        enumerable: false,
        configurable: true
    });
    __decorate([
        configurable(false)
    ], Point.prototype, "x", null);
    return Point;
}());
function configurable(value) {
    return function (target, propertyKey, descriptor) {
        descriptor.configurable = value;
    };
}
