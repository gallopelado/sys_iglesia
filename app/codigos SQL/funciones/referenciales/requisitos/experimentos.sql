
-- PARA JUGAR, crea una tabla ciudades e inserta datos.
CREATE TABLE ciudades(ciu_id serial PRIMARY KEY, ciu_des varchar(100) NOT NULL UNIQUE);
INSERT INTO ciudades VALUES('ASUNCION'), ('FERNANDO DE LA MORA');
--CREATE TYPE anon as (ciu_id integer, ciu_des varchar); --DROP TYPE anon

--PROBAR EN DURO
/*SELECT * FROM json_populate_recordset(null::anon, '[{
    "ciu_id": 5,
    "ciu_des": "VILLA ELISA"
},{
    "ciu_id": 8,
    "ciu_des": "MISIONES"
}]');*/

CREATE OR REPLACE FUNCTION public.sp_experimento_json() 
RETURNS SETOF anon AS 
$$
DECLARE	
	datos json;
	texto record;
BEGIN
	/*	Convertis a un arry de objetos lo que trae el referencial
	*	ciudades, por comodidad hice esto. Pero también podes definir
	*	como un parametro arriba.
	*	Guardas en la variable datos de tipo json.
	*/
	SELECT ARRAY_TO_JSON(ARRAY_AGG(ROW_TO_JSON(data))) INTO datos
	FROM (SELECT * FROM referenciales.ciudades)data;
	RAISE NOTICE '%', datos;
	
	/* Aquí empezas a recorrer lo que cargaste en datos, ojo que esta en
	*	formato json, aquí es cuando ocurre la magia, deconvertís el objeto
	*	json a un tipo record. Por supuesto, se almacena en la variable texto.
	*	Luego recorres, el tipo anon es un TYPE, te paso el codigo:
	*	CREATE TYPE anon as (ciu_id integer, ciu_des varchar)
	*	OJO, EL MISMO NOMBRE DEL ATRIBUTO DE TU TABLA DEBES DE PONER.
	*	Luego traes datos que cargaste arriba. Como es un conjunto de filas lo
	*	que tiene datos, vas a usar RETURN NEXT, cuando es una sola fila se usa RETURN solo.
	*	Autor: Juan José González Ramírez											   
	*/
	FOR texto IN SELECT * FROM json_populate_recordset(null::anon, datos)
	LOOP											   	
		RETURN NEXT texto;
	END LOOP;											   
END;
$$ LANGUAGE plpgsql;

-- Retorna tupla											   
SELECT public.sp_experimento_json();
											   
-- Retorna como tabla
SELECT * FROM public.sp_experimento_json();											   