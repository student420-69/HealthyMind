var muestrario;
var colorPredeterminado = "#FFFFFF";
var r = document.querySelector(":root");
var btn_color = document.getElementById("btn-color");
btn_color.addEventListener("click",registrar, false);

window.addEventListener("load", startup, false);

function startup() {
    muestrario = document.querySelector("#color_fav");
    muestrario.value = colorPredeterminado;
    muestrario.addEventListener("input", actualizarPrimero, false);
    muestrario.select();
}

function actualizarPrimero(event) {
    sessionStorage.setItem('colorf', event.target.value);
    r.style.setProperty('--color-fav',sessionStorage.getItem('colorf'));
}

function registrar(){
    document.getElementById('fm-color').submit();
}

