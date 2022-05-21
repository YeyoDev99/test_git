const pi = Math.PI

function calculationArea(radio){
    var result = radio*radio * pi
    return result
}

function calculationDiameter(radio){
    var result = radio*2 * pi
    return result
}


function run(){
    var radioInput = document.getElementById("radio")
    var radioValue = radioInput.value
    if (isNaN(radioValue) || radioValue.length < 1){
        var answerInput = document.getElementById("answer") 
        answerInput.innerText = "por favor digita un numero, no se permite texto ni espacio vacio"
    }
    else{ var radio = Number(radioValue)
        var diameter = calculationDiameter(radio)
        var area = calculationArea(radio)
        diameter = parseInt(diameter)
        area = parseInt(area)
        area = String(area)
        diameter = String(diameter)
        var answerInput = document.getElementById("answer") 
        answerInput.innerText = "el area de tu circulo es " + area + " y el diametro de tu circulo es " + diameter}  
}