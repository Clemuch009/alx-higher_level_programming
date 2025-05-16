#!/usr/bin/node
const argv = process.argv.slice(2);


if (argv.length <= 1) {
    console.log("0");
    process.exit();
}
let num = [];
for (let i = 0; i < argv.length; i++) {
    const value = Number(argv[i]);
    if (!isNaN(value)) {
        num.push(value);
    }
}

if (num.length <= 1) {
    console.log("0");
    process.exit();
}

let biggest = -Infinity;
let second = -Infinity;

for (let i = 0; i < num.length; i++) {
    if (num[i] > biggest) {
        second = biggest;
        biggest = num[i];
    } else if (num[i] > second && num[i] < biggest) {
        second = num[i];
    }
}

if (second === -Infinity) {
    console.log("0");
} else {
    console.log(second);
}

