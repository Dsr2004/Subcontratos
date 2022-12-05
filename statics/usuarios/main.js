function guardarUsuario(){
    let form = $("#registroUsuarioForm")
    $.ajax({
        type: form.attr("method") ,
        url: form.attr("action") ,
        data: form.serialize() ,
        success: function (response) {
            console.log(response)
            location.reload()
        },
        error: function (errores) {
            errores = errores.responseJSON["errores"]
            form.find('.error_text').text('');
            form.find('.is-invalid').removeClass('is-invalid');
            for (let i in errores){
                let x=form.find('input[name='+i+']')
                let y=form.find('select[name='+i+']')
                x.addClass("is-invalid")
                y.addClass("is-invalid")
                $("#"+i).text(errores[i]) 
            }
        }
    });
}

function abrirModalModificarUsuario(url){
    $("#modificarUsuarioModal").load(url, function(){
        $(this).appendTo("body").modal('show');
    })
}

