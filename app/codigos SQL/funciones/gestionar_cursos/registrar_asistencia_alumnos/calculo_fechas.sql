CREATE OR REPLACE FUNCTION cursos.calcula_fechas_segun_dias(fechainicio date, fechafin date, dias json)
RETURNS TABLE(v_dia varchar, v_fecha date) AS
$$
/**
 * Procedimiento: calcula_fechas_segun_dias
 * Autor: Juan José González Ramírez
 * Fecha creación: 2020-07-19
 * Parametros: fechainicio date, fechafin date, dias json 
 * Descripción: Segun las fechas ingresadas, se calcula un rango de fechas teniendo en cuenta
 * los dias de la semana ingresados.
 * El formato para los dias es en formato JSON, se muestra ejemplo:
 * '{"DOMINGO":false, "LUNES":false, "MARTES":false, "MIERCOLES":false, "JUEVES":false, "VIERNES":false, "SABADO":false}'
 * 
 */
DECLARE
	fechas date[];
	tamanho integer;
	i integer;
	resultado json;
	lista_fechas json[];
BEGIN
	drop table if exists data_fecha;
	create temp table data_fecha(v_dia varchar, v_fecha date);

	SELECT array_agg(data) INTO fechas FROM (select fechainicio+dia from generate_series(1, fechafin - fechainicio) dia)data;
	
	for i in 1..array_upper(fechas,1)
	loop
		if to_char(fechas[i], 'd') = '1' AND (dias->>'DOMINGO' = 'true') then
			INSERT INTO data_fecha values('DOMINGO', fechas[i]);
			raise notice 'DOMINGO %', fechas[i];
		elsif to_char(fechas[i], 'd') = '2' AND (dias->>'LUNES' = 'true') then
			INSERT INTO data_fecha values('LUNES', fechas[i]);
			raise notice 'LUNES %', fechas[i];
		elsif to_char(fechas[i], 'd') = '3' AND (dias->>'MARTES' = 'true') then
			INSERT INTO data_fecha values('MARTES', fechas[i]);
			raise notice 'MARTES %', fechas[i];
		elsif to_char(fechas[i], 'd') = '4' AND (dias->>'MIERCOLES' = 'true') then
			INSERT INTO data_fecha values('MIERCOLES', fechas[i]);
			raise notice 'MIERCOLES %', fechas[i];
		elsif to_char(fechas[i], 'd') = '5' AND (dias->>'JUEVES' = 'true') then
			INSERT INTO data_fecha values('JUEVES', fechas[i]);
			raise notice 'JUEVES %', fechas[i];
		elsif to_char(fechas[i], 'd') = '6' AND (dias->>'VIERNES' = 'true') then
			INSERT INTO data_fecha values('VIERNES', fechas[i]);
			raise notice 'VIERNES %', fechas[i];
		elsif to_char(fechas[i], 'd') = '7' AND (dias->>'SABADO' = 'true') then
			INSERT INTO data_fecha values('SABADO', fechas[i]);
			raise notice 'SABADO %', fechas[i];
		end if;
	end loop;
	return query SELECT * FROM data_fecha ORDER BY v_dia;
END;
$$ LANGUAGE plpgsql;

--Como probar
SELECT * FROM cursos.calcula_fechas_segun_dias(
	'2020-06-01', 
	'2020-07-31', 
	'{"DOMINGO":false, "LUNES":false, "MARTES":false, "MIERCOLES":false, "JUEVES":false, "VIERNES":true, "SABADO":true}'
) ORDER BY v_fecha DESC; 


