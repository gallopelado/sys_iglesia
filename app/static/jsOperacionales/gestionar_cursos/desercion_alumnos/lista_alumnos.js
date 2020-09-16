/**
 * Es es el fichero controlador del formulario
 * @author Juan Jose Gonzalez Ramírez
 * 
 */

new Vue({
    el:'#app',
    delimiters: ['[[', ']]'],
    data: {
        curso: null,
        lista_alumnos: [],
        desercion_data: JSON.parse(sessionStorage.getItem('desercion_data'))
    },
    methods: {
        cargarCabecera() {
            this.curso = this.desercion_data.curso;
        },

        cargarListaAlumnos() {
            const { cur_id } = this.desercion_data;
            axios.get(`/cursos/desercion_alumnos/get_cursos_inscriptos/${cur_id}`).then(({ data }) => this.lista_alumnos = data)
        },

        escogerAlumno(item) {
            $.confirm({
                title: 'Mensaje de confirmación!',
                content: 'Desear registrar deserción para este alumno?',
                buttons: {
                    Confirmar: {
                        text: 'Confirmar',
                        btnClass: 'btn-blue',
                        keys: ['enter', 'a'],
                        action: function() {
                            if(item){
                                sessionStorage.setItem('alumno_seleccionado', JSON.stringify(item));
                                location.href = `/cursos/desercion_alumnos/formulario_desercion`;
                            }
                        }
                    },
                    Cancelar: function () {
                    }
                }
            });
        }
    },
    mounted() {
        this.cargarCabecera();
        this.cargarListaAlumnos();
    },
})