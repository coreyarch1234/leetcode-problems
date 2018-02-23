const a = {name: "Joe", age: 33}
a.description = function() {
  console.log(`Hello ${this.name} you are ${this.age}`)
}


function User(name, age) {
  this.name = name
  this.age = age
  this.test = function() {

  }
}

User.prototype.description = function() {
  console.log(`Hello ${this.name} you are ${this.age}`)
}

const b = new User("Jane", 44)
const b2 = new User("Jane 2", 42)
const b3 = new User("Jane 3", 43)

console.log(a)
console.log(b)
console.log(b2)
console.log(b3)

b.description()

// ------------------------------------------

class Person {
  constructor(hairColor) {
    this.hairColor = hairColor
  }

  hair() {
    console.log()
  }
}

// ------------------------------------------

class User2 extends Person {
  constructor(name, age, hairColor) {
    super(hairColor)
    this.name = name
    this.age = age
  }

  speak() {
    console.log(`Person says hello`)
  }
}

const c = new User2("Jim", 55, "colorful")
const d = new User2("Dan", 33, "no-color")

console.log(c);
//  console.log(d);

//  function User2(name, age) {
//    this.constructor(name, age)
//  }

//  User2.prototype.constructor = function(name, age) {
//    this.name = name
//    this.age = age
//  }
//
//  new User2('test', 0)
//  
