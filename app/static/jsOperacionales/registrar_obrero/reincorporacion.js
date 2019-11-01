document.addEventListener('DOMContentLoaded', () => {
    window.reincorporar = (idcomite, idobrero) => {
        $('#modal_reincorporacion').modal();
        const btProceder = document.getElementById('btnProceder');
        btProceder.addEventListener('click', () => {
            let txtmotivo = document.getElementById('txtobs');
            txtmotivo = txtmotivo.value.trim();
            txtmotivo = txtmotivo.replace(/\\n/g, '');
            if (txtmotivo === '') {
                alert('El motivo no puede estar vacio!');
                document.getElementById('txtobs').focus();
            } else {
                reincorporaObrero(idcomite,idobrero,txtmotivo);
            }
        });
    }

    const reincorporaObrero = async(idcomite, idobrero, motivo) => {
        try {
            const res = await fetch('/membresia/registrar_obrero/reincorporar_obrero', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({idcomite:idcomite, idobrero:idobrero, motivo:motivo})
            });
            const data = await res.json();
            if (data.estado === true) {
                location.href = `/membresia/registrar_obrero/formulario_obrero/${idcomite}`;
            } else {
                alert('Hubo un error. Favor contacte con el administrador');
                console.error(data);
            }
        } catch (error) {
            alert('Hubo un problema. Favor contacte con el Administrador del Sistema');
            console.error(error);
        }
    }
});