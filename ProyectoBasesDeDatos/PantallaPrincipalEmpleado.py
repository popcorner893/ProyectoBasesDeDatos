from customtkinter import *
import tkinter as tk
from PIL import Image
from Utilidades import *


class MenuPrincipalUsuario(CTkFrame):

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

        #Panel de Información, Scrollable

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="transparent")
        panelScrollable.pack(expand = True, fill = "both")


        #Mensaje de Bienvenida
        bienvenidaTexto = bigText(panelScrollable,"BIENVENIDO, _nombre_usuario")
        bienvenidaTexto.pack(anchor = "nw", padx = 50)

        #Qué desea hacer?

        queDeseaTexto = mediumText(panelScrollable, "¿Qué desea hacer?")
        queDeseaTexto.pack(anchor = "nw", padx = 50)

        #Primer Panel de Opciones
        panelOpciones1 = CTkFrame(panelScrollable, fg_color="transparent", corner_radius= 16, height = 400)
        panelOpciones1.pack(expand = True, fill = "x", padx = 50, pady = 20)
        panelOpciones1.pack_propagate(False)

        #División de Paneles


        panelIzquierdo1 = frameOpcion(panelOpciones1, "Abrir Convocatoria", "AbrirConvocatoriaIcon")
        panelIzquierdo1.pack(expand = True, side = "left")
        panelIzquierdo1.pack_propagate(False)

        panelDerecho1 = frameOpcion(panelOpciones1, "Evaluar Inscripciones", "EvaluarInscripcionesIcon")
        panelDerecho1.pack(expand = True, side = "left")
        panelDerecho1.pack_propagate(False)

        #Segundo Panel de Opciones
        panelOpciones2 = CTkFrame(panelScrollable, fg_color="transparent", corner_radius= 16, height = 400)
        panelOpciones2.pack(expand = True, fill = "x", padx = 50, pady = 20)
        panelOpciones2.pack_propagate(False)

        #División de Paneles 2


        panelIzquierdo2 = frameOpcion(panelOpciones2, "Resolver Reclamaciones", "ResolverReclamacionesIcon")
        panelIzquierdo2.pack(expand = True, side = "left")
        panelIzquierdo2.pack_propagate(False)

        panelDerecho2 = frameOpcion(panelOpciones2, "Realizar Evaluación", "RealizarEvaluacionIcon")
        panelDerecho2.pack(expand = True, side = "left")
        panelDerecho2.pack_propagate(False)


        #Tercer Panel de Opciones
        panelOpciones3 = CTkFrame(panelScrollable, fg_color="transparent", corner_radius= 16, height = 400)
        panelOpciones3.pack(expand = True, fill = "x", padx = 50, pady = 20)
        panelOpciones3.pack_propagate(False)

        #División de Paneles 2


        panelIzquierdo3 = frameOpcion(panelOpciones3, "Gestionar Usuarios", "GestionarUsuariosIcon")
        panelIzquierdo3.pack(expand = True, side = "left")
        panelIzquierdo3.pack_propagate(False)

        panelDerecho3 = frameOpcion(panelOpciones3, "Finalizar Convocatoria", "FinalizarConvocatoriaIcon")
        panelDerecho3.pack(expand = True, side = "left")
        panelDerecho3.pack_propagate(False)



class frameOpcion(CTkFrame):

    def __init__(self, parent, titulo, dir):
        
        super().__init__(parent, fg_color="#DEEDFD", corner_radius= 16, width = 530, height = 340) 

    
        botonDescripcion = botonAccion(self, titulo, 33, "verde", 530, 70, lambda: None)
        botonDescripcion.pack(side = "bottom")

        img = icono(self, dir, 300, 258)
        img.pack(side = "bottom", pady = 10)