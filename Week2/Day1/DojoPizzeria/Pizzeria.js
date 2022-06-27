
var pizzaStyle={
    crustType:["thin", "deep dish", "chicago","hand tossed", "keto"],
    sauceType:["traditional","marinara","alfredo","BBQ"],
    cheese: ["mozzerella", "cheddar","4 cheese blend","feta"],
    toppings:["pepperoni","sausage","chicken","bell pepper","jalapeno","onion","mushroom","works","olives"]
}
var p1 = pizzaOven("deep dish","traditional","mozzerella",["pepperoni","sausage"])
var p2 = pizzaOven("hand tossed","marinara",["mozzarella","feta"],["mushrooms","olives","onions"])
var p3 = pizzaOven("keto","alfredo","4 cheese blend",["chicken","bell pepper","onion"])
var p4 = pizzaOven("chicago","BBQ","4 cheese blend",["chicken","bell pepper","onion"])

function pizzaOven(crustType, sauceType, cheese, toppings){
var pizza={};
pizza.crustType = crustType;
pizza.sauceType = sauceType;
pizza.cheese = cheese;
pizza.toppings = toppings;
return pizza;
}

function randomIng(arr){
    var i = Math.floor(arr.length * Math.random());
    return arr[i];
}

function randomPizza(){
    var pizza = {};
    pizza.crustType = randomIng(pizzaStyle.crustType);
    pizza.sauceType = randomIng(pizzaStyle.sauceType);
    pizza.cheese = randomIng(pizzaStyle.cheese);
    pizza.toppings = randomIng(pizzaStyle.toppings);
    return pizza;
}
console.log(p1);
console.log(p2);
console.log(p3);
console.log(p4);
console.log(randomPizza());

// *****************************************KEPT BELOW CODE FOR REFERANCE***********************************//
// var taco1 = {
//     "tortilla": "soft corn tortilla",
//     "protein":  "tinga chicken",
//     "cheese":   "cotija cheese",
//     "toppings": ["lettuce", "pico de gallo", "guacamole"],
//     "tacoInfo": function() {
//         console.log("Tortilla: " + taco1.tortilla);
//         console.log("Protein:  " + taco1.protein);
//         console.log("Cheese:   " + taco1.cheese);
//         console.log("Toppings: " + taco1.toppings);
//     }
// }
    
// // we can now get all the delicious taco facts by
// taco1.tacoInfo(); // note we call this like a function because it is a function

// var taco1 = {
//     "tortilla": "soft corn tortilla",
//     "protein":  "tinga chicken",
//     "cheese":   "cotija cheese",
//     "toppings": ["lettuce", "pico de gallo", "guacamole"],
//     "tacoInfo": function() {
//         console.log("Tortilla: " + this.tortilla);
//         console.log("Protein:  " + this.protein);
//         console.log("Cheese:   " + this.cheese);
//         console.log("Toppings: " + this.toppings);
//     }
// }
    
// // we can now still get all the delicious taco facts by
// taco1.tacoInfo(); // note tacoInfo still gets called like a function

// var sandwich = {
//     bread:    "sourdough",
//     protein:  "london broil",
//     cheese:   "lacey swiss cheese",
//     toppings: ["romaine lettuce", "heirloom tomatoes", "horseradish sauce"]
// };
    
// console.log(sandwich);

// function sandwichFactory(bread, protein, cheese, toppings) {
//     var sandwich = {};
//     sandwich.bread = bread;
//     sandwich.protein = protein;
//     sandwich.cheese = cheese;
//     sandwich.toppings = toppings;
//     return sandwich;
// }
    
// var s1 = sandwichFactory("wheat", "turkey", "provolone", ["mustard", "fried onions", "arugula"]);
// console.log(s1);

