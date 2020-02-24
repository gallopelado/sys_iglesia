/**
 * Archivo encargado de controlar el index
 * 
 */
import { idioma_spanish, mensajeConfirmacion } from '../../helper/helper.js';
document.addEventListener('DOMContentLoaded', ()=>{ 
    //traer combo, tbody
    /* const cb = document.getElementById('cbm_estado');
    const tb = document.getElementById('tb');   
    const cargaTabla = async(estado='NO-ATENDIDO') => {
        try {
            const res = await fetch(`/actividades/solicitud_hospital/get_solicitudes_json/${estado}`);
            const botonVer = (idsolicitud) => `<button type="button" class="btn btn-secondary btn-sm" onclick="ver(${idsolicitud})">Ver</button>`;
            const botonModificar = (idsolicitud) => `<button type="button" class="btn btn-primary btn-sm" onclick="modificar(${idsolicitud})">Modificar</button>`;
            const botonEliminar = (idsolicitud) => `<button type="button" class="btn btn-danger btn-sm" onclick="eliminar(${idsolicitud})">Eliminar</button>`;
            const data = await res.json();                        
            let cadena = '';
            if (data != null || data != undefined) {
                for (let item of data) {
                    cadena += `<tr id="${item.idsolicitud}">
                    <td>${item.descripcion}</td>
                    <td>${item.nombres} ${item.apellidos}</td>
                    <td>${item.estado}</td>
                    <td>
                        ${botonVer(item.idsolicitud)} ${botonModificar(item.idsolicitud)} ${botonEliminar(item.idsolicitud)}
                    </td>
                    </tr>`;
                }
                tb.innerHTML = cadena;
            }
        } catch (error) {
            console.error(error);
        }
    }

    //Capturar evento change
    cb.addEventListener('change', () => {
        tb.innerHTML = '';
        cargaTabla(cb.value);
    });
    //Inicio
    cargaTabla();

    window.modificar = (id) => {                
        const m = mensajeConfirmacion('Confirmar', 'Desea modificar?');
        m.buttons.Si.action = () => {                
            location.href = `/actividades/solicitud_hospital/form_visita/${id}`;
        }
        m.open();
    }

    window.eliminar = (id) => {                
        const m = mensajeConfirmacion('Confirmar', 'Desea cancelar?');
        m.buttons.Si.action = () => {                
            location.href = `/actividades/solicitud_hospital/cancelar/${id}`;
        }
        m.open();
    }

    window.ver = (id) => {                    
        location.href = `/actividades/solicitud_hospital/ver_formulario/${id}`;
    } */
});

var app = new Vue({
    el:'#app'
    , data: {
        solicitudes:[]
    }
    , methods: {
        obtenerSolicitudes: async function () {
            try {
                const res = await axios.get('/actividades/consejeria/get_solicitudes');
                this.solicitudes = await res.data;
            } catch (error) {
                console.error(error);
            }
        }
        , modificar: function (id) {
            const m = mensajeConfirmacion('Confirmar', 'Desea modificar?');
            m.buttons.Si.action = () => {                
                location.href = `/actividades/consejeria/editar_solicitud/${id}`;
            }
            m.open();
        }
        , ver: function (id) {            
            location.href = `/actividades/consejeria/ver_solicitud/${id}`;
        }
        , cancelar: function (id) {
            const m = mensajeConfirmacion('Confirmar', 'Desea cancelar?');
            m.buttons.Si.action = () => {                
                location.href = `/actividades/consejeria/cancela_solicitud/${id}`;
            }
            m.open();
        }
    }
    , beforeMount() {
        this.obtenerSolicitudes();
    }
    , delimiters: ['[[',']]']
})