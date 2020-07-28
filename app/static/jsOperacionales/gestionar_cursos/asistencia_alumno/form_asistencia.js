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
    }
    , mounted() {
        this.materia =  this.asistencia_data.asi_des
        this.curso =  this.asistencia_data.cur_des
        this.turno =  this.asistencia_data.turno
    }
    , delimiters: ['[[', ']]']
});