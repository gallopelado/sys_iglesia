CREATE OR REPLACE FUNCTION membresia.verifica_fechas_postulacion(fechainicio date, fechafin date)
RETURNS boolean AS
$$
/**
 * Función: verifica_fechas_postulacion.
 * Descripcion: Valida fecha de inicio y fecha fin en base a:
 * -- La fecha de inicio,fin NO debe ser menor a la actual.(CONTEXTO INSERT) 
 * --# {fechainicio, fechafin} > fechaactual
 * -- La fecha fin NO debe ser menor ni igual a la fecha inicio. (CONTEXTO INSERT/UPDATE)
 * --# fechafin > fechainicio
 * Paramétros: fechainicio date, fechafin date
 * Version: 1.0
 * Autor: Juan José González Ramírez <juanftp100@gmail.com>
 */
DECLARE
	v_fechaactual date := current_date;
	v_fechainicio date := '2019-09-06';
	v_fechafin date := '2019-10-06';

BEGIN

	IF v_fechainicio < v_fechaactual THEN

		RAISE EXCEPTION 'Fechainicio desactualizada';

	ELSEIF v_fechainicio >= v_fechafin THEN
	
		RAISE EXCEPTION 'FechaInicio es mayor o igual que la fecha fin';
	
	ELSEIF v_fechafin < v_fechaactual THEN
	
		RAISE EXCEPTION 'Fechafin desactualizada';
	
	ELSEIF v_fechafin <= v_fechainicio THEN
	
		RAISE EXCEPTION 'Fechafin es menor o igual a la fecha de inicio';		
	
	END IF;
	
	RAISE NOTICE '************************************';
	RAISE NOTICE 'Fechas configuradas correctamente!!!';
	RAISE NOTICE 'FechaInicio= % y FechaFin= %', v_fechainicio, v_fechafin;
	
	RETURN TRUE;
END

$$ LANGUAGE plpgsql;

