document.addEventListener('DOMContentLoaded', () => {
    $('select').select2();
    const cboReserva = document.getElementById('cbo_reserva');
    const cboEncargado = document.getElementById('cbo_encargado');
    const txt_solicitante = document.getElementById('txt_solicitante');
    const txt_fecha = document.getElementById('txt_fecha');
    
    //Asignar evento change a reserva   
    $('#cbo_reserva').change(function() {
        const idreserva = cboReserva.value;
        if(idreserva != '') {            
            llenarFormulario(idreserva);
        }
    });

    const llenarFormulario = async(id) => {
        try {
            const res = await fetch(`/actividades/generar_contrato/obtener_reserva_id/${id}`);
            const data = await res.json();
            console.log(data);
            const {nombres, apellidos, cedula, fechahoy} = data;
            txt_solicitante.value = `${nombres} ${apellidos} - CI: ${cedula}`;
            txt_fecha.value = fechahoy;
        } catch (error) {
            console.error(error);
        }
    }
});