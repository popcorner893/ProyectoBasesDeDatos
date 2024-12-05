from customtkinter import *
import tkinter as tk
from PIL import Image
from Utilidades import *


class GestionarUsuariosPrincipal(CTkFrame):

    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

        
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
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white")
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white")
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

        botonAgregarEmpleado = botonAccion(panelAgregar, "Empleado", 25, "verde", 60, 34, lambda: None)
        botonAgregarEmpleado.pack(side = "right", padx = 10)

        botonAgregarAspirante = botonAccion(panelAgregar, "Aspirante", 25, "verde", 60, 34, lambda: None)
        botonAgregarAspirante.pack(side = "right", padx = 10)



        #Modificar Usuario 

        panelModificar = CTkFrame(panelPrincipal, fg_color= "#DEEDFD", corner_radius=16, height = 80)
        panelModificar.pack(anchor = "nw", fill = "x")
        panelModificar.pack_propagate(False)

        textoModificar = mediumText(panelModificar, "Modificar Usuario")
        textoModificar.pack(side = "left", padx = 10)

        botonModificarEmpleado = botonAccion(panelModificar, "Empleado", 25, "verde", 60, 34, lambda: None)
        botonModificarEmpleado.pack(side = "right", padx = 10)

        botonModificarAspirante = botonAccion(panelModificar, "Aspirante", 25, "verde", 60, 34, lambda: None)
        botonModificarAspirante.pack(side = "right", padx = 10)


        #Eliminar Usuario 

        panelEliminar = CTkFrame(panelPrincipal, fg_color= "#DEEDFD", corner_radius=16, height = 80)
        panelEliminar.pack(anchor = "nw", fill = "x", pady = 20)
        panelEliminar.pack_propagate(False)

        textoEliminar = mediumText(panelEliminar, "Eliminar Usuario")
        textoEliminar.pack(side = "left", padx = 10)

        botonEliminarEmpleado = botonAccion(panelEliminar, "Empleado", 25, "verde", 60, 34, lambda: None)
        botonEliminarEmpleado.pack(side = "right", padx = 10)

        botonEliminarAspirante = botonAccion(panelEliminar, "Aspirante", 25, "verde", 60, 34, lambda: None)
        botonEliminarAspirante.pack(side = "right", padx = 10)


class AnadirUsuario(CTkFrame):
    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

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
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white")
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white")
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

        #Botón para completar acción

        botonEnviar = botonAccion(panelScrollable, "Añadir Usuario", 33, "verde", 370, 60, lambda: None)
        botonEnviar.pack(expand = True, pady = 30)


class ModificarUsuario(CTkFrame):

    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

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
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white")
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white")
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Título Grande de la Ventana

        panelTitulo = CTkFrame(panelInformacion, fg_color = "transparent", corner_radius=16)
        panelTitulo.pack(fill = "x")

        textoPrincipal = bigText(panelTitulo,"Modificar Usuario:")
        textoPrincipal.pack(side = "left", padx = 50)

        botonBuscar = botonAccion(panelTitulo, "Buscar", 26, "verde", 135, 35, lambda: None)
        botonBuscar.pack(side = "right", padx = 20)

        campoBusqueda = CTkEntry(panelTitulo, width = 250, height= 36, corner_radius=16, fg_color= "#DEEDFD", placeholder_text= "",  border_width=0, font=("Labrada", 20), justify="center")
        campoBusqueda.pack(side = "right", padx = 20)

        textoCodigo = mediumText(panelTitulo,"Código")
        textoCodigo.pack(side = "right", padx = 20)       

         

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

        #Botón para completar acción

        botonEnviar = botonAccion(panelScrollable, "Modificar Usuario", 33, "verde", 370, 60, lambda: None)
        botonEnviar.pack(expand = True, pady = 30)


class EliminarUsuario(CTkFrame):

    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

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
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white")
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white")
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Título Grande de la Ventana

        panelTitulo = CTkFrame(panelInformacion, fg_color = "transparent", corner_radius=16)
        panelTitulo.pack(fill = "x")

        textoPrincipal = bigText(panelTitulo,"Modificar Usuario:")
        textoPrincipal.pack(side = "left", padx = 50)

        botonBuscar = botonAccion(panelTitulo, "Buscar", 26, "verde", 135, 35, lambda: None)
        botonBuscar.pack(side = "right", padx = 20)

        campoBusqueda = CTkEntry(panelTitulo, width = 250, height= 36, corner_radius=16, fg_color= "#DEEDFD", placeholder_text= "",  border_width=0, font=("Labrada", 20), justify="center")
        campoBusqueda.pack(side = "right", padx = 20)

        textoCodigo = mediumText(panelTitulo,"Código")
        textoCodigo.pack(side = "right", padx = 20)       

         

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

        #Botón para completar acción

        botonEnviar = botonAccion(panelScrollable, "Eliminar Usuario", 33, "rojo", 370, 60, lambda: None)
        botonEnviar.pack(expand = True, pady = 30)




