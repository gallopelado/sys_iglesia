from app.Conexion.Conexion import Conexion

class Contrato:

    def obtenerContratos(self, ):
        selectSQL = '''SELECT con_id, tcon_des, con_titulo, 
        con_estado, creacion_por_usuario, creacion_fecha, modificado_por_usuario, modif_fecha
        FROM referenciales.contrato
        LEFT JOIN referenciales.tipo_contrato USING(tcon_id)
        '''        
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(selectSQL)
            return cur.fetchall()            
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()


    def obtenerContratosId(self, id):
        selectSQL = '''SELECT con_id, tcon_id, con_titulo, con_plantilla, 
        con_estado, creacion_por_usuario, creacion_fecha, modificado_por_usuario, modif_fecha
        FROM referenciales.contrato where con_id = %s;
        '''        
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(selectSQL, (id,))
            return cur.fetchone()            
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

    
    def guardar(self, titulo, tipo, plantilla):
        insertSQL = '''INSERT INTO referenciales.contrato
        (tcon_id, con_titulo, con_plantilla, con_estado, creacion_por_usuario, creacion_fecha)
        VALUES(%s, UPPER(%s), %s, true, null, now());'''
        parametros = (tipo, titulo, plantilla,)
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(insertSQL, parametros)
            con.commit()
            return True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()


    def modificar(self, id, titulo, tipo, plantilla):
        updateSQL = '''UPDATE referenciales.contrato
        SET con_titulo=%s, tcon_id=%s, con_plantilla=%s, con_estado=true, modificado_por_usuario=null, modif_fecha=now()
        WHERE con_id=%s;
        '''
        parametros = (titulo, tipo, plantilla, id)
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(updateSQL, parametros)
            con.commit()
            return True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()

            
    def eliminar(self, id):
        deleteSQL = '''DELETE FROM referenciales.contrato WHERE con_id=%s;
        '''        
        try:
            conexion = Conexion()
            con = conexion.getConexion()
            cur = con.cursor()
            cur.execute(deleteSQL, (id,))
            con.commit()
            return True
        except con.Error as e:
            print(e.pgerror)
        finally:
            if con is not None:
                cur.close()
                con.close()