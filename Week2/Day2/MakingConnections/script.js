
function accept1(){
    var fiveHun = document.getElementById('fiveHun').innerText;
    fiveHun++;
    document.getElementById('fiveHun').innerText = fiveHun;
    hide();
    minusRequest();
}
function close1(){
    var fiveHun = document.getElementById('fiveHun').innerText;
    fiveHun;
    document.getElementById('fiveHun').innerText = fiveHun;
    hide();
    minusRequest();
}

function accept2(){
    var fiveHun = document.getElementById('fiveHun').innerText;
    fiveHun++;
    document.getElementById('fiveHun').innerText = fiveHun;
    hide2();
    minusRequest();
}

function close2(){
    var fiveHun = document.getElementById('fiveHun').innerText;
    fiveHun;
    document.getElementById('fiveHun').innerText = fiveHun;
    hide2();
    minusRequest();
}
function hide(element){
    // var friend1= document.getElementsById('toddPic');
    element.remove();
    minusRequest();
    
}
function hide2(element){
    // var friend1= document.getElementsById('toddPic');
    element.remove();
    minusRequest();
}
function minusRequest(){
    var two = document.getElementById('two').innerText;
    two--;
    document.getElementById('two').innerText = two;
}
function editProfile(){
    var name = document.getElementById('nameTag').innerText;
    name = "Johnathon Doe";
    document.getElementById('nameTag').innerText = name;
    
}
