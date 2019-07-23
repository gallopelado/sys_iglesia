import { autoCompletar, hacerDataTable } from '../helper/helper.js'

export default class FormularioMiembroRequisito {    

    constructor() {

        this.idmiembro = document.getElementById('idmiembro');
        this.txt_miembro = document.getElementById('txt_miembro');
        this.txt_idrequisito = document.getElementById('txt_idrequisito');
        this.txt_requisito = document.getElementById('txt_requisito');
        this.txt_obs = document.getElementById('txt_obs');
        this.btnAgregaItem = document.getElementById('btnAgregaItem');        

    }

    async obtenerRequisitos() {

        try {
            
            const res = await fetch('/requisitos_miembro/lista_requisitos');
            const data = await res.json();
            
            if(data)
                return data;
                
            return false;
                        
        } catch (error) {
            console.error(error.message);
        }

    }    

    async cargarInputs() {
        
        const requisitos = await this.obtenerRequisitos();
                
        autoCompletar(requisitos, 'descripcion', 'id', 'txt_idrequisito', 'txt_requisito');

    }

    validarFormulario() {
        
        let datos = {};
        let idmiembro = this.idmiembro.value;
        let txt_miembro = this.txt_miembro.value;
        let txt_idrequisito = this.txt_idrequisito.value;
        let txt_requisito = this.txt_requisito.value;
        let txt_obs = this.txt_obs.value;

        if (idmiembro !== "" && txt_miembro !=="" && txt_idrequisito !== "" && txt_requisito !== "") {

            datos.idmiembro = idmiembro;
            datos.txt_miembro = txt_miembro.trim();
            datos.txt_idrequisito = txt_idrequisito;
            datos.txt_requisito = txt_requisito.trim();
            datos.txt_obs = txt_obs.trim();

            return datos;

        }

        alert('Complete correctamente el formulario.');
        return false;

    }

    guardar() {

        const tabla = document.getElementById('tb_requisitos');
        //console.log(tabla.rows);
        const tablaLongi = tabla.rows.length;
        //console.log(tablaLongi);
        let nuevosRequisitos = [];

        for (let i = 0; i <= tablaLongi-1; i++) {

            //console.log(tabla.rows[i].style.backgroundColor);
            const estiloTR = tabla.rows[i].style.backgroundColor;
            if (estiloTR !== 'rgb(241, 243, 232)') {

                // los que no tienen estilo son nuevos.
                console.log(tabla.rows[i].id);

                const idpersona = this.idmiembro.value;
                const idfila = tabla.rows[i].id;
                const obs = tabla.rows[i].children[1].innerHTML;
                nuevosRequisitos.push({
                    idpersona: idpersona,
                    idrequisito: idfila,
                    obs: obs
                });
                
            }

        }
        console.log(nuevosRequisitos);

    }
}