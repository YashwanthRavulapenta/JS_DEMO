function createUniqueCounter() {
    let count = 0; // private variable

    return {
        increment: function() {
            count++;
            return count;
        },
        getValue: function() {
            return count;
        }
    };
}

// Demonstration:

const counter1 = createUniqueCounter();
console.log(counter1.getValue());   // Output: 0
console.log(counter1.increment());  // Output: 1
console.log(counter1.increment());  // Output: 2
console.log(counter1.getValue()); // Output: 2
console.log(counter1.count);  

const counter2 = createUniqueCounter();
console.log(counter2.getValue());   // Output: 0 (independent counter)
console.log(counter2.increment());  // Output: 1
console.log(counter1.getValue());   // Output: 2 (counter1 is still at 2, unaffected)
