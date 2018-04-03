// This is a higher-order function (takes a function as a parameter)
// that will return a function which, when invoked, will
// wait a specified amount of time and only call the
// function if it is not invoked again in that time.

/**
 * @param {function} fn
 * @param {number} wait
 *
 * @return {function}
 */
function debounce(fn, wait) {
  var timeout;

  return () => {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      fn();
    }, wait);
  };
}



///////////
// TESTS //
// ///////////
// var assert = require('assert');
//
// var string = "";
//
// function addToString(value) {
//   string += value;
// }
//
// var debouncedAddToString = debounce(addToString, 100)
//
// debouncedAddToString("a")
// debouncedAddToString("b")
// debouncedAddToString("c")
// setTimeout(() => debouncedAddToString("d"), 200)
//
// setTimeout(() => {
//   assert.equal(string, "c")
//   console.log("YAY!")
// }, 200)
// setTimeout(() => {
//   assert.equal(string, "cd")
//   console.log("YAY!")
// }, 400)
