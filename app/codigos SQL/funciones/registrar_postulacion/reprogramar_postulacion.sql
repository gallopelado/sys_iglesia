CREATE OR REPLACE FUNCTION membresia.reprogramar_postulacion(opcion varchar, idpostulacion integer, fechainicio date, fechafin date)
RETURNS boolean AS
$$
/**
* Procedimiento: reprogramar_postulacion
* Parametros: opcion varchar, fechainicio date, fechafin
* Descripcion: Se definen ajustes con la fecha de inicio y fin
* pensado para extender el tiempo de finalizacion.
* Por 1 dia o 1 semana o 1 mes.
* Autor: Juan Jose Gonzalez Ramirez <juanftp100@gmail.com>
* Version: 1.0
* Fecha: 07-09-2019
*/
DECLARE
	v_op varchar := opcion;
	v_idpostulacion integer := idpostulacion;
	v_fechainicio date := fechainicio;
	v_fechafin date := fechafin;

	f_valido boolean := membresia.verifica_estado_postulacion(v_idpostulacion);
BEGIN
	
	-- Verificar estado del registro.
	IF f_valido IS NOT TRUE THEN
		RETURN FALSE;
	END IF;
	
	CASE v_op
		-- Agregar 1 dia a la fecha final.
		WHEN 'dia' THEN
			v_fechafin := date( v_fechafin::timestamp + '1 day' );
		
	-- Agregar 1 semana a la fecha final.
		WHEN 'semana' THEN
			v_fechafin := date( v_fechafin::timestamp + '1 week' );
		
	-- Agregar 1 mes a la fecha final.
		WHEN 'mes' THEN
			v_fechafin := date( v_fechafin::timestamp + '1 month' );
		
		WHEN 'personalizado' THEN
			v_fechafin := v_fechafin;
		
		ELSE
			RAISE info 'Ninguna opcion es correcta.(dia -- semana -- mes -- personalizado)';
			RETURN FALSE;
	END CASE;

	-- Hacer update.
	UPDATE membresia.cabe_postulacion 
	SET post_iniciopostu = v_fechainicio, post_finpostu = v_fechafin
	WHERE post_id = v_idpostulacion;

	RAISE info 'Se actualizo correctamente la postulacion'; 
	RETURN TRUE;

END

$$ LANGUAGE plpgsql;