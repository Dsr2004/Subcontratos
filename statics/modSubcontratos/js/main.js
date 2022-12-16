  $(document).ready(function() {
    // elaborador
        $('#elaborador').select2({
            language: "es",
            allowClear: true,
            ajax:{
                delay: 250,
                url: window.location.pathname,
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
                url: window.location.pathname,
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
            language: "es",
            allowClear: true,
            ajax:{
                delay: 250,
                url: window.location.pathname,
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
                url: window.location.pathname,
                data: {"csrfmiddlewaretoken":csrftoken,"proyecto":$(this).val(),"action":"centroOperacionesProyecto",tipo: "proyecto"},
                success: function (response) {
                    respuesta = JSON.stringify(response)
                    respuesta = JSON.parse(respuesta)
                    $('#centro_de_operaciones').empty().select2({
                        data:[{id:respuesta["id"], text:respuesta["id_proyecto"]}],
                        language: "es",
                        allowClear: true,
                        ajax:{
                            delay: 250,
                            url: window.location.pathname,
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
            language: "es",
            allowClear: true,
            ajax:{
                delay: 250,
                url: window.location.pathname,
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
                url: window.location.pathname,
                data: {"csrfmiddlewaretoken":csrftoken,"centroOperacion":$(this).val(),"action":"proyectoCentroOperaciones", tipo: "proyecto"},
                success: function(response){
                    respuesta = JSON.stringify(response)
                    respuesta = JSON.parse(respuesta)
                    $('#proyecto').empty().select2({
                        data:[{id:respuesta["id"], text:respuesta["proyecto"]}],
                        language: "es",
                        allowClear: true,
                        ajax:{
                            delay: 250,
                            url: window.location.pathname,
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
            language: "es",
            allowClear: true,
            ajax:{
                delay: 250,
                url: window.location.pathname,
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
            language: "es",
            allowClear: true,
            ajax:{
                delay: 250,
                url: window.location.pathname,
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
                url: window.location.pathname,
                data: {"csrfmiddlewaretoken":csrftoken,"nit":$(this).val(),"action":"proveedordelNIT", tipo:"proveedor"},
                success: function(response){
                    respuesta = JSON.stringify(response)
                    respuesta = JSON.parse(respuesta)
                    $('#proveedor').empty().select2({
                        data:[{id:respuesta["id"], text:respuesta["proveedor"]}],
                        language: "es",
                        allowClear: true,
                        ajax:{
                            delay: 250,
                            url: window.location.pathname,
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
                url: window.location.pathname,
                data: {"csrfmiddlewaretoken":csrftoken,"proveedor":$(this).val(), "action":"NITdelProveedor", tipo:"proveedor"},
                success: function(response){
                    respuesta = JSON.stringify(response)
                    respuesta = JSON.parse(respuesta)
                    console.log(respuesta)
                    $('#nit').empty().select2({
                        data:[{id:respuesta["id"], text:respuesta["nit"]}],
                        language: "es",
                        allowClear: true,
                        ajax:{
                            delay: 250,
                            url: window.location.pathname,
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
        //compañia
        $('#compania').select2({
            language: "es",
            allowClear: true,
            ajax:{
                delay: 250,
                url: window.location.pathname,
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
            placeholder: "Ingrese el nombre de la compañia",
            minimumInputLength :1
        });
     //items
     $('#Codigo').select2({
        language: "es",
        allowClear: true,
        ajax:{
            delay: 250,
            url: window.location.pathname,
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



});