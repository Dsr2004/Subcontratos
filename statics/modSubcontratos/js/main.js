  $(document).ready(function() {
    // elaborador
        $('#elaborador').select2({
            theme: "bootstrap-5",
            width:"100%",
            language: "es",
            allowClear: true,
            ajax:{
                delay: 250,
                url: '/Subcontratos/BusquedaInfoSubcontrato/',
                type: "POST",
                data: function(params){
                var queryParams = {
                    csrfmiddlewaretoken:csrftoken,
                    term: params.term,
                    action: "autocompleteElaborador",
                    tipo: "elaborador"
                }
                return queryParams
                },
                processResults: function(data){
                    return{
                        results: $.map(data, function(item){
                            return {id: item.id, text:item.razon_social}
                        })
                    }
                }
            },
            placeholder: "Ingrese el nombre del elaborador",
            minimumInputLength :1
        });
        $('#elaborador').on("change", function(){
            $.ajax({
                type: "POST",
                url: '/Subcontratos/BusquedaInfoSubcontrato/',
                data: {"csrfmiddlewaretoken":csrftoken,"elaborador":$(this).val(),"action":"CargoElaborador", "tipo":"elaborador"},
                success: function (response) {
                    respuesta = JSON.stringify(response)
                    respuesta = JSON.parse(respuesta)["cargoElaborador"]
                    $("#cargoElaborador").val(respuesta)
                    
                }
                // error: function(e){
                //     console.log(e)
                //     alert("error")
                // }
            });
        })
    // proyecto
    $('#proyecto').select2({
            theme: "bootstrap-5",
            width:"100%",
            language: "es",
            allowClear: true,
            ajax:{
                delay: 250,
                url: '/Subcontratos/BusquedaInfoSubcontrato/',
                type: "POST",
                data: function(params){
                var queryParams = {
                    csrfmiddlewaretoken:csrftoken,
                    term: params.term,
                    action: "autocompleteProyecto",
                    tipo: "proyecto"
                }
                return queryParams
                },
                processResults: function(data){
                    return{
                        results: $.map(data, function(item){
                            return {id: item.id, text:item.nombre_proyecto}
                        })
                    }
                }
            },
            placeholder: "Ingrese el nombre del proyecto",
            minimumInputLength :1
        });
        $('#proyecto').on("change", function(){
            $.ajax({
                type: "POST",
                url: '/Subcontratos/BusquedaInfoSubcontrato/',
                data: {"csrfmiddlewaretoken":csrftoken,"proyecto":$(this).val(),"action":"centroOperacionesProyecto",tipo: "proyecto"},
                success: function (response) {
                    respuesta = JSON.stringify(response)
                    respuesta = JSON.parse(respuesta)
                    $('#centro_de_operaciones').empty().select2({
                        data:[{id:respuesta["id"], text:respuesta["id_proyecto"]}],
                        theme: "bootstrap-5",
                        width:"100%",
                        language: "es",
                        allowClear: true,
                        ajax:{
                            delay: 250,
                            url: '/Subcontratos/BusquedaInfoSubcontrato/',
                            type: "POST",
                            data: function(params){
                            var queryParams = {
                                csrfmiddlewaretoken:csrftoken,
                                term: params.term,
                                action: "autocompleteCentroOperaciones",
                                tipo: "proyecto"
                            }
                            return queryParams
                            },
                            processResults: function(data){
                                return{
                                    results: $.map(data, function(item){
                                        return {id: item.id, text:item.id_proyecto}
                                    })
                                }
                            }
                        },
                        placeholder: "Ingrese el ID del proyecto",
                        minimumInputLength :1
                    })     
                }
                // error: function(e){
                //     console.log(e)
                //     alert("error")
                // }
            });
        })
        $('#centro_de_operaciones').select2({
            theme: "bootstrap-5",
            width:"100%",
            language: "es",
            allowClear: true,
            ajax:{
                delay: 250,
                url: '/Subcontratos/BusquedaInfoSubcontrato/',
                type: "POST",
                data: function(params){
                var queryParams = {
                    csrfmiddlewaretoken:csrftoken,
                    term: params.term,
                    action: "autocompleteCentroOperaciones",
                    tipo: "proyecto",
                }
                return queryParams
                },
                processResults: function(data){
                    return{
                        results: $.map(data, function(item){
                            return {id: item.id, text:item.id_proyecto}
                        })
                    }
                }
            },
            placeholder: "Ingrese el ID del proyecto",
            minimumInputLength :1
        });

        $('#centro_de_operaciones').on("change", function(){
            $.ajax({
                type: "POST",
                url: '/Subcontratos/BusquedaInfoSubcontrato/',
                data: {"csrfmiddlewaretoken":csrftoken,"centroOperacion":$(this).val(),"action":"proyectoCentroOperaciones", tipo: "proyecto"},
                success: function(response){
                    respuesta = JSON.stringify(response)
                    respuesta = JSON.parse(respuesta)
                    $('#proyecto').empty().select2({
                        data:[{id:respuesta["id"], text:respuesta["proyecto"]}],
                        theme: "bootstrap-5",
                        width:"100%",
                        language: "es",
                        allowClear: true,
                        ajax:{
                            delay: 250,
                            url: '/Subcontratos/BusquedaInfoSubcontrato/',
                            type: "POST",
                            data: function(params){
                            var queryParams = {
                                csrfmiddlewaretoken:csrftoken,
                                term: params.term,
                                action: "autocompleteProyecto",
                                tipo: "proyecto"
                            }
                            return queryParams
                            },
                            processResults: function(data){
                                return{
                                    results: $.map(data, function(item){
                                        return {id: item.id, text:item.nombre_proyecto}
                                    })
                                }
                            }
                        }, //fin de ajax
                        placeholder: "Ingrese el nombre del proyecto",
                        minimumInputLength :1
                    });
                }
            });
        })
        // proveedor
        $('#nit').select2({
            theme: "bootstrap-5",
            width:"100%",
            language: "es",
            allowClear: true,
            ajax:{
                delay: 250,
                url: '/Subcontratos/BusquedaInfoSubcontrato/',
                type: "POST",
                data: function(params){
                var queryParams = {
                    csrfmiddlewaretoken:csrftoken,
                    term: params.term,
                    action: "autocompleteNit",
                    tipo: "proveedor"
                }
                return queryParams
                },
                processResults: function(data){
                    return{
                        results: $.map(data, function(item){
                            return {id: item.id, text:item.nit}
                        })
                    }
                }
            },
            placeholder: "Ingrese el NIT",
            minimumInputLength :1
        });
        $('#proveedor').select2({
            theme: "bootstrap-5",
            width:"100%",
            language: "es",
            allowClear: true,
            ajax:{
                delay: 250,
                url: '/Subcontratos/BusquedaInfoSubcontrato/',
                type: "POST",
                data: function(params){
                var queryParams = {
                    csrfmiddlewaretoken:csrftoken,
                    term: params.term,
                    action: "autocompleteProveedor",
                    tipo: "proveedor"
                }
                return queryParams
                },
                processResults: function(data){
                    return{
                        results: $.map(data, function(item){
                            return {id: item.id, text:item.razon_social}
                        })
                    }
                }
            },
            placeholder: "Ingrese el nombre del proveedor",
            minimumInputLength :1
        });
        $('#nit').on("change", function(){
            $.ajax({
                type: "POST",
                url: '/Subcontratos/BusquedaInfoSubcontrato/',
                data: {"csrfmiddlewaretoken":csrftoken,"nit":$(this).val(),"action":"proveedordelNIT", tipo:"proveedor"},
                success: function(response){
                    let respuesta = JSON.stringify(response)
                    respuesta = JSON.parse(respuesta)
                    $("#correo_notificacion_proveedor").val(respuesta["email"])
                    $('#proveedor').empty().select2({
                        data:[{id:respuesta["id"], text:respuesta["proveedor"]}],
                        theme: "bootstrap-5",
                        width:"100%",
                        language: "es",
                        allowClear: true,
                        ajax:{
                            delay: 250,
                            url: '/Subcontratos/BusquedaInfoSubcontrato/',
                            type: "POST",
                            data: function(params){
                            var queryParams = {
                                csrfmiddlewaretoken:csrftoken,
                                term: params.term,
                                action: "autocompleteProveedor",
                                tipo: "proveedor"
                            }
                            return queryParams
                            },
                            processResults: function(data){
                                return{
                                    results: $.map(data, function(item){
                                        return {id: item.id, text:item.razon_social}
                                    })
                                }
                            }
                        }, //fin de ajax
                        placeholder: "Ingrese el nombre del proveedor",
                        minimumInputLength :1
                    });
                }
            });
        })
        $('#proveedor').on("change", function(){
            $.ajax({
                type: "POST",
                url: '/Subcontratos/BusquedaInfoSubcontrato/',
                data: {"csrfmiddlewaretoken":csrftoken,"proveedor":$(this).val(), "action":"NITdelProveedor", tipo:"proveedor"},
                success: function(response){
                    respuesta = JSON.stringify(response)
                    respuesta = JSON.parse(respuesta)
                    $("#correo_notificacion_proveedor").val(respuesta["email"])
                    $('#nit').empty().select2({
                        data:[{id:respuesta["id"], text:respuesta["nit"]}],
                        theme: "bootstrap-5",
                        width:"100%",
                        language: "es",
                        allowClear: true,
                        ajax:{
                            delay: 250,
                            url: '/Subcontratos/BusquedaInfoSubcontrato/',
                            type: "POST",
                            data: function(params){
                            var queryParams = {
                                csrfmiddlewaretoken:csrftoken,
                                term: params.term,
                                action: "autocompleteNit",
                                tipo: "proveedor"
                            }
                            return queryParams
                            },
                            processResults: function(data){
                                return{
                                    results: $.map(data, function(item){
                                        return {id: item.id, text:item.nit}
                                    })
                                }
                            }
                        },
                        placeholder: "Ingrese el NIT",
                        minimumInputLength :1
                    });
                }
            });
        })
        //compa??ia
        $('#compania').select2({
            theme: "bootstrap-5",
            width:"100%",
            language: "es",
            allowClear: true,
            ajax:{
                delay: 250,
                url: '/Subcontratos/BusquedaInfoSubcontrato/',
                type: "POST",
                data: function(params){
                var queryParams = {
                    csrfmiddlewaretoken:csrftoken,
                    term: params.term,
                    action: "autocompleteCompania",
                    tipo: "compania"
                }
                return queryParams
                },
                processResults: function(data){
                    return{
                        results: $.map(data, function(item){
                            return {id: item.id, text:item.compania}
                        })
                    }
                }
            },
            placeholder: "Ingrese el nombre de la compa??ia",
            minimumInputLength :1
        });
     //items
     $('#Codigo').select2({
        theme: "bootstrap-5",
        language: "es",
        allowClear: true,
        ajax:{
            delay: 250,
            url: '/Subcontratos/BusquedaInfoSubcontrato/',
            type: "POST",
            data: function(params){
            var queryParams = {
                csrfmiddlewaretoken:csrftoken,
                term: params.term,
                action: "autocompleteItem",
                tipo: "item"
            }
            return queryParams
            },
            processResults: function(data){
                return{
                    results: $.map(data, function(item){
                        return {id: item.id, text:item.final}
                    })
                }
            }
        },
        placeholder: "Ingrese el codigo",
        minimumInputLength :3,
        scrollAfterSelect:true
    });
    // items del subcapitulo
     $('#CodigoSub').select2({
        theme: "bootstrap-5",
        language: "es",
        allowClear: true,
        ajax:{
            delay: 250,
            url: '/Subcontratos/BusquedaInfoSubcontrato/',
            type: "POST",
            data: function(params){
            var queryParams = {
                csrfmiddlewaretoken:csrftoken,
                term: params.term,
                action: "autocompleteItem",
                tipo: "item"
            }
            return queryParams
            },
            processResults: function(data){
                return{
                    results: $.map(data, function(item){
                        return {id: item.id, text:item.final}
                    })
                }
            }
        },
        placeholder: "Ingrese el codigo",
        minimumInputLength :3,
        scrollAfterSelect:true,
        dropdownParent: $('#AddSubcapitulo'),
        width:"20vw"
    });
    // elaboradores
    $('#validadores').select2({
        language: "es",
        theme: "bootstrap-5",
        width:"100%",
        placeholder: "Seleccione a los validadores",
        closeOnSelect: false,
        allowClear: false,
    });

    //Polizas
    $('#Tipo_Poliza').select2({
        language: "es",
        theme: "bootstrap-5",
        width:"100%",
        placeholder: "Seleccione el tipo de poliza",
        closeOnSelect: true,
        allowClear: false,
        tags: true,
    });
    $('#id_aseguradora').select2({
        language: "es",
        theme: "bootstrap-5",
        width:"100%",
        placeholder: "Seleccione la aseguradora",
        closeOnSelect: true,
        allowClear: false,
    });
    //Subcapitulos
    $('#Subcapitulos').select2({
        language: "es",
        theme: "bootstrap-5",
        width:"100%",
        placeholder: "Seleccione el subcapitulo",
        closeOnSelect: true,
        allowClear: false,
        tags: true,
        dropdownParent: $('#AddSubcapitulo'),
    });

});


function guardarSubcontrato(){
    let items = JSON.stringify(ItemsObject.data)
    let polizas = JSON.stringify(PolizasObject.data)
    let form = $("#guardarSubcontratoForm")

    $("#slec").prop("disabled", false)
    let tipo_orden = $("#slec").val()
    $("#slec").prop("disabled", true)
    if ($('#comboA').val() == "3"){
        $("#slec").prop("disabled", false)
    }

    let formData = new FormData(document.getElementById("guardarSubcontratoForm"));
    formData.append("items",items)
    formData.append("listpolizas",polizas)
    formData.append("tipo_orden",tipo_orden)

    $.ajax({
        type:form.attr("method"),
        url:form.attr("action"),
        processData: false,
        contentType: false,
        data: formData,
        success: function(response) {
            form.find('.error_text').text('');
            form.find('.is-invalid').removeClass('is-invalid');
            location.href = response["path"]
        },
        error: function(errors){
            form.find('.error_text').text('');
            form.find('.is-invalid').removeClass('is-invalid');
            tipo = errors.responseJSON["tipo"]
            if(tipo){
                if(tipo=="general"){
                    Swal.fire({
                        icon: 'error',
                        title: '??Error!',
                        text: errors.responseJSON["errores"],
                      })
                }
            }else{
                console.log(errors)
                errores = errors.responseJSON["errores"]
                form.find('.error_text').text('');
                form.find('.is-invalid').removeClass('is-invalid');
                for (let i in errores){
                    let x=form.find('input[name='+i+']')
                    let y=form.find('select[name='+i+']')
                    x.addClass("is-invalid")
                    y.addClass("is-invalid")
                    $("#P_"+i).text(errores[i])
                }
            }
            
        }
    });
}

function modificarrSubcontrato(){
    const items = JSON.stringify(ItemsObject.data)
    const polizas = JSON.stringify(PolizasObject.data)
    let form = $("#modificarrSubcontratoForm")

    $("#slec").prop("disabled", false)
    let tipo_orden = $("#slec").val()
    $("#slec").prop("disabled", true)
    if ($('#comboA').val() == "3"){
        $("#slec").prop("disabled", false)
    }

    let formData = new FormData(document.getElementById("modificarrSubcontratoForm"));
    // formData.append("items",items)
    // formData.append("listpolizas",polizas)
    formData.append("tipo_orden",tipo_orden)

    $.ajax({
        type:form.attr("method"),
        url:form.attr("action"),
        processData: false,
        contentType: false,
        data: formData,
        success: function(response) {
            form.find('.error_text').text('');
            form.find('.is-invalid').removeClass('is-invalid');
            location.href = response["path"]
        },
        error: function(errors){
            form.find('.error_text').text('');
            form.find('.is-invalid').removeClass('is-invalid');
            tipo = errors.responseJSON["tipo"]
            if(tipo){
                if(tipo=="general"){
                    Swal.fire({
                        icon: 'error',
                        title: '??Error!',
                        text: errors.responseJSON["errores"],
                      })
                }
            }else{
                console.log(errors)
                errores = errors.responseJSON["errores"]
                form.find('.error_text').text('');
                form.find('.is-invalid').removeClass('is-invalid');
                for (let i in errores){
                    let x=form.find('input[name='+i+']')
                    let y=form.find('select[name='+i+']')
                    x.addClass("is-invalid")
                    y.addClass("is-invalid")
                    $("#P_"+i).text(errores[i])
                }
            }
            
        }
    });
}