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

function actualizarEstadoUsuario(url,id){
    const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success',
        cancelButton: 'btn btn-danger'
      },
      buttonsStyling: false
    })
    
    swalWithBootstrapButtons.fire({
      title: '¿Estas Seguro?',
      text: "¡Se modificará el estado del usuario!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: '¡Si, Modificar!',
      cancelButtonText: '¡No, Cancelar!',
      confirmButtonClass: "buttonSweetalert",
      reverseButtons: true
    }).then((result) => {
      if (result.isConfirmed) {
        console.log(csrftoken)
       $.ajax({
        url:url,
        type:"POST",
        data:{"csrfmiddlewaretoken":csrftoken,"id":id},
        success: function(){
           swalWithBootstrapButtons.fire(
          'Modificado!',
          'El estado del usuario se ha modificado',
          'success'
        ).then(function(){
          location.reload()
        })
        },
        error: function(){
           swalWithBootstrapButtons.fire(
          'ERROR!',
          'ha ocurrido un error.',
          'error'
        )
        },
       })
      } else if (
        /* Read more about handling dismissals below */
        result.dismiss === Swal.DismissReason.cancel
      ) {
        swalWithBootstrapButtons.fire(
          'Cancelado',
          'No se han aplicado cambios',
          'error'
        ).then(function(){
          location.reload()
        })
      }
    })
  }