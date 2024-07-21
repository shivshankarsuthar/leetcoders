"use strict";
class User {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    greet() {
        console.log("Hello brother");
    }
    printAge() {
        console.log("My age is " + this.age);
    }
}
let user = new User("SHiv", 28);
user.printAge();
