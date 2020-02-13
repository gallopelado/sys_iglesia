document.addEventListener('DOMContentLoaded', () => {
    $('select').select2();
    const solicitud = document.getElementById('solicitudes');
    const diasdisp = document.getElementById('dias');
    const horavisi = document.getElementById('horario');
    const comite = document.getElementById('idcomite');
    const voluntario = document.getElementById('idvoluntario');

    $('#solicitudes').change(async function() {
        const idsolicitud = solicitud.value;
        if (idsolicitud != '') {
            const {horavisi, lunes, martes, miercoles, jueves, viernes, sabado, domingo} = await solicitudId(idsolicitud);
            let dias =  `${lunes ? 'Lunes,':''}${martes ? 'Martes,':''}${miercoles ? 'Miercoles,':''}
            ${jueves ? 'Jueves,':''}${viernes ? 'Viernes,':''}${sabado ? 'Sabado,':''}
            ${domingo ? 'Domingo,':''} `;
            $('#dias').val(`${dias.replace(/\s/g,'')}`);
            $('#horario').val(horavisi);
        }
    });
    
    const solicitudId = async(id) => {
        try {
            const res = await fetch(`/actividades/solicitud_hospital/get_solicitudes_json_id/${id}`);
            const data = await res.json();
            console.log(data);
            return data;
        } catch (error) {
            console.log(error);
        }
    }

});