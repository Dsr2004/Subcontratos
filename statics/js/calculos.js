// Valores del subcontrato con tipo de contrato 1.1 y 1.2
function calcularTotal(){
    campoCantidad = document.getElementById("Cantidad").value
    campoValorUnitario = document.getElementById("ValorUnitario").value

    resultado = campoCantidad * campoValorUnitario

    campoTotal = document.getElementById("ValorTotal")
    campoTotal.value = resultado

}


function calcularSubtotal(){

    const resume_table = document.getElementById("tbl_items");

    const tableRows = document.querySelectorAll('#tbl_items tr.it_row');

    let subt = document.getElementById("subtot");

    let iva = document.getElementById("tarifaiva").value;

    let con = parseFloat(iva)
    let porc = (con / 100);

    
    for(let i = 0; i < tableRows.length; i++) {
        const row = tableRows[i];

        const status = row.querySelector('.valTot');
        let conversion= parseInt(status.innerHTML); 


        status.innerText = valorTotal;
    }
}


function calcularIva(){
    
    //VariabLES DE TIPO CONTRATO
    let iva = document.getElementById("tarifaiva").value
    
    let porcIva = parseFloat(iva) / 100
    let ValorSubto = document.getElementById("subtot")
    let conSubtot = parseFloat(ValorSubto.innerText)

    let CalcIva = porcIva * conSubtot
   

    let campoIva = document.getElementById("calciv")
    campoIva.innerHTML = CalcIva.toFixed(2)


    //Variables de tipo contrato 2
    let ivaT = document.getElementById("tarifaivaT").value
    
    let porcIvaT = parseFloat(ivaT) / 100
    let ValorSubtoT = document.getElementById("subtot3")
    let conSubtotT = parseFloat(ValorSubtoT.innerText)

    let CalcIvaT = porcIvaT * conSubtotT
   

    let campoIvaT = document.getElementById("iv3")
    campoIvaT.innerHTML = CalcIvaT.toFixed(2)
}


function CalcularAdmins(){
    let CamPorcAd = document.getElementById("porcAdmin").value
    
    let porcAd = parseFloat(CamPorcAd) / 100
    let Subt = document.getElementById("subtot3")
    let convSubtotT = parseFloat(Subt.innerText)

    let CalcPorcAdmin = porcAd * convSubtotT
   

    let campoAdmin = document.getElementById("admin2")
    campoAdmin.innerHTML = CalcPorcAdmin.toFixed(2)
}


function CalcularImprevist(){
    let CamPorcImprv = document.getElementById("porcImpr").value
    
    let porcImprv = parseFloat(CamPorcImprv) / 100
    let Subtt = document.getElementById("subtot3")
    let convSub = parseFloat(Subtt.innerText)

    let CalcPorcImprev = porcImprv * convSub
   

    let campoImprev = document.getElementById("imprev2")
    campoImprev.innerHTML = CalcPorcImprev.toFixed(2)
}

function CalcularUtilidad(){
    let CamPorcUtil = document.getElementById("porcUtil").value
    
    let porcUtil = parseFloat(CamPorcUtil) / 100
    let Subtu = document.getElementById("subtot3")
    let convSubtu = parseFloat(Subtu.innerText)

    let CalcPorcUtili = porcUtil * convSubtu
   

    let campoUtili = document.getElementById("util2")
    campoUtili.innerHTML = CalcPorcUtili.toFixed(2)
}

function CalcularIvaUtilidad(){
    let CamI = document.getElementById("tarifaivaT").value

    let porcImprv = parseFloat(CamI) / 100
    let Util = document.getElementById("util2")
    let convUtil = parseFloat(Util.innerText)

    let CalcIvaUtil = porcImprv * convUtil

    let campoIvaUt = document.getElementById("ivu2")
    campoIvaUt.innerHTML = CalcIvaUtil.toFixed(2)
}



function CalcularT(){
    let ValorSubto = document.getElementById("subtot")
    let campoIva = document.getElementById("calciv")

    let total = document.getElementById("Tot")

    let sum =  parseFloat(ValorSubto.innerText) + parseFloat(campoIva.innerText)
    total.innerHTML = sum.toFixed(2)


    //Variables contrato 2
    let ValorSubtoT = document.getElementById("subtot3")
    let campoAdministracion = document.getElementById("admin2")
    let campoImprevistos = document.getElementById("imprev2")
    let campoUtilidad= document.getElementById("util2")
    let campoIvaT = document.getElementById("iv3")
    let campoIvaUti = document.getElementById("ivu2")

    console.log(parseFloat(campoIvaUti.innerText))
    let totalT = document.getElementById("Tot3")

    let sumT =  parseFloat(ValorSubtoT.innerText) + parseFloat(campoIvaT.innerText) + parseFloat(campoAdministracion.innerText) + parseFloat(campoImprevistos.innerText) + parseFloat(campoUtilidad.innerText) + parseFloat(campoIvaUti.innerText)
    totalT.innerHTML = sumT.toFixed(2)
}


// Calculos del contratos tipo 2
function calcularSubtotal(){

    const resume_table = document.getElementById("tbl_items");

    const tableRows = document.querySelectorAll('#tbl_items tr.it_row');

    let subt = document.getElementById("subtot3");

    let iva = document.getElementById("tarifaiva").value;

    let con = parseFloat(iva)
    let porc = (con / 100);

    
    for(let i = 0; i < tableRows.length; i++) {
        const row = tableRows[i];

        const status = row.querySelector('.valTot');
        let conversion= parseInt(status.innerHTML); 


        status.innerText = valorTotal;
    }
}
