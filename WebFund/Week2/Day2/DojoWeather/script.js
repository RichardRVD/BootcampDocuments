function hide(){
    var cookie = document.getElementById('nav4')
    cookie.remove();
}
var w1 = document.getElementById('toDeg1').innerText
var w2 = document.getElementById('toDeg2').innerText
var w3 = document.getElementById('tomDeg1').innerText
var w4 = document.getElementById('tomDeg2').innerText
var w5 = document.getElementById('friDeg1').innerText
var w6 = document.getElementById('friDeg2').innerText
var w7 = document.getElementById('satDeg1').innerText
var w8 = document.getElementById('satDeg2').innerText
function weatherSelect(){

    if(document.getElementById('toDeg1').innerText == '24°'){
        document.getElementById('toDeg1').innerText = '75°'
    }
    else(document.getElementById('toDeg1').innerText = '24°')

    if(document.getElementById('toDeg2').innerText == '18°'){
        document.getElementById('toDeg2').innerText = '65°'
    }
    else(document.getElementById('toDeg2').innerText = '18°')

    if(document.getElementById('tomDeg1').innerText == '27°'){
        document.getElementById('tomDeg1').innerText = '80°'
    }
    else(document.getElementById('tomDeg1').innerText = '27°')

    if(document.getElementById('tomDeg2').innerText == '19°'){
        document.getElementById('tomDeg2').innerText = '66°'
    }
    else(document.getElementById('tomDeg2').innerText = '19°')

    if(document.getElementById('friDeg1').innerText == '21°'){
        document.getElementById('friDeg1').innerText = '69°'
    }
    else(document.getElementById('friDeg1').innerText = '21°')

    if(document.getElementById('friDeg2').innerText == '16°'){
        document.getElementById('friDeg2').innerText = '61°'
    }
    else(document.getElementById('friDeg2').innerText = '16°')

    if(document.getElementById('satDeg1').innerText == '26°'){
        document.getElementById('satDeg1').innerText = '78°'
    }
    else(document.getElementById('satDeg1').innerText = '26°')

    if(document.getElementById('satDeg2').innerText == '21°'){
        document.getElementById('satDeg2').innerText = '70°'
    }
    else(document.getElementById('satDeg2').innerText = '21°')
}