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

    $('#idcomite').change(async function() {
        const idcomite = comite.value;
        let cadena = '<option value="">...</option>';
        if (idcomite != '') {
            const datos = await integrantesComite(idcomite);
            console.log(datos);
            if (datos != null || datos != undefined) {
                for(let voluntario of datos) {
                    const { idcomite, comite, idpersona, nombres, apellidos } = voluntario;
                    //console.log(voluntario);
                    cadena += `<option value="${idpersona}">${nombres} ${apellidos}</option>`;
                }
                voluntario.disabled = false;                
                voluntario.innerHTML = cadena;
                $('#registrar').prop('disabled', false);
            } else {
                voluntario.innerHTML = '';
                voluntario.disabled = true;
                $('#registrar').prop('disabled', true);
            }
        }
    });
    
    const solicitudId = async(id) => {
        try {
            const res = await fetch(`/actividades/solicitud_hospital/get_solicitudes_json_id/${id}`);
            const data = await res.json();            
            return data;
        } catch (error) {
            console.log(error);
        }
    }

    const integrantesComite = async(id) => {
        try {
            const res = await fetch(`/actividades/solicitud_hospital/get_integrantes_comite/${id}`);
            const data = await res.json();            
            return data;
        } catch (error) {
            console.log(error);
        }
    }

});