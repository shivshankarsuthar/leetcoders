// Method decorators
function logger(target: any, propertyKey: string, descriptor: PropertyDescriptor): void {
    const originalMethod = descriptor.value;

    descriptor.value = function(...args: any[]) {
        console.log("start:", propertyKey);
        const result = originalMethod.apply(this, args);
        console.log("end:", propertyKey);
        return result;
    };
}
//class decorators
function created(ctr:Function){
    ctr.prototype.created = new Date().toISOString();
}
@created
class User{
    [x:string]:any;
    constructor(private name:string,private age:number){
    }

   @logger
    greet(){
        console.log("Hello brother");
    }

    printAge(){
        console.log("My age is " +this.age)
    }
}


let user = new User("SHiv",28)
user.greet()
console.log(user.created);


//accessor decorators
class Point {
    private _x: number;
    constructor(x: number, y: number) {
      this._x = x;
    }
   
    @configurable(false)
    get x() {
      return this._x;
    } 
  }
  
  
  function configurable(value: boolean) {
    return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
      descriptor.configurable = value;
    };
  }