import pymysql

class MiConexion:
    def __init__(self):
        self.conexion = pymysql.connect(host='localhost', user='root', passwd='', db='seleccionprof')

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