function filterObjectProperties(data, minLength) {
    const result = {};
    for (let i in data) {
        if (typeof data[i] === 'string' && data[i].length >= minLength) {
            result[i] = data[i];
        }
    }
    return result;
}

const data = { a: "short", b: "longer string", c: 123, d: "very long string indeed" };
const filtered = filterObjectProperties(data, 16);
console.log(filtered);