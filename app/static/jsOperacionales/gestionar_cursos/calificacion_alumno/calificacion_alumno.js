$(function() {
    window.modalPuntaje = (alumno_id) => {
        const planex_id = $('#cbo_examen').val();
        if(!planex_id) {
            alert('Debe escoger un examen!');
            $('#cbo_examen').focus();
            return;
        }
        $('#modal_calificacion').modal('show');
        $('#btn_cargarpuntaje').click(function() {
            const puntaje = $('#txt_puntos').val();
            if(!puntaje) {
                alert('No debe dejar vacio el puntaje');
                return;
            }
            if(puntaje < 0) {
                alert('No debe ser valor negativo');
                return;
            }
            if(puntaje > 100) {
                alert('No debe ser valor tan grande');
                return;
            }
            axios.post(`/cursos/calificacion_examen/guardar`, {
                planex_id: parseInt(planex_id), alumno_id: parseInt(alumno_id), cal_puntaje: parseInt(puntaje)
            }).then(({data}) => {
                if(data.estado !== 'error') {
                    $.confirm({
                        title: data.estado,
                        content: data.mensaje,
                        buttons: {
                            confirm: function () {
                                location.reload();
                            }
                        }
                    });
                } else {
                    location.reload();
                }
            })
        })
    }

    $('#formulario').submit(function(e) {
        const planex_id = $('#cbo_examen').val();
        if(!planex_id) {
            alert('Debe escoger un examen!');
            $('#cbo_examen').focus();
            return false;
        }
        if(!confirm('Estas a punto de anular un todas las calificaciones de una asignatura! Estas seguro?')) {
            return false;
        }
    })
});