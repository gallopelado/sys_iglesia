 
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
create type estado_reserva as enum('CONFIRMADO', 'NO-CONFIRMADO', 'CANCELADO', 'DESACTIVADO');
create type estado_solicitud_hospital as enum('ATENDIDO', 'NO-ATENDIDO', 'CANCELADO');
create type turno as enum('MAÑANA', 'TARDE', 'NOCHE');
create type public.dia as enum('LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES', 'SABADO', 'DOMINGO');
