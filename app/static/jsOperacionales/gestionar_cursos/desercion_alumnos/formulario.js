/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */

new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    data:{
        malla_id: null,
        cur_id: null,
        per_id: null,
        curso: null,
        alumno: null,
        motivo_desercion: null,
        descripcion: null,
        lista_motivo_desercion: [],
        alumnoSeleccionado: null
    }
})