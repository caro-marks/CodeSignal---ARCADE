/* 

ADD
write a function that returns the sum of two numbers

*/

function add1(param1,param2) {
    return param1+param2
}

const add2 = (param1,param2) => param1 + param2;

/* 

CENTURY FROM YEAR
Given a year, return the century it is in.

*/

function centuryFromYear1(year) {
    return Math.ceil(year / 100)
}

const centuryFromYear2 = y => Math.ceil(y / 100)

/*

CHECK PALINDROME
Given the string, check ir it is a palindrome.

*/

function checkPalindrome1(inputString) {
    return inputString == inputString.split('').reverse('').join('')
}

function checkPalindrome2(inputString) {
    return [...inputString].reverse().join('') === inputString
}

/*

ADJACENT ELEMENTS PRODUCT
Given an array of integers,
find the pair of adjacent elements that has the largest product and return that product.

*/

function adjacentElementsProduct1(inputArray) {
    var prod = inputArray[0] * inputArray[1];
    
    for (var i = 1; i<inputArray.length - 1;i++) {
        prod = Math.max(prod, inputArray[i] * inputArray[i+1]);
    }
    
    return prod
}

function adjacentElementsProduct2(arr) {
    return Math.max(...arr.slice(1).map((x,i)=>[x*arr[i]]))
}

/*

SHAPE AREA
Find the area of a n-interesting polygon for a given n.

*/

function shapeArea1(n) {
    return n**2 + (n-1)**2;
}

shapeArea2 = n => {
    return 2 * n * (n-1) + 1
}

/*

MAKE ARRAY CONSECUTIVE 2
Figure out

*/

function makeArrayConsecutive2(sequence) {
  return Math.max(...sequence) - Math.min(...sequence) - sequence.length + 1
}

/*

ALMOST INCREASING SEQUENCE
Given an array of integers,
determine if it's possible to obtain an increasing sequence by removing only one element.

*/

function almostIncreasingSequence1(seq) {
    var bad=0
    for(var i=1;i<seq.length;i++) if(seq[i]<=seq[i-1]) {
        bad++
        if(bad>1) return false
        if(seq[i]<=seq[i-2]&&seq[i+1]<=seq[i-1]) return false
    }
    return true
}

function almostIncreasingSequence2(sequence) {    
    if(sequence.length == 2) return true;

    var error = 0;

    for(var i = 0; i < sequence.length - 1; i++){
        if(sequence[i] >= sequence[i+1]){
            var noStepBack = sequence[i-1] && sequence[i-1] >= sequence[i+1];
            var noStepFoward = sequence[i+2] && sequence[i] >= sequence[i+2];
            if(i > 0 && noStepBack && noStepFoward) {
                error+=2;
            }else{
                error++;
            }
        }
        if(error > 1) return false;
    }
    return true;
}

/*

MATRIX ELEMENTS SUM
Given a matrix of integers,
add up all the values that don't appear below a 0.

*/

function matrixElementsSum1(matrix) {
    for(var r=0,j=0;j<matrix[0].length;j++){
        for(var i=0;i<matrix.length;i++){
          if(matrix[i][j]===0) break
          else r+=matrix[i][j]
        }
    }
    return r
}

function matrixElementsSum2(matrix) {
    let price = 0;
    for (let i = 0; i < matrix.length; i++){
        for (let j = 0; j < matrix[i].length; j++){
            price += matrix[i][j];            
            if (matrix[i][j] === 0 && i < matrix.length-1){
                matrix[i+1][j] = 0;
            }
        }
    }
    return price;
}