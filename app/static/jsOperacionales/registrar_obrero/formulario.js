document.addEventListener('DOMContentLoaded', () => {
    window.modificar = (idcomite, idobrero) => {
        if (confirm('Desea editar este registro ?')) {
            location.href = `/membresia/registrar_obrero/editar_obrero/${idcomite}/${idobrero}`;
        }
    }

    window.baja = (idcomite, idobrero) => {
        if (confirm('Desea dar de baja este registro ?')) {            
            $('#modal_baja').modal();
            document.getElementById('btnProceder').addEventListener('click', () => {
                const txtobs = document.getElementById('txtobs');
                let observacion = txtobs.value.trim();
                observacion = observacion.replace(/\\n/g, '');
                if (observacion === '') {
                    alert('No debe estar vacía la descripción');
                    txtobs.focus();
                } else {
                    bajaObrero(idcomite,idobrero,observacion);
                }
            });
        }
    }

    const bajaObrero = async(idcomite, idobrero, observacion) => {
        try {
            const res = await fetch('/membresia/registrar_obrero/baja_obrero', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({idcomite: idcomite, idobrero: idobrero, observacion:observacion})
            });
            const data = await res.json();
            if (data.estado === true) {
                location.href = `/membresia/registrar_obrero/formulario_obrero/${idcomite}`;
            } else {
                alert('Hubo un error al intentar dar de baja. Favor contacte con el administrador');
                console.error(data);
            }
        } catch (error) {
            alert('Hubo un error al intentar dar de baja. Favor contacte con el administrador');
            console.error(error);
        }
    }
});