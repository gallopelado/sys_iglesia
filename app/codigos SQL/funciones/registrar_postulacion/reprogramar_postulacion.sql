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
	v_bandera boolean := FALSE;
BEGIN
	
	-- Verificar estado del registro.
	IF f_valido IS NOT TRUE THEN
		RETURN FALSE;
	END IF;
	
	-- En caso de no personalizado, se recibe la opcion nada más.
	IF v_op != 'personalizado' AND v_fechainicio IS NULL AND v_fechafin IS NULL THEN
		
		v_bandera := TRUE;
		-- Obtener las fechas segun idpostulacion
		SELECT post_iniciopostu, post_finpostu 
		INTO v_fechainicio, v_fechafin
		FROM membresia.cabe_postulacion WHERE post_id = v_idpostulacion;
	
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


	IF v_bandera = TRUE THEN
		-- Hacer update.
		UPDATE membresia.cabe_postulacion 
		SET post_iniciopostu = v_fechainicio, post_finpostu = v_fechafin
		WHERE post_id = v_idpostulacion;
			
		RETURN TRUE;	
	
	ELSE
		
		UPDATE membresia.cabe_postulacion 
		SET post_iniciopostu = v_fechainicio, post_finpostu = v_fechafin
		WHERE post_id = v_idpostulacion;
			 
		RETURN TRUE;	
	
	END IF;	

END

$$ LANGUAGE plpgsql;