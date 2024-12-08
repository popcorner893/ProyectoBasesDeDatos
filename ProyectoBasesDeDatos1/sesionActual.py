import conectarMySql


class sesionActualAspirante:

    username = ""
    password = ""
    nombre = ""
    cargos = ""
import conectarMySql


class sesionActualAspirante:

    username = ""
    password = ""
    nombre = ""
    cargos = ""
    idconcursos = ""
    convocatoria = ""
   
    @classmethod
    def crearSesion(self, username, password):
        conexion = conectarMySql.MiConexion()
        sesionActualAspirante.username = username
        sesionActualAspirante.password = password
        sesionActualAspirante.nombre = conexion.get_full_name_aspirante(username)
        sesionActualAspirante.cargos = conexion.get_cargos_postulado(username)
        sesionActualAspirante.idconcursos = conexion.get_id_concurso
        sesionActualAspirante.convocatoria = conexion.get_convocatoria_postulado(username)
        
    @classmethod
    def cerrarSesion():
        sesionActualAspirante.username = ""
        sesionActualAspirante.password = ""
        sesionActualAspirante.nombre = ""
        sesionActualAspirante.cargos = ""
        sesionActualAspirante.idconcursos = ""
        sesionActualAspirante.convocatoria = ""  
    
class sesionActualEmpleado:
    
    username = ""
    password = ""
    nombre = ""
    nivelAceso = ""
    
    @classmethod
    def crearSesion(self, username, password):
        conexion = conectarMySql.MiConexion()
        sesionActualEmpleado.username = username
        sesionActualEmpleado.password = password
        sesionActualEmpleado.nombre = conexion.get_full_name_empleado(username)
        sesionActualEmpleado.nivelAceso = conexion.get_nivel_Acceso(username)

    @classmethod
    def cerrarSesion():
        sesionActualEmpleado.username = ""
        sesionActualEmpleado.password = ""
        sesionActualEmpleado.nombre = ""
        sesionActualEmpleado.nivelAceso = ""
