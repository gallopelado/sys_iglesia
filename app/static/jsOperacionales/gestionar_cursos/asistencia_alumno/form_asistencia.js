/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */
var app = new Vue({
    el:'#app'
    , data: {
        asistencia_data: JSON.parse(sessionStorage.getItem('asistencia_data'))
        , materia: null
        , curso: null
        , turno: null
        , descripcion: null
        , det_alumnos: null
        , fecha_clase: null
    }
    , mounted() {
        this.materia =  `${this.asistencia_data.asi_des} ${this.asistencia_data.num_des}`;
        this.curso =  this.asistencia_data.cur_des
        this.turno =  this.asistencia_data.turno
        this.fecha_clase = this.asistencia_data.fecha_larga
    }
    , delimiters: ['[[', ']]']
});