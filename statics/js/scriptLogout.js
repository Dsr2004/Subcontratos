
window.setTimeout(function() {
    $(".alert").fadeTo(500, 0).slideUp(500, function() {
        $(this).remove();
    });
}, 30000);


// 2) Script para avisar al usuario acerca de de los 5 minutos
setTimeout(function() {
    var noticia = document.querySelector("#advertencia");

    if(noticia){
        noticia.click();
    }
}, 1 * 150000);


// 3) Script para cerrar sesión

setTimeout(function() {
    var action = document.querySelector("#btn-logout");

    if(action){
        action.click();
    }
}, 1 * 30000);