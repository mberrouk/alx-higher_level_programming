#!/usr/bin/node

const { dict } = require('./101-data');

function invertDictionary (obj) {
  const invertedDict = {};
  for (const key in obj) {
    const value = obj[key];
    if (!invertedDict[value]) {
      invertedDict[value] = [key];
    } else {
      invertedDict[value].push(key);
    }
  }
  return invertedDict;
}

const newDict = invertDictionary(dict);

console.log(newDict);
