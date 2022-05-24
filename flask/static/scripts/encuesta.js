var ro = document.querySelector(":root");
window.addEventListener("load", startup, false);
var color = sessionStorage.getItem('colorf');
var btn_encuesta = document.getElementById("btn-encuesta");
btn_encuesta.addEventListener("click",registrar, false);

function startup() {
    ro.style.setProperty('--color-f',sessionStorage.getItem('colorf'));
}

function registrar(){
    document.getElementById('fm-preguntas').submit();
}
