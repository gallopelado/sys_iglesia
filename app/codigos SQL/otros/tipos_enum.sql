 
create type razonbaja as enum('DISCIPLINA', 'DEFUNCION', 'EXCOMUNION', 'TRASLADO', 'OTRAS');
create type sexo as enum('MASCULINO', 'FEMENINO');
create type estadocivil as enum('SOLTERO/A', 'CASADO/A', 'CONCUBINATO');
create type tipotel as enum('CASA', 'PERSONAL','TRABAJO', 'FAX', 'OTROS');
CREATE TYPE estado_membresia AS ENUM(
'ACTIVO, CON CARGOS',
'ACTIVO, SIN CARGOS',
'INACTIVO',
'A PRUEBA',
'DADO DE BAJA',
'EN OBSERVACION'
);
