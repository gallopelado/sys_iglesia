export default class Documento {

    constructor(binario) {
               
        this.binario = binario;
        
    }

    /**
     * validarDocumento
     * 
     * Permite validar el documento o binario.
     * La extension usa este formato
     * ['PDF', 'EPUB']
     * Peso recomendado: 30720 es 30MB
     * 
     * @param {Array} extensiones_permitidas 
     * @param {int} peso_permitido 
     */
    validarDocumento(extensiones_permitidas, peso_permitido) {
        
        const extensiones = extensiones_permitidas;
        const peso = peso_permitido;
        const longitud_extension = extensiones.length;
        let extensionFile;
        let tamadocu;
        let nopermitida = true;

        // Si no es undefined
        if ( typeof(this.binario) !== 'undefined' ) {

            // Get extension.
            if ( this.binario.type === '' ) {
                alert('No se permiten archivos sin extension PDF o EPUB.');
                return;
            }
            extensionFile = this.binario.type.split('/')[1];
            
            extensionFile = extensionFile.toUpperCase();

            // Tamaño del documento
            tamadocu = Math.round(this.binario.size / 1024);

            if ( tamadocu <= peso ) {

                // Recorre en busca de extensiones correctas.
                for (let i = 0; i <= longitud_extension; i++) {

                    if (extensionFile === extensiones_permitidas[i]) {

                        nopermitida = true;                        
                        return this.binario;
                        
                    }                     

                }

                if (nopermitida) {
                    alert('Solo se admiten documentos en PDF o EPUB');
                    return false;
                }

            } else {
                alert('Solo se admiten hasta 30 MB');
                return false;
            }

        } else {

            // Cuando no se subio ningun documento.
            console.log('No se cargo ningun documento');
            return false;
        }

    }

    /**
     * getDocumento
     * 
     * Retorna el binario de archivo.
     * (Recuerda inicializar correctamente con .files[0] en el constructor)
     */
    getDocumento() {

        return this.binario;

    }

    /**
     * getNombreDocumento
     * 
     * Retorna el nombre de archivo.
     * (Recuerda inicializar correctamente con .files[0] en el constructor)
     */
    getNombreDocumento() {

        return this.binario.name;

    }

}