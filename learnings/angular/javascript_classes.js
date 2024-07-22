class Rectangle{
    #primap=23;
    constructor(height,width){
        this.height = height;
        this.width = width;
    }

    getArea(){
        return this.height * this.width;
    }

    get getHeight(){
        return this.height;
    }

    get Primap(){
        return this.#primap;
    }

    static NumberOfBhuja(){
        return 4;
    }
}

person = {
    name:"Shiv",
    age:27,
    get fullName(){
        return this.name + ' Shankar Suthar';
    },
    set fullName(x){
        this.name = this.name + x;
    }
}

class Jyamiti extends Rectangle{
    constructor(height,width){
        super(height,width);
    }
    get sum(){
        return this.height + this.width;
    }
}

rectangle = new Rectangle(100,200);
console.log(rectangle.height);
console.log(rectangle.getArea())
console.log(rectangle.getHeight);
console.log(person.fullName)
person.fullName = ' Shankar Suthar';
console.log(person.name)
console.log(rectangle.Primap);
console.log(Rectangle.NumberOfBhuja())
console.log(new Jyamiti(100,200).sum)