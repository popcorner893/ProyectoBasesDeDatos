from customtkinter import *
import tkinter as tk
from PIL import Image
from Utilidades import *
import PantallaPrincipalEmpleado, PantallaPerfil, conectarMySql
import tkinter.messagebox as messagebox


class GestionarUsuariosPrincipal(CTkFrame):

    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

        self.controller = controller
        
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)


    
        # Crear canvas para manejar la imagen y el texto
        canvas = tk.Canvas(self, width=640, height=721, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        #Imagen de Fondo             
        self.img_fondo = tk.PhotoImage(file="FondoDegradadoMain.png")  # Mantener referencia a la imagen
        canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")  # Colocar la imagen en la esquina superior izquierda     


        frameBlancoFondo = CTkFrame(
            canvas,
            bg_color= "white",
            fg_color= "white",
            corner_radius=20,
            width=1200,
            height=600,
        )

        frameBlancoFondo.pack(expand = True)
        frameBlancoFondo.pack_propagate(False)


        panelUsuario = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 90                  
        )


        panelInformacion = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 510
                     
        )


        #Dividir la pantalla en 2 paneles distintos
        panelUsuario.pack(expand = True, fill = "x")
        panelUsuario.pack_propagate(False)
        panelInformacion.pack(expand = True, fill = "x")
        panelInformacion.pack_propagate(False)


        #Ícono para volver atrás
        iconBack = CTkImage(dark_image= Image.open("BackSymbol1.png"), size = (51,51))
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white", command =lambda: self.controller.show_frame(PantallaPrincipalEmpleado.MenuPrincipalUsuario))
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white", command=lambda: self.controller.show_frame(PantallaPerfil.PantallaPerfilEmpleado))
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Mensaje Principal de Ventana

        panelTitulo = CTkFrame(panelInformacion, fg_color = "transparent", corner_radius=16)
        panelTitulo.pack(fill = "x")

        textoPrincipal = bigText(panelTitulo,"Gestión de Usuarios")
        textoPrincipal.pack(side = "left", padx = 50)

        
        #Panel de Información

        panelPrincipal = CTkFrame(panelInformacion, fg_color = "transparent", width = 1120, height = 420, corner_radius=16)
        panelPrincipal.pack(expand = True)
        panelPrincipal.pack_propagate(False)


        #Agregar Usuario


        panelAgregar = CTkFrame(panelPrincipal, fg_color= "#DEEDFD", corner_radius=16, height = 80)
        panelAgregar.pack(anchor = "nw", fill = "x", pady = 18)
        panelAgregar.pack_propagate(False)

        textoAgregar = mediumText(panelAgregar, "Agregar Usuarios")
        textoAgregar.pack(side = "left", padx = 10)

        botonAgregarEmpleado = botonAccion(panelAgregar, "Empleado", 25, "verde", 60, 34, lambda: self.controller.show_frame(AnadirUsuarioEmpleado))
        botonAgregarEmpleado.pack(side = "right", padx = 10)

        botonAgregarAspirante = botonAccion(panelAgregar, "Aspirante", 25, "verde", 60, 34, lambda: self.controller.show_frame(AnadirUsuarioAspirante))
        botonAgregarAspirante.pack(side = "right", padx = 10)



        #Modificar Usuario 

        panelModificar = CTkFrame(panelPrincipal, fg_color= "#DEEDFD", corner_radius=16, height = 80)
        panelModificar.pack(anchor = "nw", fill = "x")
        panelModificar.pack_propagate(False)

        textoModificar = mediumText(panelModificar, "Modificar Usuario")
        textoModificar.pack(side = "left", padx = 10)

        botonModificarEmpleado = botonAccion(panelModificar, "Empleado", 25, "verde", 60, 34, lambda: self.controller.show_frame(ModificarUsuarioEmpleado))
        botonModificarEmpleado.pack(side = "right", padx = 10)

        botonModificarAspirante = botonAccion(panelModificar, "Aspirante", 25, "verde", 60, 34, lambda: self.controller.show_frame(ModificarUsuarioAspirante))
        botonModificarAspirante.pack(side = "right", padx = 10)


        #Eliminar Usuario 

        panelEliminar = CTkFrame(panelPrincipal, fg_color= "#DEEDFD", corner_radius=16, height = 80)
        panelEliminar.pack(anchor = "nw", fill = "x", pady = 20)
        panelEliminar.pack_propagate(False)

        textoEliminar = mediumText(panelEliminar, "Eliminar Usuario")
        textoEliminar.pack(side = "left", padx = 10)

        botonEliminarEmpleado = botonAccion(panelEliminar, "Empleado", 25, "verde", 60, 34, lambda: self.controller.show_frame(EliminarUsuarioEmpleado))
        botonEliminarEmpleado.pack(side = "right", padx = 10)

        botonEliminarAspirante = botonAccion(panelEliminar, "Aspirante", 25, "verde", 60, 34, lambda: self.controller.show_frame(EliminarUsuarioAspirante))
        botonEliminarAspirante.pack(side = "right", padx = 10)


class AnadirUsuarioAspirante(CTkFrame):
    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

        self.controller = controller

        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)



        # Crear canvas para manejar la imagen y el texto
        canvas = tk.Canvas(self, width=640, height=721, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        #Imagen de Fondo
        self.img_fondo = tk.PhotoImage(file="FondoDegradadoMain.png")  # Mantener referencia a la imagen
        canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")  # Colocar la imagen en la esquina superior izquierda     


        frameBlancoFondo = CTkFrame(
            canvas,
            bg_color= "white",
            fg_color= "white",
            corner_radius=20,
            width=1200,
            height=600,
        )

        frameBlancoFondo.pack(expand = True)
        frameBlancoFondo.pack_propagate(False)


        panelUsuario = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 90                  
        )


        panelInformacion = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 510
                     
        )


        #Dividir la pantalla en 2 paneles distintos
        panelUsuario.pack(expand = True, fill = "x")
        panelUsuario.pack_propagate(False)
        panelInformacion.pack(expand = True, fill = "x")
        panelInformacion.pack_propagate(False)


        #Ícono para volver atrás
        iconBack = CTkImage(dark_image= Image.open("BackSymbol1.png"), size = (51,51))
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white", command =lambda: self.controller.show_frame(GestionarUsuariosPrincipal))
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white", command = lambda: self.controller.show_frame(PantallaPerfil.PantallaPerfilEmpleado))
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Título Grande de la Ventana

        textoPrincipal = bigText(panelInformacion, "Añadir Usuario")
        textoPrincipal.pack(anchor = "nw", padx = 50)

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        #Paneles de Formulario - 1

        panel1 = CTkFrame(panelScrollable, fg_color = "transparent")
        panel1.pack(anchor = "nw", pady = 30, fill = "x")

        nombre = formularioSimple(panel1, "Nombre")
        nombre.pack(side = "left", padx = 32)

        ciudad = formularioSimple(panel1, "Ciudad")
        ciudad.pack(side = "right", padx = 32)


        #Paneles de Formulario - 2

        panel2 = CTkFrame(panelScrollable, fg_color = "transparent")
        panel2.pack(anchor = "nw", pady = 30, fill = "x")

        apellido1 = formularioSimple(panel2, "Apellido 1")
        apellido1.pack(side = "left", padx = 32)

        apellido2 = formularioSimple(panel2, "Apellido 2")
        apellido2.pack(side = "right", padx = 32)

        #Paneles de Formulario - 3

        panel3 = CTkFrame(panelScrollable, fg_color = "transparent")
        panel3.pack(anchor = "nw", pady = 30, fill = "x")

        usuario = formularioSimple(panel3, "Usuario")
        usuario.pack(side = "left", padx = 32)

        contrasena = formularioSimple(panel3, "Contraseña")
        contrasena.pack(side = "right", padx = 32)

        #Botón para completar acción

        botonEnviar = botonAccion(panelScrollable, "Añadir Usuario", 33, "verde", 370, 60, lambda: ejecutarAnadirUsuario())
        botonEnviar.pack(expand = True, pady = 30)


        def ejecutarAnadirUsuario():
            
            nombreQuery = nombre.entradaTexto.get()
            ciudadQuery = ciudad.entradaTexto.get()
            apellido1Query = apellido1.entradaTexto.get()
            apellido2Query = apellido2.entradaTexto.get()
            usuarioQuery = usuario.entradaTexto.get()
            contrasenaQuery = contrasena.entradaTexto.get()

            if not nombreQuery.strip() or not ciudadQuery.strip() or not apellido1Query.strip() or not apellido2Query.strip() or not usuarioQuery.strip() or not contrasenaQuery.strip():
                messagebox.showerror("Error", "Alguno de los campos se encuentra vacío")
            else: 
                conexion = conectarMySql.MiConexion()
                conexion.anade_usuario(0,nombreQuery,ciudadQuery,apellido1Query,apellido2Query,usuarioQuery,contrasenaQuery,  None)

                conexion.conexion.close()

                self.controller.show_frame(PantallaPrincipalEmpleado.MenuPrincipalUsuario)

            

class AnadirUsuarioEmpleado(CTkFrame):
    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

        self.controller = controller

        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)



        # Crear canvas para manejar la imagen y el texto
        canvas = tk.Canvas(self, width=640, height=721, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        #Imagen de Fondo
        self.img_fondo = tk.PhotoImage(file="FondoDegradadoMain.png")  # Mantener referencia a la imagen
        canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")  # Colocar la imagen en la esquina superior izquierda     


        frameBlancoFondo = CTkFrame(
            canvas,
            bg_color= "white",
            fg_color= "white",
            corner_radius=20,
            width=1200,
            height=600,
        )

        frameBlancoFondo.pack(expand = True)
        frameBlancoFondo.pack_propagate(False)


        panelUsuario = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 90                  
        )


        panelInformacion = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 510
                     
        )


        #Dividir la pantalla en 2 paneles distintos
        panelUsuario.pack(expand = True, fill = "x")
        panelUsuario.pack_propagate(False)
        panelInformacion.pack(expand = True, fill = "x")
        panelInformacion.pack_propagate(False)


        #Ícono para volver atrás
        iconBack = CTkImage(dark_image= Image.open("BackSymbol1.png"), size = (51,51))
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white", command =lambda: self.controller.show_frame(GestionarUsuariosPrincipal))
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white", command = lambda: self.controller.show_frame(PantallaPerfil.PantallaPerfilEmpleado))
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Título Grande de la Ventana

        textoPrincipal = bigText(panelInformacion, "Añadir Usuario")
        textoPrincipal.pack(anchor = "nw", padx = 50)

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        #Paneles de Formulario - 1

        panel1 = CTkFrame(panelScrollable, fg_color = "transparent")
        panel1.pack(anchor = "nw", pady = 30, fill = "x")

        nombre = formularioSimple(panel1, "Nombre")
        nombre.pack(side = "left", padx = 32)

        ciudad = formularioSimple(panel1, "Ciudad")
        ciudad.pack(side = "right", padx = 32)


        #Paneles de Formulario - 2

        panel2 = CTkFrame(panelScrollable, fg_color = "transparent")
        panel2.pack(anchor = "nw", pady = 30, fill = "x")

        apellido1 = formularioSimple(panel2, "Apellido 1")
        apellido1.pack(side = "left", padx = 32)

        apellido2 = formularioSimple(panel2, "Apellido 2")
        apellido2.pack(side = "right", padx = 32)

        #Paneles de Formulario - 3

        panel3 = CTkFrame(panelScrollable, fg_color = "transparent")
        panel3.pack(anchor = "nw", pady = 30, fill = "x")

        usuario = formularioSimple(panel3, "Usuario")
        usuario.pack(side = "left", padx = 32)

        contrasena = formularioSimple(panel3, "Contraseña")
        contrasena.pack(side = "right", padx = 32)

        #Paneles de Formulario - 4

        panel4 = CTkFrame(panelScrollable, fg_color = "transparent")
        panel4.pack(anchor = "nw", pady = 30, fill = "x")

        nivelAcceso = formularioSimple(panel4, "Nivel de Acceso")
        nivelAcceso.pack(side = "left", padx = 32)

        #Botón para completar acción

        botonEnviar = botonAccion(panelScrollable, "Añadir Usuario", 33, "verde", 370, 60, lambda: ejecutarAnadirUsuario())
        botonEnviar.pack(expand = True, pady = 30)


        def ejecutarAnadirUsuario():
            
            nombreQuery = nombre.entradaTexto.get()
            ciudadQuery = ciudad.entradaTexto.get()
            apellido1Query = apellido1.entradaTexto.get()
            apellido2Query = apellido2.entradaTexto.get()
            usuarioQuery = usuario.entradaTexto.get()
            contrasenaQuery = contrasena.entradaTexto.get()
            nivelAccesoQuery = nivelAcceso.entradaTexto.get()


            if not nombreQuery.strip() or not ciudadQuery.strip() or not apellido1Query.strip() or not apellido2Query.strip() or not usuarioQuery.strip() or not contrasenaQuery.strip() or not nivelAccesoQuery.strip():
                messagebox.showerror("Error", "Alguno de los campos se encuentra vacío")

            else: 
                conexion = conectarMySql.MiConexion()
                conexion.anade_usuario(1,nombreQuery,ciudadQuery,apellido1Query,apellido2Query,usuarioQuery,contrasenaQuery,nivelAccesoQuery)

                conexion.conexion.close()

                self.controller.show_frame(PantallaPrincipalEmpleado.MenuPrincipalUsuario)
 
         



class ModificarUsuarioAspirante(CTkFrame):

    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

        self.controller = controller

        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)



        # Crear canvas para manejar la imagen y el texto
        canvas = tk.Canvas(self, width=640, height=721, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        #Imagen de Fondo
        self.img_fondo = tk.PhotoImage(file="FondoDegradadoMain.png")  # Mantener referencia a la imagen
        canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")  # Colocar la imagen en la esquina superior izquierda     


        frameBlancoFondo = CTkFrame(
            canvas,
            bg_color= "white",
            fg_color= "white",
            corner_radius=20,
            width=1200,
            height=600,
        )

        frameBlancoFondo.pack(expand = True)
        frameBlancoFondo.pack_propagate(False)


        panelUsuario = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 90                  
        )


        panelInformacion = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 510
                     
        )


        #Dividir la pantalla en 2 paneles distintos
        panelUsuario.pack(expand = True, fill = "x")
        panelUsuario.pack_propagate(False)
        panelInformacion.pack(expand = True, fill = "x")
        panelInformacion.pack_propagate(False)


        #Ícono para volver atrás
        iconBack = CTkImage(dark_image= Image.open("BackSymbol1.png"), size = (51,51))
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white", command =lambda: self.controller.show_frame(GestionarUsuariosPrincipal))
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white", command =lambda: self.controller.show_frame(PantallaPerfil.PantallaPerfilEmpleado))
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Título Grande de la Ventana

        panelTitulo = CTkFrame(panelInformacion, fg_color = "transparent", corner_radius=16)
        panelTitulo.pack(fill = "x")

        textoPrincipal = bigText(panelTitulo,"Modificar Usuario:")
        textoPrincipal.pack(side = "left", padx = 50)

        campoBusqueda = CTkEntry(panelTitulo, width = 250, height= 36, corner_radius=16, fg_color= "#DEEDFD", placeholder_text= "",  border_width=0, font=("Labrada", 20), justify="center")

        botonBuscar = botonAccion(panelTitulo, "Buscar", 26, "verde", 135, 35, lambda: realizarBusqueda(campoBusqueda.get()))
        botonBuscar.pack(side = "right", padx = 20)

        campoBusqueda = CTkEntry(panelTitulo, width = 250, height= 36, corner_radius=16, fg_color= "#DEEDFD", placeholder_text= "",  border_width=0, font=("Labrada", 20), justify="center")
        campoBusqueda.pack(side = "right", padx = 20)

        textoCodigo = mediumText(panelTitulo,"Código")
        textoCodigo.pack(side = "right", padx = 20)       

         

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        #Verificar si existe el usuario. Si existe, mostrar la información del mismo.

        def realizarBusqueda(id):

            if id.isdigit():
                conexion = conectarMySql.MiConexion()

                if conexion.existe_aspirante(id):

                    info = conexion.buscar_info_aspirante(id)

                    for widget in panelScrollable.winfo_children():
                        widget.destroy()

                    #Paneles de Formulario - 1

                    panel1 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel1.pack(anchor = "nw", pady = 30, fill = "x")

                    nombre = formularioSimple(panel1, "Nombre")
                    nombre.entradaTexto.configure(placeholder_text = info[2])
                    nombre.pack(side = "left", padx = 32)

                    ciudad = formularioSimple(panel1, "Ciudad")
                    ciudad.entradaTexto.configure(placeholder_text = info[5])
                    ciudad.pack(side = "right", padx = 32)


                    #Paneles de Formulario - 2

                    panel2 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel2.pack(anchor = "nw", pady = 30, fill = "x")

                    apellido1 = formularioSimple(panel2, "Apellido 1")
                    apellido1.entradaTexto.configure(placeholder_text = info[3])
                    apellido1.pack(side = "left", padx = 32)

                    apellido2 = formularioSimple(panel2, "Apellido 2")
                    apellido2.entradaTexto.configure(placeholder_text = info[4])
                    apellido2.pack(side = "right", padx = 32)

                    #Paneles de Formulario - 3

                    panel3 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel3.pack(anchor = "nw", pady = 30, fill = "x")

                    usuario = formularioSimple(panel3, "Usuario")
                    usuario.entradaTexto.configure(placeholder_text = info[0])
                    usuario.pack(side = "left", padx = 32)


                    contrasena = formularioSimple(panel3, "Contraseña")
                    contrasena.entradaTexto.configure(placeholder_text = info[1])
                    contrasena.pack(side = "right", padx = 32)



                    #Botón para completar acción

                    botonEnviar = botonAccion(panelScrollable, "Modificar Usuario", 33, "verde", 370, 60, lambda: ejecutarModificarUsuario())
                    botonEnviar.pack(expand = True, pady = 30)


                    def ejecutarModificarUsuario():


                        if nombre.entradaTexto.get() != "":
                            nombreQuery = nombre.entradaTexto.get()
                        else:
                            nombreQuery = info[2]

                        if ciudad.entradaTexto.get() != "":
                            ciudadQuery = ciudad.entradaTexto.get()
                        else:
                            ciudadQuery = info[5]

                        if apellido1.entradaTexto.get() != "":
                            apellido1Query = apellido1.entradaTexto.get()
                        else:
                            apellido1Query = info[3]

                        if apellido2.entradaTexto.get() != "":
                            apellido2Query = apellido2.entradaTexto.get()
                        else:
                            apellido2Query = info[4]

                        if usuario.entradaTexto.get() != "":
                            usuarioQuery = usuario.entradaTexto.get()
                        else:
                            usuarioQuery = info[0]

                        if contrasena.entradaTexto.get() != "":
                            contrasenaQuery = contrasena.entradaTexto.get()
                        else:
                            contrasenaQuery = info[1]

                    

                        
                        conexion = conectarMySql.MiConexion()
                        conexion.modificar_usuario(0, nombreQuery, ciudadQuery, apellido1Query, apellido2Query, usuarioQuery, contrasenaQuery, None, id)

                        conexion.conexion.close()

                        self.controller.show_frame(PantallaPrincipalEmpleado.MenuPrincipalUsuario)
                                
                        

                else: messagebox.showerror("Error", "El código ingresado no existe")
                

            else: 
                messagebox.showerror("Error", "No ingresó un código válido")

    


        

class ModificarUsuarioEmpleado(CTkFrame):

    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

        self.controller = controller

        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)



        # Crear canvas para manejar la imagen y el texto
        canvas = tk.Canvas(self, width=640, height=721, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        #Imagen de Fondo
        self.img_fondo = tk.PhotoImage(file="FondoDegradadoMain.png")  # Mantener referencia a la imagen
        canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")  # Colocar la imagen en la esquina superior izquierda     


        frameBlancoFondo = CTkFrame(
            canvas,
            bg_color= "white",
            fg_color= "white",
            corner_radius=20,
            width=1200,
            height=600,
        )

        frameBlancoFondo.pack(expand = True)
        frameBlancoFondo.pack_propagate(False)


        panelUsuario = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 90                  
        )


        panelInformacion = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 510
                     
        )


        #Dividir la pantalla en 2 paneles distintos
        panelUsuario.pack(expand = True, fill = "x")
        panelUsuario.pack_propagate(False)
        panelInformacion.pack(expand = True, fill = "x")
        panelInformacion.pack_propagate(False)


        #Ícono para volver atrás
        iconBack = CTkImage(dark_image= Image.open("BackSymbol1.png"), size = (51,51))
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white", command =lambda: self.controller.show_frame(GestionarUsuariosPrincipal))
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white", command =lambda: self.controller.show_frame(PantallaPerfil.PantallaPerfilEmpleado))
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Título Grande de la Ventana

        panelTitulo = CTkFrame(panelInformacion, fg_color = "transparent", corner_radius=16)
        panelTitulo.pack(fill = "x")

        textoPrincipal = bigText(panelTitulo,"Modificar Usuario:")
        textoPrincipal.pack(side = "left", padx = 50)

        botonBuscar = botonAccion(panelTitulo, "Buscar", 26, "verde", 135, 35, lambda: realizarBusqueda(campoBusqueda.get()))
        botonBuscar.pack(side = "right", padx = 20)

        campoBusqueda = CTkEntry(panelTitulo, width = 250, height= 36, corner_radius=16, fg_color= "#DEEDFD", placeholder_text= "",  border_width=0, font=("Labrada", 20), justify="center")
        campoBusqueda.pack(side = "right", padx = 20)

        textoCodigo = mediumText(panelTitulo,"Código")
        textoCodigo.pack(side = "right", padx = 20)       

         

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        #Verificar si existe el usuario. Si existe, mostrar la información del mismo.

        def realizarBusqueda(id):

            if id.isdigit():
                conexion = conectarMySql.MiConexion()

                if conexion.existe_empleado(id):

                    info = conexion.buscar_info_empleado(id)

                    for widget in panelScrollable.winfo_children():
                        widget.destroy()

                    #Paneles de Formulario - 1

                    panel1 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel1.pack(anchor = "nw", pady = 30, fill = "x")

                    nombre = formularioSimple(panel1, "Nombre")
                    nombre.entradaTexto.configure(placeholder_text = info[2])
                    nombre.pack(side = "left", padx = 32)

                    ciudad = formularioSimple(panel1, "Ciudad")
                    ciudad.entradaTexto.configure(placeholder_text = info[5])
                    ciudad.pack(side = "right", padx = 32)


                    #Paneles de Formulario - 2

                    panel2 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel2.pack(anchor = "nw", pady = 30, fill = "x")

                    apellido1 = formularioSimple(panel2, "Apellido 1")
                    apellido1.entradaTexto.configure(placeholder_text = info[3])
                    apellido1.pack(side = "left", padx = 32)

                    apellido2 = formularioSimple(panel2, "Apellido 2")
                    apellido2.entradaTexto.configure(placeholder_text = info[4])
                    apellido2.pack(side = "right", padx = 32)

                    #Paneles de Formulario - 3

                    panel3 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel3.pack(anchor = "nw", pady = 30, fill = "x")

                    usuario = formularioSimple(panel3, "Usuario")
                    usuario.entradaTexto.configure(placeholder_text = info[0])
                    usuario.pack(side = "left", padx = 32)


                    contrasena = formularioSimple(panel3, "Contraseña")
                    contrasena.entradaTexto.configure(placeholder_text = info[1])
                    contrasena.pack(side = "right", padx = 32)

                    #Paneles de Formulario - 4

                    panel4 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel4.pack(anchor = "nw", pady = 30, fill = "x")

                    nivelAcceso = formularioSimple(panel4, "Nivel de Acceso")
                    nivelAcceso.entradaTexto.configure(placeholder_text = info[6])
                    nivelAcceso.pack(side = "left", padx = 32)

                    #Botón para completar acción

                    botonEnviar = botonAccion(panelScrollable, "Modificar Usuario", 33, "verde", 370, 60, lambda: ejecutarModificarUsuario())
                    botonEnviar.pack(expand = True, pady = 30)


                    def ejecutarModificarUsuario():


                        if nombre.entradaTexto.get() != "":
                            nombreQuery = nombre.entradaTexto.get()
                        else:
                            nombreQuery = info[2]

                        if ciudad.entradaTexto.get() != "":
                            ciudadQuery = ciudad.entradaTexto.get()
                        else:
                            ciudadQuery = info[5]

                        if apellido1.entradaTexto.get() != "":
                            apellido1Query = apellido1.entradaTexto.get()
                        else:
                            apellido1Query = info[3]

                        if apellido2.entradaTexto.get() != "":
                            apellido2Query = apellido2.entradaTexto.get()
                        else:
                            apellido2Query = info[4]

                        if usuario.entradaTexto.get() != "":
                            usuarioQuery = usuario.entradaTexto.get()
                        else:
                            usuarioQuery = info[0]

                        if contrasena.entradaTexto.get() != "":
                            contrasenaQuery = contrasena.entradaTexto.get()
                        else:
                            contrasenaQuery = info[1]

                        if nivelAcceso.entradaTexto.get() != "":
                            nivelAccesoQuery = nivelAcceso.entradaTexto.get()
                        else:
                            nivelAccesoQuery = info[6]

        

                        
                        conexion = conectarMySql.MiConexion()
                        conexion.modificar_usuario(1, nombreQuery, ciudadQuery, apellido1Query, apellido2Query, usuarioQuery, contrasenaQuery, nivelAccesoQuery, id)

                        conexion.conexion.close()

                        self.controller.show_frame(PantallaPrincipalEmpleado.MenuPrincipalUsuario)
                                
                        

                else: messagebox.showerror("Error", "El código ingresado no existe")
                

            else: 
                messagebox.showerror("Error", "No ingresó un código válido")



class EliminarUsuarioAspirante(CTkFrame):

    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

        self.controller = controller

        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)



        # Crear canvas para manejar la imagen y el texto
        canvas = tk.Canvas(self, width=640, height=721, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        #Imagen de Fondo
        self.img_fondo = tk.PhotoImage(file="FondoDegradadoMain.png")  # Mantener referencia a la imagen
        canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")  # Colocar la imagen en la esquina superior izquierda     


        frameBlancoFondo = CTkFrame(
            canvas,
            bg_color= "white",
            fg_color= "white",
            corner_radius=20,
            width=1200,
            height=600,
        )

        frameBlancoFondo.pack(expand = True)
        frameBlancoFondo.pack_propagate(False)


        panelUsuario = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 90                  
        )


        panelInformacion = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 510
                     
        )


        #Dividir la pantalla en 2 paneles distintos
        panelUsuario.pack(expand = True, fill = "x")
        panelUsuario.pack_propagate(False)
        panelInformacion.pack(expand = True, fill = "x")
        panelInformacion.pack_propagate(False)


        #Ícono para volver atrás
        iconBack = CTkImage(dark_image= Image.open("BackSymbol1.png"), size = (51,51))
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white", command = lambda: self.controller.show_frame(GestionarUsuariosPrincipal))
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white", command =lambda: self.controller.show_frame(PantallaPerfil.PantallaPerfilEmpleado))
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Título Grande de la Ventana

        panelTitulo = CTkFrame(panelInformacion, fg_color = "transparent", corner_radius=16)
        panelTitulo.pack(fill = "x")

        textoPrincipal = bigText(panelTitulo,"Modificar Usuario:")
        textoPrincipal.pack(side = "left", padx = 50)

        botonBuscar = botonAccion(panelTitulo, "Buscar", 26, "verde", 135, 35, lambda: realizarBusqueda(campoBusqueda.get()))
        botonBuscar.pack(side = "right", padx = 20)

        campoBusqueda = CTkEntry(panelTitulo, width = 250, height= 36, corner_radius=16, fg_color= "#DEEDFD", placeholder_text= "",  border_width=0, font=("Labrada", 20), justify="center")
        campoBusqueda.pack(side = "right", padx = 20)

        textoCodigo = mediumText(panelTitulo,"Código")
        textoCodigo.pack(side = "right", padx = 20)       

         

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        #Verificar si existe el usuario. Si existe, mostrar la información del mismo.

        def realizarBusqueda(id):

            if id.isdigit():
                conexion = conectarMySql.MiConexion()

                if conexion.existe_aspirante(id):

                    info = conexion.buscar_info_aspirante(id)

                    for widget in panelScrollable.winfo_children():
                        widget.destroy()

                    #Paneles de Formulario - 1

                    panel1 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel1.pack(anchor = "nw", pady = 30, fill = "x")

                    nombre = formularioSimple(panel1, "Nombre")
                    nombre.entradaTexto.configure(placeholder_text = info[2])
                    nombre.entradaTexto.configure(state = "disabled")
                    nombre.pack(side = "left", padx = 32)

                    ciudad = formularioSimple(panel1, "Ciudad")
                    ciudad.entradaTexto.configure(placeholder_text = info[5])
                    ciudad.entradaTexto.configure(state = "disabled")
                    ciudad.pack(side = "right", padx = 32)


                    #Paneles de Formulario - 2

                    panel2 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel2.pack(anchor = "nw", pady = 30, fill = "x")

                    apellido1 = formularioSimple(panel2, "Apellido 1")
                    apellido1.entradaTexto.configure(placeholder_text = info[3])
                    apellido1.entradaTexto.configure(state = "disabled")
                    apellido1.pack(side = "left", padx = 32)

                    apellido2 = formularioSimple(panel2, "Apellido 2")
                    apellido2.entradaTexto.configure(placeholder_text = info[4])
                    apellido2.entradaTexto.configure(state = "disabled")
                    apellido2.pack(side = "right", padx = 32)

                    #Paneles de Formulario - 3

                    panel3 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel3.pack(anchor = "nw", pady = 30, fill = "x")

                    usuario = formularioSimple(panel3, "Usuario")
                    usuario.entradaTexto.configure(placeholder_text = info[0])
                    usuario.entradaTexto.configure(state = "disabled")
                    usuario.pack(side = "left", padx = 32)


                    contrasena = formularioSimple(panel3, "Contraseña")
                    contrasena.entradaTexto.configure(placeholder_text = info[1])
                    contrasena.entradaTexto.configure(state = "disabled")
                    contrasena.pack(side = "right", padx = 32)



                    #Botón para completar acción

                    botonEnviar = botonAccion(panelScrollable, "Eliminar Usuario", 33, "verde", 370, 60, lambda: ejecutarEliminarUsuario())
                    botonEnviar.pack(expand = True, pady = 30)


                    def ejecutarEliminarUsuario():

                        
                        conexion = conectarMySql.MiConexion()

                        if messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas continuar?"):
                            conexion.eliminarUsuarioAspirante(0, id)
                            conexion.conexion.close()
                            self.controller.show_frame(PantallaPrincipalEmpleado.MenuPrincipalUsuario)
                        else: 
                            conexion.conexion.close()
                             
                        

                else: messagebox.showerror("Error", "El código ingresado no existe")
                

            else: 
                messagebox.showerror("Error", "No ingresó un código válido")

class EliminarUsuarioEmpleado(CTkFrame):

    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

        self.controller = controller

        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)



        # Crear canvas para manejar la imagen y el texto
        canvas = tk.Canvas(self, width=640, height=721, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        #Imagen de Fondo
        self.img_fondo = tk.PhotoImage(file="FondoDegradadoMain.png")  # Mantener referencia a la imagen
        canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")  # Colocar la imagen en la esquina superior izquierda     


        frameBlancoFondo = CTkFrame(
            canvas,
            bg_color= "white",
            fg_color= "white",
            corner_radius=20,
            width=1200,
            height=600,
        )

        frameBlancoFondo.pack(expand = True)
        frameBlancoFondo.pack_propagate(False)


        panelUsuario = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 90                  
        )


        panelInformacion = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 510
                     
        )


        #Dividir la pantalla en 2 paneles distintos
        panelUsuario.pack(expand = True, fill = "x")
        panelUsuario.pack_propagate(False)
        panelInformacion.pack(expand = True, fill = "x")
        panelInformacion.pack_propagate(False)


        #Ícono para volver atrás
        iconBack = CTkImage(dark_image= Image.open("BackSymbol1.png"), size = (51,51))
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white", command = lambda: self.controller.show_frame(GestionarUsuariosPrincipal))
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white", command =lambda: self.controller.show_frame(PantallaPerfil.PantallaPerfilEmpleado))
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Título Grande de la Ventana

        panelTitulo = CTkFrame(panelInformacion, fg_color = "transparent", corner_radius=16)
        panelTitulo.pack(fill = "x")

        textoPrincipal = bigText(panelTitulo,"Modificar Usuario:")
        textoPrincipal.pack(side = "left", padx = 50)

        botonBuscar = botonAccion(panelTitulo, "Buscar", 26, "verde", 135, 35, lambda: realizarBusqueda(campoBusqueda.get()))
        botonBuscar.pack(side = "right", padx = 20)

        campoBusqueda = CTkEntry(panelTitulo, width = 250, height= 36, corner_radius=16, fg_color= "#DEEDFD", placeholder_text= "",  border_width=0, font=("Labrada", 20), justify="center")
        campoBusqueda.pack(side = "right", padx = 20)

        textoCodigo = mediumText(panelTitulo,"Código")
        textoCodigo.pack(side = "right", padx = 20)       

         

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        #Verificar si existe el usuario. Si existe, mostrar la información del mismo.

        def realizarBusqueda(id):

            if id.isdigit():
                conexion = conectarMySql.MiConexion()

                if conexion.existe_empleado(id):

                    info = conexion.buscar_info_empleado(id)

                    for widget in panelScrollable.winfo_children():
                        widget.destroy()

                    #Paneles de Formulario - 1

                    panel1 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel1.pack(anchor = "nw", pady = 30, fill = "x")

                    nombre = formularioSimple(panel1, "Nombre")
                    nombre.entradaTexto.configure(placeholder_text = info[2])
                    nombre.entradaTexto.configure(state = "disabled")
                    nombre.pack(side = "left", padx = 32)

                    ciudad = formularioSimple(panel1, "Ciudad")
                    ciudad.entradaTexto.configure(placeholder_text = info[5])
                    ciudad.entradaTexto.configure(state = "disabled")
                    ciudad.pack(side = "right", padx = 32)


                    #Paneles de Formulario - 2

                    panel2 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel2.pack(anchor = "nw", pady = 30, fill = "x")

                    apellido1 = formularioSimple(panel2, "Apellido 1")
                    apellido1.entradaTexto.configure(placeholder_text = info[3])
                    apellido1.entradaTexto.configure(state = "disabled")
                    apellido1.pack(side = "left", padx = 32)

                    apellido2 = formularioSimple(panel2, "Apellido 2")
                    apellido2.entradaTexto.configure(placeholder_text = info[4])
                    apellido2.entradaTexto.configure(state = "disabled")
                    apellido2.pack(side = "right", padx = 32)

                    #Paneles de Formulario - 3

                    panel3 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel3.pack(anchor = "nw", pady = 30, fill = "x")

                    usuario = formularioSimple(panel3, "Usuario")
                    usuario.entradaTexto.configure(placeholder_text = info[0])
                    usuario.entradaTexto.configure(state = "disabled")
                    usuario.pack(side = "left", padx = 32)


                    contrasena = formularioSimple(panel3, "Contraseña")
                    contrasena.entradaTexto.configure(placeholder_text = info[1])
                    contrasena.entradaTexto.configure(state = "disabled")
                    contrasena.pack(side = "right", padx = 32)

                    #Paneles de Formulario - 4

                    panel4 = CTkFrame(panelScrollable, fg_color = "transparent")
                    panel4.pack(anchor = "nw", pady = 30, fill = "x")

                    nivelAcceso = formularioSimple(panel4, "Nivel de Acceso")
                    nivelAcceso.entradaTexto.configure(placeholder_text = info[6])
                    nivelAcceso.entradaTexto.configure(state = "disabled")
                    nivelAcceso.pack(side = "left", padx = 32)



                    #Botón para completar acción

                    botonEnviar = botonAccion(panelScrollable, "Eliminar Usuario", 33, "verde", 370, 60, lambda: ejecutarEliminarUsuario())
                    botonEnviar.pack(expand = True, pady = 30)


                    def ejecutarEliminarUsuario():

                        
                        conexion = conectarMySql.MiConexion()

                        if messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas continuar?"):
                            conexion.eliminarUsuarioAspirante(1, id)
                            conexion.conexion.close()
                            self.controller.show_frame(PantallaPrincipalEmpleado.MenuPrincipalUsuario)
                        else: 
                            conexion.conexion.close()
                             
                        

                else: messagebox.showerror("Error", "El código ingresado no existe")
                

            else: 
                messagebox.showerror("Error", "No ingresó un código válido")



