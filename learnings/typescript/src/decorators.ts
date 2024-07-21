class User{
    constructor(private name:string,private age:number){
    }

    greet(){
        console.log("Hello brother")
    }

    printAge(){
        console.log("My age is " +this.age)
    }
}


let user = new User("SHiv",28)
user.printAge()