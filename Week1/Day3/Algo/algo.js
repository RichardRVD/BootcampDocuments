var isSunny = true;
var temperature = 45; // let's assume degrees Fahrenheit
var isRaining = false;
var whatToBring = "I should bring: ";
    
if(isSunny) {
  whatToBring += "sunglasses, ";
}
if(temperature < 50) {
  whatToBring += "a coat, ";
}
if(isRaining) {
  whatToBring += "an umbrella, ";
}
whatToBring += "and a smile!";
    
console.log(whatToBring); //I should bring: sunglasses, a coat, and a smile!



for(var i=10; i>0; i--) {
    if(i != 2) {
      console.log(i); // logs 10, 9 ,8 ,7 ,6 ,5 , 4 , 3 , 1
    } else {
      console.log("ignition!"); //at 2 logs ignition instead of 2
    }
  }
  console.log("liftoff!"); //log output: 10,9,8,7,6,5,4,3,ignition!,1,liftoff!



  
var countPositives = 0;
var numbers = [3, 4, -2, 7, 16, -8, 0];

// We need to run through entire array to count the positive numbers only

    for(var i=0; i<numbers.length; i++){   //for loop that will run through arr.
        if(numbers[i] > -1){  //if statement requiring i to be > -1
            countPositives ++;  //change value of countPositives.
        }
    }
console.log("there are " + countPositives + " positive values"); //log there are 5 positive values



var countPositives = 0;
var numbers = [3, 4, -2, 7, 16, -8, 0];

// We need to run through entire array to count the positive numbers only

    for(var i=0; i<numbers.length; i++){     //for loop that will run through arr.
        if(numbers[i] > 0){    //if statement requiring i to be > 0 (if zero is not positive)
            countPositives= countPositives + 1; //change value of countPositives.
        }
    }
console.log("there are " + countPositives + " positive values"); //log there are 5 positive values
