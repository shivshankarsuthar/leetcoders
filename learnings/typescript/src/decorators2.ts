// Class decorators
function sealed(constructor: Function) {
    Object.seal(constructor);
    Object.seal(constructor.prototype);
  }
  
  
  @sealed
  class Greeter {
    greeting?: string;
    constructor(message: string) {
      this.greeting = message;
    }
  
    greet() {
      return `Hello, ${this.greeting}`;
    }
  }

  var greeter = new Greeter("hello");
  console.log(greeter.greeting);

  
// Method decorators
  function log(target: any, propertyName: string, descriptor: PropertyDescriptor): void {
    const method = descriptor.value;
    
    descriptor.value = function(...args: any[]) {
      console.log(`Calling ${propertyName} with arguments: ${args.join(", ")}`);
      return method.apply(this, args);
    };
  }
  
  class Calculator {
    @log
    add(a: number, b: number): number {
      return a + b;
    }

    subtract(a:number,b:number):number{
        return a - b;
    }
  }
  
  const calc = new Calculator();
  calc.add(2, 3);  // Logs: Calling add with arguments: 2, 3

  //Accessor decorators
  function enumerable(value: boolean) {
    return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
      descriptor.enumerable = value;
    };
  }
  
  class Person {
    private _name: string;
  
    constructor(name: string) {
      this._name = name;
    }
  
    @enumerable(true)
    get name(): string {
      return this._name;
    }
  }
  
  const person = new Person("John");
  for (const key in person) {
    console.log(key);  // Logs: name
  }
  
  //Property decorators

  function format(formatString: string) {
    return function (target: any, propertyKey: string) {
      let value = target[propertyKey];
  
      const getter = () => {
        return formatString.replace("{value}", value);
      };
  
      const setter = (newValue:any) => {
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
  
  class Product {
    @format("Product: {value}")
    name: string;
  
    constructor(name: string) {
      this.name = name;
    }
  }
  
  const product = new Product("Laptop");
  console.log(product.name);  // Logs: Product: Laptop
  

  // Parameter decorators
  function logParameter(target: any, propertyName: string, index: number) {
    const metadataKey = `__log_${propertyName}_parameters`;
  
    if (Array.isArray(target[metadataKey])) {
      target[metadataKey].push(index);
    } else {
      target[metadataKey] = [index];
    }
  }
  
  class Example {
    greet( message: string,@logParameter message2:string): void {
      console.log(message);
    }

    greet2(@logParameter message2:string){
        console.log(message2);
    }
  }
  
  const example = new Example();
  example.greet("Hello, World!","New hello world");  // Parameter index logged
  console.log(example)
  