import conectarMySql


class sesionActualAspirante:

    username = ""
    password = ""
    nombre = ""
    cargos = ""
    concursos = ""
    convocatoria = ""

   
    @classmethod
    def crearSesion(self, username, password):
        sesionActualAspirante.username = username
        sesionActualAspirante.password = password
        sesionActualAspirante.nombre = conectarMySql.MiConexion.get_full_name_aspirante(username)
        sesionActualAspirante.cargos = conectarMySql.MiConexion.get_cargos_postulado(username)
        sesionActualAspirante.convocatoria = conectarMySql.MiConexion.get_convocatoria_postulado(username)
        
    @classmethod
    def cerrarSesion(cls, clave):
        sesionActualAspirante.username = ""
        sesionActualAspirante.password = ""
        sesionActualAspirante.nombre = ""
        sesionActualAspirante.cargos = ""
        sesionActualAspirante.concursos = ""
        sesionActualAspirante.convocatoria = ""  
    
class sesionActualEmpleado:
    
    username = ""
    password = ""
    nombre = ""
    nivelAceso = ""
    
    @classmethod
    def crearSesion(self, username, password):
        sesionActualEmpleado.username = username
        sesionActualEmpleado.password = password
        sesionActualEmpleado.nombre = conectarMySql.MiConexion.get_full_name_empleado(username)
        sesionActualEmpleado.nivelAceso = conectarMySql.MiConexion.get_nivel_Acceso(username)

    @classmethod
    def cerrarSesion(cls, clave):
        sesionActualEmpleado.username = ""
        sesionActualEmpleado.password = ""
        sesionActualEmpleado.nombre = ""
        sesionActualEmpleado.cargos = ""
        sesionActualEmpleado.concursos = ""
        sesionActualEmpleado.convocatoria = ""  
    
