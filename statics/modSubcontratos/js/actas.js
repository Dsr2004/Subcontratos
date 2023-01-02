function abrir_modal_seguimiento_acta(url){
    $("#verSeguimientoActaModal").load(url, function(){
        $(this).appendTo("body").modal("show")
    })
}

$(document).ready(function() {
    // items
    $('#Acta_item').select2({
        theme: "bootstrap-5",
        width:"100%",
        language: "es",
        allowClear: true,
        dropdownParent: $('#AddActa'),
        ajax:{
            delay: 250,
            url: '/Subcontratos/BusquedaInfoSubcontrato/',
            type: "POST",
            data: function(params){
            var queryParams = {
                csrfmiddlewaretoken:csrftoken,
                term: params.term,
                subcontrato: $("#PK_Subcontrato").val(),
                action: "autocompleteItemActa",
                tipo: "acta"
            }
            return queryParams
            },
            processResults: function(data){
                return{
                    results: $.map(data, function(item){
                        return {id: item.id, text:item.item_nombre}
                    })
                }
            }
        },
        placeholder: "Ingrese el ítem",
        minimumInputLength :1
    });

    $('#Acta_item').on("change", function(){
        $.ajax({
            type: "POST",
            url: '/Subcontratos/BusquedaInfoSubcontrato/',
            data: {"csrfmiddlewaretoken":csrftoken,"item":$(this).val(),"action":"descripcionItem", tipo: "acta"},
            success: function(response){
                respuesta = JSON.stringify(response)
                respuesta = JSON.parse(respuesta)
                $("#Acta_Unidad").val(respuesta["unidad"])
                $("#Acta_valor_unitario").val(respuesta["valor"])
                $('#Acta_descripcion').empty().select2({
                    data:[{id:respuesta["id"], text:respuesta["descripcion"]}],
                    theme: "bootstrap-5",
                    width:"100%",
                    language: "es",
                    dropdownParent: $('#AddActa'),
                    allowClear: true,
                    ajax:{
                        delay: 250,
                        url: '/Subcontratos/BusquedaInfoSubcontrato/',
                        type: "POST",
                        data: function(params){
                        var queryParams = {
                            csrfmiddlewaretoken:csrftoken,
                            term: params.term,
                            subcontrato: $("#PK_Subcontrato").val(),
                            action: "autocompleteDescripcionItem",
                            tipo: "acta"
                        }
                        return queryParams
                        },
                        processResults: function(data){
                            return{
                                results: $.map(data, function(item){
                                    return {id: item.id, text:item.descripcion}
                                })
                            }
                        }
                    }, //fin de ajax
                    placeholder: "Ingrese la descripción",
                    minimumInputLength :1
                });
            }
        });
    })
    $('#Acta_descripcion').select2({
        theme: "bootstrap-5",
        width:"100%",
        language: "es",
        allowClear: true,
        dropdownParent: $('#AddActa'),
        ajax:{
            delay: 250,
            url: '/Subcontratos/BusquedaInfoSubcontrato/',
            type: "POST",
            data: function(params){
            var queryParams = {
                csrfmiddlewaretoken:csrftoken,
                term: params.term,
                subcontrato: $("#PK_Subcontrato").val(),
                action: "autocompleteDescripcionItem",
                tipo: "acta"
            }
            return queryParams
            },
            processResults: function(data){
                return{
                    results: $.map(data, function(item){
                        return {id: item.id, text:item.descripcion}
                    })
                }
            }
        },
        placeholder: "Ingrese la descripción",
        minimumInputLength :1
    });

    $('#Acta_descripcion').on("change", function(){
        $.ajax({
            type: "POST",
            url: '/Subcontratos/BusquedaInfoSubcontrato/',
            data: {"csrfmiddlewaretoken":csrftoken,"item":$(this).val(),"action":"Itemdescripcion", tipo: "acta"},
            success: function(response){
                respuesta = JSON.stringify(response)
                respuesta = JSON.parse(respuesta)
                $("#Acta_Unidad").val(respuesta["unidad"])
                $("#Acta_valor_unitario").val(respuesta["valor"])
                $('#Acta_item').empty().select2({
                    data:[{id:respuesta["id"], text:respuesta["item"]}],
                    theme: "bootstrap-5",
                    width:"100%",
                    language: "es",
                    dropdownParent: $('#AddActa'),
                    allowClear: true,
                    ajax:{
                        delay: 250,
                        url: '/Subcontratos/BusquedaInfoSubcontrato/',
                        type: "POST",
                        data: function(params){
                        var queryParams = {
                            csrfmiddlewaretoken:csrftoken,
                            term: params.term,
                            subcontrato: $("#PK_Subcontrato").val(),
                            action: "autocompleteItemActa",
                            tipo: "acta"
                        }
                        return queryParams
                        },
                        processResults: function(data){
                            return{
                                results: $.map(data, function(item){
                                    return {id: item.id, text:item.item_nombre}
                                })
                            }
                        }
                    }, //fin de ajax
                    placeholder: "Ingrese la descripción",
                    minimumInputLength :1
                });
            }
        });
    })
})