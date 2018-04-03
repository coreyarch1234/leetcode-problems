// Persistent Stack
//
// Mutable stack in js
//
// class Stack {
//     // items should be array
//     constructor(items = []) {
//         this.stack = items.length == 0 ? [] : items;
//     }
//
//     pop() {
//         // remove last element
//         return this.stack.pop();
//     }
//
//
//     push(item) {
//         this.stack.push(item);
//     }
// }
//
// var stack = new Stack([5,6,7]);
// console.log(stack);
// stack.push(2);
// console.log(stack);
// stack.pop();
// console.log(stack);


// immutable stack

var createStack = function () {
  var createInternalStack = function (top, rest) {
    var isEmpty = function () {
      return top === undefined;
    };

    var peek = function () {
      return top;
    };

    var push = function (item) {
      return createInternalStack(item, this);
    }

    var pop = function () {
      return rest;
    }

    return {
      isEmpty: isEmpty,
      peek: peek,
      push: push,
      pop: pop
    }
  };

  return createInternalStack(undefined, undefined);
};
