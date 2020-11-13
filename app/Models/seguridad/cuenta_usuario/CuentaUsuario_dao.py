from app.Conexion.Conexion import Conexion

class CuentaUsuario_dao:

    def getUserData(self, usu_id):
        obj = {}
        querySQL = '''SELECT 
            u.usu_nick, u.usu_imagen,CONCAT(p.per_nombres, ' ', p.per_apellidos)nombres, c.car_des cargo, g.gru_des grupo
            , CASE WHEN (SELECT COUNT(adp_id) from membresia.admision_persona WHERE adp_id=p.per_id)=1 THEN 'ES MIEMBRO' ELSE 'NO ES MIEMBRO' END estado
            , CONCAT(fecha_formatolargo(u.modificacion_fecha::DATE), ' a las ', u.modificacion_fecha::TIME(0))ultima_vez
        FROM seguridad.usuarios u
        LEFT JOIN seguridad.funcionarios f ON f.fun_id = u.fun_id
        LEFT JOIN referenciales.personas p ON p.per_id = f.fun_id
        LEFT JOIN seguridad.grupos g ON g.gru_id = u.gru_id
        LEFT JOIN seguridad.cargos c ON c.car_id = f.car_id WHERE u.usu_id=%s
        '''
        conexion = Conexion()
        conn = conexion.getConexion()
        cur = conn.cursor()
        try:
            cur.execute(querySQL, (usu_id,))
            rs = cur.fetchone()
            obj['usu_nick'] = rs[0]
            obj['usu_imagen'] = rs[1]
            obj['nombres'] = rs[2]
            obj['cargo'] = rs[3]
            obj['grupo'] = rs[4]
            obj['estado'] = rs[5]
            obj['ultima_vez'] = rs[6]
        except conn.Error as e:
            obj = {}
            obj['codigo'] = e.pgcode
            obj['mensaje'] = e.pgerror
        finally:
            if conn is not None:
                cur.close()
                conn.close()
        return obj