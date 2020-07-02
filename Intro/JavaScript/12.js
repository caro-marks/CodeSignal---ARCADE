// Smooth Sailing

/* 

ALL LONGEST STRINGS
Given an array of strings, return another array containing all of its longest strings.

*/

function allLongestStrings1(inputArray) {
    return inputArray.filter(x => x.length === Math.max(...inputArray.map(x => x.length)))
}

function allLongestStrings2(inputArray) {
    let maxSize = Math.max(...inputArray.map(x => x.length));
    return inputArray.filter(x => x.length === maxSize);
}

/*

COMMON CHARACTER COUNTS
Given two string, find the number of common characters between them.

*/

function commonCharacterCount1(s1, s2) {
    for (var i = 0; i < s1.length; i++) {
        s2 = s2.replace(s1[i], "!");
    }
    return s2.replace(/[^!]/g, "").length;
}

function commonCharacterCount2(s1, s2) {
    var a=s1.split(""),r=0
    while (a.length){
      var t=a.pop()
      if(s2.includes(t)){
        r++
        s2=s2.replace(t,"")
      }
    }
    return r
  }