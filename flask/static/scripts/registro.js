var ro = document.querySelector(":root");
window.addEventListener("load", startup, false);
var color = sessionStorage.getItem('colorf');

function startup() {
    ro.style.setProperty('--color-f',sessionStorage.getItem('colorf'));
}

var btn_registrar = document.getElementById("btn-registrar");
btn_registrar.addEventListener("click",registrar, false);
function registrar() {
    document.getElementById('registro').submit();
}
