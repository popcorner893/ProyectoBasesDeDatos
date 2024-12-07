import pymysql

class MiConexion:
    def __init__(self):
        self.conexion = pymysql.connect(host='localhost', user='root', passwd='', db='basededatosprof1')

    def busca_user_Aspirante(self, users):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT * FROM usuarioaspirante WHERE usuario = %s"
            cur.execute(sql, (users,))
            usersx = cur.fetchall()
            return usersx
        finally:
            cur.close()

    def busca_password_Aspirante(self, password):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT * FROM usuarioaspirante WHERE password = %s"
            cur.execute(sql, (password,))
            passwordx = cur.fetchall()
            return passwordx
        finally:
            cur.close()

    def busca_user_Empleado(self, users):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT * FROM usuarioempleado WHERE usuario = %s"
            cur.execute(sql, (users,))
            usersx = cur.fetchall()
            return usersx
        finally:
            cur.close()

    def busca_password_Empleado(self, password):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT * FROM usuarioempleado WHERE password = %s"
            cur.execute(sql, (password,))
            passwordx = cur.fetchall()
            return passwordx
        finally:
            cur.close()

    # Obtiene el nombre  de un aspirante completo usando el username  Ejemplo(Alejandro Castro R) 
    def get_full_name_aspirante(self, username):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT CONCAT_WS(' ', aspirante.nombre, aspirante.apellido1, SUBSTR(aspirante.apellido2, 1, 1)) 
                    FROM aspirante INNER JOIN usuarioaspirante ON aspirante.idAspirante = usuarioaspirante.idUsuarioAspirante 
                    WHERE usuario = %s"""
            cur.execute(sql, (username,))
            return cur.fetchall()[0][0]
            miConexion.close()
        except:
            return "Sin nombre"
        finally:
                cur.close()

     # Obtiene el nombre de un empleado completo usando el username  Ejemplo(Alejandro Castro R) 
    def get_full_name_empleado(self, username):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT CONCAT_WS(' ', empleado.nombre, empleado.apellido1, SUBSTR(empleado.apellido2, 1, 1)) 
                        FROM empleado INNER JOIN usuarioempleado ON empleado.idEmpleado = usuarioempleado.idUsuarioEmpleado 
                    WHERE usuario = %s"""
            cur.execute(sql, (username,))
            return cur.fetchall()[0][0]
            miConexion.close()
        except:
            return "Sin nombre"
        finally:
                cur.close()

    #obtiene una tupla que contiene los cargos aspirado
    def get_cargos_postulado(self, username):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT cargo.nombreCargo from UsuarioAspirante
                    INNER JOIN aspirante ON aspirante.idAspirante = usuarioaspirante.idUsuarioAspirante
                    INNER JOIN inscripcion ON inscripcion.idAspirante = aspirante.idAspirante
                    INNER JOIN concurso ON concurso.idConcurso = inscripcion.idConcurso
                    INNER JOIN cargo ON cargo.idCargo = concurso.idCargo
                    where usuarioaspirante.usuario = %s"""
            cur.execute(sql, (username,))
            return cur.fetchall()[0]
            miConexion.close()
        except:
            return "Sin Cargos"
        finally:
                cur.close()  

    #obtiene una tupla que contiene las convocatorias en las que ha estado un aspirante
    def get_convocatoria_postulado(self, username):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT convocatoria.nombreConvocatoria from UsuarioAspirante
                    INNER JOIN aspirante ON aspirante.idAspirante = usuarioaspirante.idUsuarioAspirante
                    INNER JOIN inscripcion ON inscripcion.idAspirante = aspirante.idAspirante
                    INNER JOIN concurso ON concurso.idConcurso = inscripcion.idConcurso
                    INNER JOIN convocatoria ON convocatoria.idConvocatoria = concurso.idConvocatoria
                    where usuarioaspirante.usuario = %s"""
            cur.execute(sql, (username,))
            return cur.fetchall()[0]
            miConexion.close()
        except:
            return "No aplica"
        finally:
                cur.close()

    #obtiene el nivel de acceso de un empleado usando su username
    def get_nivel_Acceso(self,username):
        try:
            cur = self.miConexion.cursor()
            sql = """SELECT nivelacceso.nombreNivel FROM usuarioempleado 
                        INNER JOIN empleado ON empleado.idEmpleado = usuarioempleado.idEmpleado
                        INNER JOIN nivelacceso ON nivelacceso.idNivelAcceso = empleado.idNivelAcceso
                        where usuarioempleado.usuario = %s"""
            cur.execute(sql, (username,))
            return cur.fetchall()[0][0]
            miConexion.close()
        except:
            return "No se encontro nivel"
        finally:
                cur.close() 
    







