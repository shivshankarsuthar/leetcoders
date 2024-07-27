"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __param = (this && this.__param) || function (paramIndex, decorator) {
    return function (target, key) { decorator(target, key, paramIndex); }
};
// Class decorators
function sealed(constructor) {
    Object.seal(constructor);
    Object.seal(constructor.prototype);
}
var Greeter = /** @class */ (function () {
    function Greeter(message) {
        this.greeting = message;
    }
    Greeter.prototype.greet = function () {
        return "Hello, ".concat(this.greeting);
    };
    Greeter = __decorate([
        sealed
    ], Greeter);
    return Greeter;
}());
var greeter = new Greeter("hello");
console.log(greeter.greeting);
// Method decorators
function log(target, propertyName, descriptor) {
    var method = descriptor.value;
    descriptor.value = function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i] = arguments[_i];
        }
        console.log("Calling ".concat(propertyName, " with arguments: ").concat(args.join(", ")));
        return method.apply(this, args);
    };
}
var Calculator = /** @class */ (function () {
    function Calculator() {
    }
    Calculator.prototype.add = function (a, b) {
        return a + b;
    };
    Calculator.prototype.subtract = function (a, b) {
        return a - b;
    };
    __decorate([
        log
    ], Calculator.prototype, "add", null);
    return Calculator;
}());
var calc = new Calculator();
calc.add(2, 3); // Logs: Calling add with arguments: 2, 3
//Accessor decorators
function enumerable(value) {
    return function (target, propertyKey, descriptor) {
        descriptor.enumerable = value;
    };
}
var Person = /** @class */ (function () {
    function Person(name) {
        this._name = name;
    }
    Object.defineProperty(Person.prototype, "name", {
        get: function () {
            return this._name;
        },
        enumerable: false,
        configurable: true
    });
    __decorate([
        enumerable(true)
    ], Person.prototype, "name", null);
    return Person;
}());
var person = new Person("John");
for (var key in person) {
    console.log(key); // Logs: name
}
//Property decorators
function format(formatString) {
    return function (target, propertyKey) {
        var value = target[propertyKey];
        var getter = function () {
            return formatString.replace("{value}", value);
        };
        var setter = function (newValue) {
            value = newValue;
        };
        Object.defineProperty(target, propertyKey, {
            get: getter,
            set: setter,
            enumerable: true,
            configurable: true,
        });
    };
}
var Product = /** @class */ (function () {
    function Product(name) {
        this.name = name;
    }
    __decorate([
        format("Product: {value}")
    ], Product.prototype, "name", void 0);
    return Product;
}());
var product = new Product("Laptop");
console.log(product.name); // Logs: Product: Laptop
// Parameter decorators
function logParameter(target, propertyName, index) {
    var metadataKey = "__log_".concat(propertyName, "_parameters");
    if (Array.isArray(target[metadataKey])) {
        target[metadataKey].push(index);
    }
    else {
        target[metadataKey] = [index];
    }
}
var Example = /** @class */ (function () {
    function Example() {
    }
    Example.prototype.greet = function (message, message2) {
        console.log(message);
    };
    Example.prototype.greet2 = function (message2) {
        console.log(message2);
    };
    __decorate([
        __param(1, logParameter)
    ], Example.prototype, "greet", null);
    __decorate([
        __param(0, logParameter)
    ], Example.prototype, "greet2", null);
    return Example;
}());
var example = new Example();
example.greet("Hello, World!", "New hello world"); // Parameter index logged
console.log(example);
