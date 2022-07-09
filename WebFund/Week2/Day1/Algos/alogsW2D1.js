var fruit1 = "apples";
var fruit2 = "oranges";
    
fruit2 = fruit1;
    
console.log(fruit2 + " and " + fruit1);

var fruit1 = "apples";
var fruit2 = "oranges";
    
var temp = fruit1; // temp is a common name for this
fruit1 = fruit2; //oranges
fruit2 = temp; //apples
    
console.log(fruit2 + " and " + fruit1); //logs apples and oranges

var start = 0;
var end = 12;
    
while(start < end) {
    console.log("start: " + start + ", end: " + end);
    start += 2;
    end -= 2;
}
// 0 and 12, 2 and 10, 4 and 8 

arr =["a","b","c","d","e"];
function reverse(){
    arr1 = [];
    for (var i = arr.length - 1; i >= 0; i--) {
    arr1.push(arr[i]);
}
console.log(arr1);
}
reverse(arr);

function reverse(arr){
    arr.reverse();
    console.log(arr);
    return arr;
}
reverse(["a","b","c","d","e"]); 
console.log (reverse);