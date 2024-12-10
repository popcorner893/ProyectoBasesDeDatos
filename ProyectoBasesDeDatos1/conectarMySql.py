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
            
    # Obtiene el nombre completo usando el username        
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

	# Obtiene el nombre completo usando el username       
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
        
                
    # Regreesa una tripla con el nombre y apellidos de un usuario
    def get_list_full_name_aspirante(self, username):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT aspirante.nombre, aspirante.apellido1, aspirante.apellido2
                    FROM aspirante INNER JOIN usuarioaspirante ON aspirante.idAspirante = usuarioaspirante.idUsuarioAspirante 
                    WHERE usuarioaspirante.usuario = %s"""
            cur.execute(sql, (username,))
            return cur.fetchall()[0]
            miConexion.close()
        except:
            return ("Sin nombre","sin apellido","sin apellido")
        finally:
                cur.close()
                
    def get_list_full_name_empleado(self, username):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT empleado.nombre, empleado.apellido1, empleado.apellido2
                    FROM empleado INNER JOIN usuarioempleado ON empleado.idEmpleado = usuarioempleado.idUsuarioEmpleado 
                    WHERE usuarioempleado.usuario = %s"""
            cur.execute(sql, (username,))
            return cur.fetchall()[0]
            miConexion.close()
        except:
            return ("Sin nombre","sin apellido","sin apellido")
        finally:
                cur.close()
                
    def get_ciudad_aspirante(self, username):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT aspirante.ciudad FROM usuarioaspirante
                    INNER JOIN aspirante ON aspirante.idEmpleado = usuarioaspirante.idAspirante
                    where usuarioaspirante.usuario = %s"""
            cur.execute(sql, (username,))
            return cur.fetchall()[0][0]
            miConexion.close()
        except:
            return "No figura"
        finally:
                cur.close()
                
    def get_ciudad_empleado(self, username):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT empleado.ciudad FROM usuarioempleado 
			        INNER JOIN empleado ON empleado.idEmpleado = usuarioempleado.idEmpleado 
                    where usuarioempleado.usuario = %s"""
            cur.execute(sql, (username,))
            return cur.fetchall()[0][0]
            miConexion.close()
        except:
            return "No figura"
        finally:
                cur.close()
                
    #Regresa una lista con los cargos a los que esta aspirando un usuario            
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
            listaAux = []
            for dato in cur.fetchall():
                listaAux.append(dato)
            return listaAux
            miConexion.close()
        except:
            return ("Sin Cargos",)
        finally:
                cur.close()       
    
    #Regresa una lista con el id de  convocatorias a las que pertenece un aspirante
    def get_convocatoria_postulado(self, username): 
        try:
            cur = self.conexion.cursor()
            sql = """SELECT convocatoria.idConvocatoria from UsuarioAspirante
                    INNER JOIN aspirante ON aspirante.idAspirante = usuarioaspirante.idUsuarioAspirante
                    INNER JOIN inscripcion ON inscripcion.idAspirante = aspirante.idAspirante
                    INNER JOIN concurso ON concurso.idConcurso = inscripcion.idConcurso
                    INNER JOIN convocatoria ON convocatoria.idConvocatoria = concurso.idConvocatoria
                    where usuarioaspirante.usuario = %s"""
            cur.execute(sql, (username,))
            listaAux = []
            for dato in cur.fetchall():
                listaAux.append(dato)
            return listaAux
            miConexion.close()
        except:
            return ("No aplica",)
        finally:
                cur.close()          
    
    #retorna una lista de duplas con los nombres y id de todas las convocatorias en la base de datos
    #[('Convocatoria 2025-1', 1), ('Convocatoria 2025-2', 2), ('Convocatoria 2025-3', 3)]
    def get_name_id_all_convocatorias(self):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT convocatoria.nombreConvocatoria, convocatoria.idConvocatoria FROM convocatoria"""
            cur.execute(sql)
            listaAux = []
            for dato in cur.fetchall():
                listaAux.append(dato)
            return listaAux
            miConexion.close()
        except:
            return [("No aplica",),("No aplica",)]
        finally:
                cur.close()   
    
    #retorna una lista con los cargos que se ofrecen en una convocatoria
    def get_cargos_convocatoria(self, convocatoria):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT cargo.nombreCargo FROM convocatoria 
                    INNER JOIN concurso ON concurso.idConvocatoria = convocatoria.idConvocatoria
                    INNER JOIN cargo On cargo.idCargo = concurso.idCargo
                    WHERE convocatoria.idConvocatoria = %s"""
            cur.execute(sql, (convocatoria,))
            listaAux = []
            for dato in cur.fetchall():
                listaAux.append(dato[0])
            return listaAux
            miConexion.close()
        except:
            return ("No se encontraron cargos",)
        finally:
                cur.close()    
    
    def get_nivel_Acceso(self,username):
        try:
            cur = self.conexion.cursor()
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
    
    #Regresa una lista de los Idconcursos de un aspirante atraves de su usuario
    def get_id_concurso(self,username):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT concurso.idConcurso FROM usuarioaspirante 
                        INNER JOIN aspirante ON aspirante.idAspirante = usuarioaspirante.idUsuarioAspirante
                        INNER JOIN inscripcion ON inscripcion.idAspirante = aspirante.idAspirante
                        INNER JOIN concurso ON concurso.idConcurso = inscripcion.idConcurso
                        where usuarioaspirante.usuario = %s"""
            cur.execute(sql, (username,))
            listaAux = []
            for dato in cur.fetchall():
                listaAux.append(dato)
            return listaAux
            miConexion.close()
        except:
            return ("No se encontro ID",)
        finally:
                cur.close() 
                
    #Obtiene una dupla con el area diciplinar y titulacion minima del perfil apartir de un ID concurso
    def get_perfiles_concurso(self, idConcurso):    
        try:
            cur = self.conexion.cursor()
            sql = """SELECT perfil.areaDisciplinar, perfil.titulacionRequerida FROM 
		            perfil INNER JOIN concurso ON perfil.idPerfil = concurso.idPerfil
                    where concurso.idConcurso = %s"""
            cur.execute(sql, (idConcurso,))
            return cur.fetchall()[0]
            miConexion.close()
        except:
            return ("No se encontraron perfiles","No se encontraron perfiles")
        finally:
                cur.close() 
    
    #Obtiene en forma de String el estao de un concurso apartir de su id  
    def get_estado_concurso(self, idConcurso):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT estado FROM concurso
                    WHERE idConcurso = %s"""
            cur.execute(sql, (idConcurso,))
            return cur.fetchall()[0][0]
            miConexion.close()
        except:
            return "---"
        finally:
                cur.close()       
    
    #Obtiene una dupla con la fecha de inicio y decha de hoja de vida de un concurso mediante su id
    def get_fecha_inicio_hojavida_concurso(self, idConcurso):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT cronogramaactividades.fechaInicio, cronogramaactividades.fechaHojasDeVida FROM 
		            concurso INNER JOIN cronogramaactividades On concurso.idCronograma = cronogramaactividades.idCronograma
                    where concurso.idConcurso = %s"""
            cur.execute(sql, (idConcurso,))
            return cur.fetchall()[0]
            miConexion.close()
        except:
            return ("No se encontraron fechas", "No se encontraron fechas")
        finally:
                cur.close()                 
    # Obtiene el nombre completo usando el username        
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

	# Obtiene el nombre completo usando el username       
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
                
    #Regresa una lista con los cargos a los que esta aspirando un usuario            
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
            listaAux = []
            for dato in cur.fetchall():
                listaAux.append(dato)
            return listaAux
            miConexion.close()
        except:
            return ("Sin Cargos",)
        finally:
                cur.close()       
    
    #Regresa una lista con el id de  convocatorias a las que pertenece un aspirante
    def get_convocatoria_postulado(self, username): 
        try:
            cur = self.conexion.cursor()
            sql = """SELECT convocatoria.idConvocatoria from UsuarioAspirante
                    INNER JOIN aspirante ON aspirante.idAspirante = usuarioaspirante.idUsuarioAspirante
                    INNER JOIN inscripcion ON inscripcion.idAspirante = aspirante.idAspirante
                    INNER JOIN concurso ON concurso.idConcurso = inscripcion.idConcurso
                    INNER JOIN convocatoria ON convocatoria.idConvocatoria = concurso.idConvocatoria
                    where usuarioaspirante.usuario = %s"""
            cur.execute(sql, (username,))
            listaAux = []
            for dato in cur.fetchall():
                listaAux.append(dato)
            return listaAux
            miConexion.close()
        except:
            return ("No aplica",)
        finally:
                cur.close()          
    
    #retorna una lista de duplas con los nombres y id de todas las convocatorias en la base de datos
    #[('Convocatoria 2025-1', 1), ('Convocatoria 2025-2', 2), ('Convocatoria 2025-3', 3)]
    def get_name_id_all_convocatorias(self):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT convocatoria.nombreConvocatoria, convocatoria.idConvocatoria FROM convocatoria"""
            cur.execute(sql)
            listaAux = []
            for dato in cur.fetchall():
                listaAux.append(dato)
            return listaAux
            miConexion.close()
        except:
            return [("No aplica",),("No aplica",)]
        finally:
                cur.close()   
    
    #retorna una lista con los cargos que se ofrecen en una convocatoria
    def get_cargos_convocatoria(self, convocatoria):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT cargo.nombreCargo FROM convocatoria 
                    INNER JOIN concurso ON concurso.idConvocatoria = convocatoria.idConvocatoria
                    INNER JOIN cargo On cargo.idCargo = concurso.idCargo
                    WHERE convocatoria.idConvocatoria = %s"""
            cur.execute(sql, (convocatoria,))
            listaAux = []
            for dato in cur.fetchall():
                listaAux.append(dato[0])
            return listaAux
            miConexion.close()
        except:
            return ("No se encontraron cargos",)
        finally:
                cur.close()    
    
    def get_nivel_Acceso(self,username):
        try:
            cur = self.conexion.cursor()
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
    
    #Regresa una lista de los Idconcursos de un aspirante atraves de su usuario
    def get_id_concurso(self,username):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT concurso.idConcurso FROM usuarioaspirante 
                        INNER JOIN aspirante ON aspirante.idAspirante = usuarioaspirante.idUsuarioAspirante
                        INNER JOIN inscripcion ON inscripcion.idAspirante = aspirante.idAspirante
                        INNER JOIN concurso ON concurso.idConcurso = inscripcion.idConcurso
                        where usuarioaspirante.usuario = %s"""
            cur.execute(sql, (username,))
            listaAux = []
            for dato in cur.fetchall():
                listaAux.append(dato)
            return listaAux
            miConexion.close()
        except:
            return ("No se encontro ID",)
        finally:
                cur.close() 
                
    #Obtiene una dupla con el area diciplinar y titulacion minima del perfil apartir de un ID concurso
    def get_perfiles_concurso(self, idConcurso):    
        try:
            cur = self.conexion.cursor()
            sql = """SELECT perfil.areaDisciplinar, perfil.titulacionRequerida FROM 
		            perfil INNER JOIN concurso ON perfil.idPerfil = concurso.idPerfil
                    where concurso.idConcurso = %s"""
            cur.execute(sql, (idConcurso,))
            return cur.fetchall()[0]
            miConexion.close()
        except:
            return ("No se encontraron perfiles","No se encontraron perfiles")
        finally:
                cur.close() 
    
    #Obtiene en forma de String el estao de un concurso apartir de su id  
    def get_estado_concurso(self, idConcurso):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT estado FROM concurso
                    WHERE idConcurso = %s"""
            cur.execute(sql, (idConcurso,))
            return cur.fetchall()[0][0]
            miConexion.close()
        except:
            return "---"
        finally:
                cur.close()       
    
    #Obtiene una dupla con la fecha de inicio y decha de hoja de vida de un concurso mediante su id
    def get_fecha_inicio_hojavida_concurso(self, idConcurso):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT cronogramaactividades.fechaInicio, cronogramaactividades.fechaHojasDeVida FROM 
		            concurso INNER JOIN cronogramaactividades On concurso.idCronograma = cronogramaactividades.idCronograma
                    where concurso.idConcurso = %s"""
            cur.execute(sql, (idConcurso,))
            return cur.fetchall()[0]
            miConexion.close()
        except:
            return ("No se encontraron fechas", "No se encontraron fechas")
        finally:
                cur.close()                 

    
    def anade_usuario(self, mode, nombre, ciudad, apellido1, apellido2, usuario, contrasena, nivelAcceso):
        
        if mode == 0:

            cur = self.conexion.cursor()

            try:
                # Inserción en la tabla Aspirante
                query_aspirante = """
                    INSERT INTO Aspirante (nombre, ciudad, apellido1, apellido2, idHojadeVida)
                    VALUES (%s, %s, %s, %s, NULL)
                """
                cur.execute(query_aspirante, (nombre, ciudad, apellido1, apellido2))
                
                # Recuperar el ID del aspirante recién insertado
                id_aspirante = cur.lastrowid
                
                # Inserción en la tabla UsuarioAspirante
                query_usuario = """
                    INSERT INTO UsuarioAspirante (usuario, password, idAspirante)
                    VALUES (%s, %s, %s)
                """
                cur.execute(query_usuario, (usuario, contrasena, id_aspirante))
                
                # Confirmar los cambios
                self.conexion.commit()
                messagebox.showinfo("Éxito", "Usuario Creado Correctamente")
            
            except Exception as e:
                # Revertir los cambios si algo falla
                self.conexion.rollback()
                print(f"Error al agregar el usuario y el aspirante: {e}")
    

            cur.close()


        elif mode == 1:

            cur = self.conexion.cursor()

            if int(nivelAcceso) > 2: nivelAcceso = 2

            try:
                # Inserción en la tabla Aspirante
                query_empleado = """
                    INSERT INTO empleado (nombre, ciudad, apellido1, apellido2, idNivelAcceso)
                    VALUES (%s, %s, %s, %s, %s)

                """

                

                cur.execute(query_empleado, (nombre, ciudad, apellido1, apellido2, nivelAcceso))
                
                # Recuperar el ID del aspirante recién insertado
                id_empleado = cur.lastrowid
                
                # Inserción en la tabla UsuarioAspirante
                query_usuario = """
                    INSERT INTO UsuarioEmpleado (usuario, password, idEmpleado)
                    VALUES (%s, %s, %s)
                """
                cur.execute(query_usuario, (usuario, contrasena, id_empleado))
                
                # Confirmar los cambios
                self.conexion.commit()
                messagebox.showinfo("Éxito", "Usuario Creado Correctamente")
            
            except Exception as e:
                # Revertir los cambios si algo falla
                self.conexion.rollback()
                messagebox.showerror("Error", "Error al Agregar el Usuario")
    

            cur.close()


    def modificar_usuario(self, mode, nombre, ciudad, apellido1, apellido2, usuario, contrasena, nivelAcceso, id):

        if mode == 0:

            cur = self.conexion.cursor()
            try:
                # Actualización en la tabla Aspirante
                query_aspirante = """
                    UPDATE Aspirante
                    SET 
                        nombre = COALESCE(%s, nombre),
                        ciudad = COALESCE(%s, ciudad),
                        apellido1 = COALESCE(%s, apellido1),
                        apellido2 = COALESCE(%s, apellido2)
                    WHERE idAspirante = %s
                """
                cur.execute(query_aspirante, (nombre, ciudad, apellido1, apellido2, id))

                # Actualización en la tabla UsuarioAspirante
                query_usuario = """
                    UPDATE UsuarioAspirante
                    SET 
                        usuario = COALESCE(%s, usuario),
                        password = COALESCE(%s, password)
                    WHERE idAspirante = %s
                """
                cur.execute(query_usuario, (usuario, contrasena, id))

                # Confirmar los cambios
                self.conexion.commit()
                messagebox.showinfo("Éxito", "Usuario Modificado Correctamente")

            except Exception as e:
                # Revertir los cambios si algo falla
                self.conexion.rollback()
                print(f"Error al modificar el usuario y el aspirante: {e}")
                messagebox.showerror("Error", f"No se pudo modificar el usuario: {e}")
    

            cur.close()


        elif mode == 1:

            cur = self.conexion.cursor()

            if int(nivelAcceso) > 2: nivelAcceso = 2
            try:
                # Actualización en la tabla Aspirante
                query_empleado = """
                    UPDATE Empleado
                    SET 
                        nombre = COALESCE(%s, nombre),
                        ciudad = COALESCE(%s, ciudad),
                        apellido1 = COALESCE(%s, apellido1),
                        apellido2 = COALESCE(%s, apellido2),
                        idNivelAcceso = COALESCE(%s, idNivelAcceso)
                    WHERE idEmpleado = %s
                """
                cur.execute(query_empleado, (nombre, ciudad, apellido1, apellido2,nivelAcceso, id))

                # Actualización en la tabla UsuarioAspirante
                query_usuario = """
                    UPDATE UsuarioEmpleado
                    SET 
                        usuario = COALESCE(%s, usuario),
                        password = COALESCE(%s, password)
                    WHERE idEmpleado = %s
                """
                cur.execute(query_usuario, (usuario, contrasena, id))

                # Confirmar los cambios
                self.conexion.commit()
                messagebox.showinfo("Éxito", "Usuario Modificado Correctamente")

            except Exception as e:
                # Revertir los cambios si algo falla
                self.conexion.rollback()
                print(f"Error al modificar el usuario y el aspirante: {e}")
                messagebox.showerror("Error", f"No se pudo modificar el usuario: {e}")
    

            cur.close()


    def existe_aspirante(self, id):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT 1 FROM Aspirante WHERE idAspirante = %s LIMIT 1"
            cur.execute(sql, (id,))
            resultado = cur.fetchone()
            return resultado is not None  # Devuelve True si existe, False si no
        finally:
            cur.close()


    def buscar_info_aspirante(self, id):
        try:
            cur = self.conexion.cursor()
            sql = """
                SELECT 
                    UsuarioAspirante.usuario,
                    UsuarioAspirante.password,
                    Aspirante.nombre,
                    Aspirante.apellido1,
                    Aspirante.apellido2,
                    Aspirante.ciudad
                FROM 
                    Aspirante
                JOIN 
                    UsuarioAspirante 
                ON 
                    UsuarioAspirante.idAspirante = Aspirante.idAspirante
                WHERE 
                    Aspirante.idAspirante = %s
            """
            cur.execute(sql, (id,))
            resultado = cur.fetchone()
            return resultado  # Devuelve una tupla con los datos o None si no existe
        finally:
            cur.close()

    
    def existe_empleado(self, id):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT 1 FROM empleado WHERE idEmpleado = %s LIMIT 1"
            cur.execute(sql, (id,))
            resultado = cur.fetchone()
            return resultado is not None  # Devuelve True si existe, False si no
        finally:
            cur.close()


    def buscar_info_empleado(self, id):
        try:
            cur = self.conexion.cursor()
            sql = """
                SELECT 
                    UsuarioEmpleado.usuario,
                    UsuarioEmpleado.password,
                    Empleado.nombre,
                    Empleado.apellido1,
                    Empleado.apellido2,
                    Empleado.ciudad,
                    Empleado.idNivelAcceso
                FROM 
                    Empleado
                JOIN 
                    UsuarioEmpleado 
                ON 
                    UsuarioEmpleado.idEmpleado = Empleado.idEmpleado
                WHERE 
                    Empleado.idEmpleado = %s
            """
            cur.execute(sql, (id,))
            resultado = cur.fetchone()
            return resultado  # Devuelve una tupla con los datos o None si no existe
        finally:
            cur.close()


    def eliminarUsuarioAspirante(self, mode, id):

        if mode == 0:

            try:
                cur = self.conexion.cursor()

                # Eliminar primero de la tabla UsuarioAspirante
                sql_eliminar_usuario = "DELETE FROM UsuarioAspirante WHERE idAspirante = %s"
                cur.execute(sql_eliminar_usuario, (id,))

                # Luego, eliminar de la tabla Aspirante
                sql_eliminar_aspirante = "DELETE FROM Aspirante WHERE idAspirante = %s"
                cur.execute(sql_eliminar_aspirante, (id,))

                # Confirmar los cambios
                self.conexion.commit()
                messagebox.showinfo("Éxito", "Usuario aspirante eliminado correctamente.")

            except Exception as e:
                # Revertir cambios en caso de error
                self.conexion.rollback()
                print(f"Error al eliminar el usuario aspirante: {e}")
                messagebox.showerror("Error", f"No se pudo eliminar el usuario aspirante: {e}")

        elif mode == 1:

            try:
                cur = self.conexion.cursor()

                # Eliminar primero de la tabla UsuarioAspirante
                sql_eliminar_usuario = "DELETE FROM UsuarioEmpleado WHERE idEmpleado = %s"
                cur.execute(sql_eliminar_usuario, (id,))

                # Luego, eliminar de la tabla Aspirante
                sql_eliminar_empleado = "DELETE FROM Empleado WHERE idEmpleado = %s"
                cur.execute(sql_eliminar_empleado, (id,))

                # Confirmar los cambios
                self.conexion.commit()
                messagebox.showinfo("Éxito", "Usuario empleado eliminado correctamente.")

            except Exception as e:
                # Revertir cambios en caso de error
                self.conexion.rollback()
                print(f"Error al eliminar el usuario empleado: {e}")
                messagebox.showerror("Error", f"No se pudo eliminar el usuario empleado: {e}")


        
        cur.close()


	#Mis cambios:

    def insertar_datos_acuerdo(self, archivoAcuerdo):
        try:
            cur = self.conexion.cursor()   
            cur.execute('''
            INSERT INTO Acuerdo (archivoAcuerdo)
            VALUES (%s)
            ''', (archivoAcuerdo,))
            self.conexion.commit()
            idAcuerdo = cur.lastrowid
            return idAcuerdo
        except Exception as e:
            self.conexion.rollback()
            messagebox.showerror("Error", "Error al insertar acuerdo")

    def insertar_datos_calendario(self,fechainicio, fechafin):
        try:
            cur = self.conexion.cursor()   
            cur.execute('''
            INSERT INTO CalendarioConvocatoria (fechaInicio, fechaFin)
            VALUES (%s, %s)
            ''', (fechainicio, fechafin))
            self.conexion.commit()
            idCalendario = cur.lastrowid  # Obtener el id del último acuerdo insertado
            cur.close()
            return idCalendario
        except Exception as e:
            self.conexion.rollback()
            messagebox.showerror("Error", "Error al insertar calendario")
    

            cur.close()

    def insertar_datos_convocatoria(self, nombreConvocatoria, idCalendario, idAcuerdo,imagenConvocatoria):
        try:
            cur = self.conexion.cursor()   
            cur.execute('''INSERT INTO Convocatoria (nombreConvocatoria, idCalendario, idAcuerdo, imagenConvocatoria)
            VALUES (%s, %s, %s, %s)
            ''', (nombreConvocatoria, idCalendario, idAcuerdo, imagenConvocatoria))
            self.conexion.commit()
            idConvocatoria = cur.lastrowid  # Obtener el id del último acuerdo insertado
            cur.close()
            return idConvocatoria
        except Exception as e:
            self.conexion.rollback()
            messagebox.showerror("Error", "Error al insertar convocatoria")
    

            cur.close()

    def insertar_datos_concurso(self, idCargo, idPerfil, idCronograma, idConvocatoria, idComite, estado):
        try:
            cur = self.conexion.cursor()
            cur.execute('''
            INSERT INTO Concurso (idPerfil, idCargo, idCronograma, idConvocatoria, idComite, estado)
            VALUES (%s, %s, %s, %s, %s, %s)
            ''', (idCargo, idPerfil, idCronograma, idConvocatoria, idComite, estado))
            self.conexion.commit()
            idConcurso = cur.lastrowid
            cur.close()
            return idConcurso
        except Exception as e:
            self.conexion.rollback()
            messagebox.showerror("Error", "Error al insertar concurso")
        
    def obtener_o_insertar_cargo(self, nombreCargo, idEscuela):
        try:
        # Verificar si el cargo existe
            cur = self.conexion.cursor()
            sql_select = "SELECT idCargo FROM Cargo WHERE nombreCargo = %s"
            cur.execute(sql_select, (nombreCargo,))
            resultado = cur.fetchone()
        
            if resultado:
            # Si existe, devolver el ID
                return resultado[0]
            else:
            # Si no existe, insertar y devolver el nuevo ID
                sql_insert = '''
                INSERT INTO Cargo (nombreCargo, idEscuela)
                VALUES (%s, %s)
                '''
                cur.execute(sql_insert, (nombreCargo, idEscuela))
                self.conexion.commit()
                return cur.lastrowid
        except Exception as e:
        # Manejo de errores e impresión del mensaje
            self.conexion.rollback()
            messagebox.showerror("Error", f"Error al procesar el cargo: {e}")
        finally:
            cur.close()

    def obtener_o_insertar_escuela(self, nombreEscuela):
        try:
        # Verificar si el cargo existe
            cur = self.conexion.cursor()
            sql_select = "SELECT idEscuela FROM Escuela WHERE nombreEscuela = %s"
            cur.execute(sql_select, (nombreEscuela,))
            resultado = cur.fetchone()
        
            if resultado:
            # Si existe, devolver el ID
                return resultado[0]
            else:
            # Si no existe, insertar y devolver el nuevo ID
                sql_insert = '''
                INSERT INTO Escuela (nombreEscuela)
                VALUES (%s)
                '''
                cur.execute(sql_insert, (nombreEscuela))
                self.conexion.commit()
                return cur.lastrowid
        except Exception as e:
        # Manejo de errores e impresión del mensaje
            self.conexion.rollback()
            messagebox.showerror("Error", f"Error al procesar el cargo: {e}")
        finally:
            cur.close()

    def obtener_o_insertar_perfil(self, areaD, titu, exp, areaA, compromiso, modalidad):
        try:
        # Conexión a la base de datos
            cur = self.conexion.cursor()

        # Verificar si el perfil ya existe
            sql_select = """
            SELECT idPerfil 
            FROM Perfil 
            WHERE areaDisciplinar = %s AND titulacionRequerida = %s AND experiencia = %s AND areaAcademica = %s AND compromisoFormacion = %s AND idModalidad = %s
            """
            cur.execute(sql_select, (areaD, titu, exp, areaA, compromiso, modalidad))
            resultado = cur.fetchone()

            if resultado:
            # Si existe, devolver el ID del perfil
                return resultado[0]
            else:
            # Si no existe, insertar el nuevo perfil
                sql_insert = '''
                INSERT INTO Perfil (areaDisciplinar, titulacionRequerida, experiencia, areaAcademica, compromisoFormacion, idModalidad)
                VALUES (%s, %s, %s, %s, %s, %s)
                '''
                cur.execute(sql_insert, (areaD, titu, exp, areaA, compromiso, modalidad))
                self.conexion.commit()
                return cur.lastrowid
        except Exception as e:
        # Manejo de errores
            self.conexion.rollback()
            messagebox.showerror("Error", f"Error al procesar el perfil: {e}")
        finally:
            cur.close()


    def obtener_Modalidad(self, nombreModalidad):
        try:
        # Verificar si el cargo existe
            cur = self.conexion.cursor()
            sql_select = "SELECT idModalidad FROM modalidad WHERE nombreModalidad = %s"
            cur.execute(sql_select, (nombreModalidad,))
            resultado = cur.fetchone()
            return resultado[0]
        except Exception as e:
        # Manejo de errores e impresión del mensaje
            self.conexion.rollback()
            messagebox.showerror("Error", f"Error al procesar el cargo: {e}")
        finally:
            cur.close()

    def obtener_o_insertar_cronograma(self, fechainicio, fechaHojasDeVida, fechaPsicotecnica, fechaSesionDocente, fechaEntrevista, fechaFin):
        try:
        # Conexión a la base de datos
            cur = self.conexion.cursor()

        # Verificar si el perfil ya existe
            sql_select = """
            SELECT idCronograma 
            FROM cronogramaactividades 
            WHERE fechainicio = %s AND fechaHojasDeVida = %s AND fechaPsicotecnica = %s AND fechaSesionDocente = %s AND fechaEntrevista = %s AND fechaFin = %s
            """
            cur.execute(sql_select, (fechainicio, fechaHojasDeVida, fechaPsicotecnica, fechaSesionDocente, fechaEntrevista, fechaFin))
            resultado = cur.fetchone()

            if resultado:
            # Si existe, devolver el ID del perfil
                return resultado[0]
            else:
            # Si no existe, insertar el nuevo perfil
                sql_insert = '''
                INSERT INTO cronogramaactividades (fechainicio, fechaHojasDeVida, fechaPsicotecnica, fechaSesionDocente, fechaEntrevista, fechaFin)
                VALUES (%s, %s, %s, %s, %s, %s)
                '''
                cur.execute(sql_insert, (fechainicio, fechaHojasDeVida, fechaPsicotecnica, fechaSesionDocente, fechaEntrevista, fechaFin))
                self.conexion.commit()
                return cur.lastrowid
        except Exception as e:
        # Manejo de errores
            self.conexion.rollback()
            messagebox.showerror("Error", f"Error al procesar el perfil: {e}")
        finally:
            cur.close()

    def obtener_o_insertar_calendarioConv(self, fechainicio, fechafin):
        try:
        # Conexión a la base de datos
            cur = self.conexion.cursor()

        # Verificar si el perfil ya existe
            sql_select = """
            SELECT idCalendario 
            FROM calendarioconvocatoria 
            WHERE fechainicio = %s AND fechaFin = %s
            """
            cur.execute(sql_select, (fechainicio, fechafin))
            resultado = cur.fetchone()

            if resultado:
            # Si existe, devolver el ID del perfil
                return resultado[0]
            else:
            # Si no existe, insertar el nuevo perfil
                sql_insert = '''
                INSERT INTO cronogramaactividades (fechainicio, fechaFin)
                VALUES (%s, %s)
                '''
                cur.execute(sql_insert, (fechainicio, fechafin))
                self.conexion.commit()
                return cur.lastrowid
        except Exception as e:
        # Manejo de errores
            self.conexion.rollback()
            messagebox.showerror("Error", f"Error al procesar el perfil: {e}")
        finally:
            cur.close()
		
    def insertar_datos_comite(self):
        try:
            cur = self.conexion.cursor()   
            cur.execute('''INSERT INTO comiteevaluacion (nombreComite)
            VALUES (%s)
            ''', ("Comite"))
            self.conexion.commit()
            idComite = cur.lastrowid  # Obtener el id del último acuerdo insertado
            cur.close()
            return idComite
        except Exception as e:
            self.conexion.rollback()
            messagebox.showerror("Error", "Error al insertar convocatoria")

    def hallar_nivel_acceso(self, idEmpleado):
        try:
            cur = self.conexion.cursor()
            sql_select = """SELECT idNivelAcceso FROM empleado WHERE idEmpleado = %s"""
            cur.execute(sql_select, (idEmpleado))
            resultado = cur.fetchone()
            if resultado:
            # Devolver el ID del nivel acceso
                return resultado[0]
        except Exception as e:
            self.conexion.rollback()
            messagebox.showerror("Error", "No se encontró el Empleado")

    def anadir_comite_empleado(self, idComite, idEmpleado):
        try:
            cur = self.conexion.cursor()
            sql_insert = '''
                INSERT INTO comiteempleado (idComite, idEmpleado)
                VALUES (%s, %s)
                '''
            cur.execute(sql_insert, (idComite, idEmpleado))
            self.conexion.commit()
        except Exception as e:
            self.conexion.rollback()
            messagebox.showerror("Error", "No se encontró el Empleado")












