 const fs = require('fs');

 const lines = fs.readFileSync('/Users/sebastianpelli/Desktop/Advent/day2:2020:input', {encoding: 'utf-8'}).split('\n').filter(x => x);


 let acceptedPasswords = 0;


lines.forEach(line => {
    const {groups} = /^(?<from>\d+)-(?<to>\d+) (?<char>.): (?<password>.*)$/.exec(line);

    const total = {};

    [...groups.password].forEach(char => {
        if(!total[char]) {
            total[char] = 0;
        }
        total[char]++;
    });

    if(total[groups.char] >= groups.from && total[groups.char] <= groups.to) {
        acceptedPasswords++;
    }
})

console.log(acceptedPasswords);

acceptedPasswords = 0;

lines.forEach(line => {
    const {groups} = /^(?<from>\d+)-(?<to>\d+) (?<char>.): (?<password>.*)$/.exec(line);

    if(groups.password[groups.from-1] == groups.char ^ groups.password[groups.to-1] == groups.char) {
        acceptedPasswords++;
    }
})

console.log(acceptedPasswords);