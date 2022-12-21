// Alerta
function cargando() {
    alert("Loading weather report...");
}
// Eliminar msj cookies
var ck = document.querySelector("#CK");
function EliminarCK() {
    ck.remove();
}
// Cambio Temperaturas
function ctof(temp) {
    return Math.round(9 / 5 * temp + 32);
}
function ftoc(temp) {
    return Math.round(5 / 9 * (temp - 32));
}
function convert(element) {
    console.log(element.value);
    for(var i=1; i<=8; i++) {
        var temperatureSpan = document.querySelector("#temp" + i);
        var tempVal = parseInt(temperatureSpan.innerText);
        if(element.value == "°C") {
            temperatureSpan.innerText = ftoc(tempVal) + "°  ";
        } else {
            temperatureSpan.innerText = "  " + ctof(tempVal);
        }
    }
}

