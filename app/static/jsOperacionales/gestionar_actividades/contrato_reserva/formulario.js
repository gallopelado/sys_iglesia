document.addEventListener('DOMContentLoaded', () => {
    $('select').select2();
    const cboReserva = document.getElementById('cbo_reserva');
    const cboEncargado = document.getElementById('cbo_encargado');
    
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
        } catch (error) {
            console.error(error);
        }
    }
});