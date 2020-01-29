document.addEventListener('DOMContentLoaded', () => {
    $('select').select2();
    const cboReserva = document.getElementById('cbo_reserva');
    const cboEncargado = document.getElementById('cbo_encargado');
    const cboContrato = document.getElementById('cbo_contrato');
    const txt_solicitante = document.getElementById('txt_solicitante');
    const txt_fecha = document.getElementById('txt_fecha');
    const txt_contrato = document.getElementById('txt_contrato');
    const btnActualizar = document.getElementById('btnActualizar');
    let datosReserva = {};
    let textoPlantilla = '';
    let datosEncargado = {};
    
    //Asignar evento change a reserva   
    $('#cbo_reserva').change(function() {
        const idreserva = cboReserva.value;
        if(idreserva != '') {            
            llenarFormulario(idreserva);
            cboEncargado.disabled = false;
        }
    });

    //Asignar evento change a cboEncargado   
    $('#cbo_encargado').change(async function() {
        const idencargado = cboEncargado.value;
        if(idencargado != '') {                    
            cboContrato.disabled = false;
            datosEncargado = await obtenerEncargado(idencargado);
        }
    });

    //Asignar evento change a plantilla   
    $('#cbo_contrato').change(function() {
        const idcontrato = cboContrato.value;
        if(idcontrato != '') {            
            llenarVistaPrevia(idcontrato);
            btnActualizar.style.display = 'block';                        
        }
    });
    
    const llenarFormulario = async(id) => {
        try {
            const res = await fetch(`/actividades/generar_contrato/obtener_reserva_id/${id}`);
            const data = await res.json();             
            datosReserva = data;           
            const {nombres, apellidos, cedula, fechahoy} = data;
            txt_solicitante.value = `${nombres} ${apellidos} - CI: ${cedula}`;
            txt_fecha.value = fechahoy;
        } catch (error) {
            console.error(error);
        }
    }

    const llenarVistaPrevia = async(id) => {
        try {
            const res = await fetch(`/actividades/generar_contrato/obtener_plantilla_id/${id}`);
            const data = await res.json();        
            textoPlantilla = data[4];
            txt_contrato.innerHTML = formatearContrato(datosEncargado, datosReserva, textoPlantilla);                                          
        } catch (error) {
            console.error(error);
        }
    }

    const obtenerEncargado = async(id) => {
        try {
            const res = await fetch(`/actividades/generar_contrato/obtener_encargado_id/${id}`);
            const data = await res.json();        
            return data;                                        
        } catch (error) {
            console.error(error);
        }
    }

    const formatearContrato = (datosE, datos, plantilla) => {
        console.log(datosE);
        console.log(datos);
        //console.log(plantilla);
        const {nombres, apellidos, cedula, nrocasa, direccion} = datos;                
        plantilla = plantilla.replace(/{COMODANTE}/g, `${nombres} ${apellidos}`);
        plantilla = plantilla.replace(/{CEDULA_CTE}/g, `${cedula}`);
        plantilla = plantilla.replace(/{NROCASA_CTE}/g, `${nrocasa}`);
        plantilla = plantilla.replace(/{DIRECCION_CTE}/g, `${direccion}`);
        plantilla = plantilla.replace(/{COMODATARIO}/g, `${datosE.nombres} ${datosE.apellidos}`);
        plantilla = plantilla.replace(/{CEDULA_CIO}/g, `${datosE.cedula}`);
        plantilla = plantilla.replace(/{NROCASA_CIO}/g, `${datosE.nrocasa}`);
        plantilla = plantilla.replace(/{DIRECCION_CIO}/g, `${datosE.nrocasa}`);
        return plantilla;
    }

    
});