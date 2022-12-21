
var nombreUsuario = document.querySelector("h1")
function cambioUsuario() {
    nombreUsuario.innerText = "Maria Rosa R.";
}

var peticionesPl = document.querySelector("#peticiones");
var conexionesPl= document.querySelector("#conexiones");

function aceptar(id){
    var element = document.querySelector(id);
    element.remove();
    peticionesPl.innerText--;
    conexionesPl.innerText++;

}
function declinar(id){
    var element = document.querySelector(id);
    element.remove();
    peticionesPl.innerText--;
}

