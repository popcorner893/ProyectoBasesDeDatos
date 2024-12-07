from customtkinter import *
import tkinter as tk
from PIL import Image
from Utilidades import *
import PantallaPrincipalEmpleado, PantallaPerfil


class FinalizarConvocatoria (CTkFrame):

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


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white", command =lambda: self.controller.show_frame(PantallaPerfil.PantallaPerfilEmpleado))
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Títlo principal de Ventana

        abrirConvocatoria = bigText(panelInformacion, "Convocatorias Activas")
        abrirConvocatoria.pack(anchor = "nw", padx = 50)

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="transparent", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        #Paneles Colapsables - 1

        panelColapsable1 = CollapsiblePanel(panelScrollable, "nombre_convocatoria")
        panelColapsable1.pack(anchor = "nw",fill = "x", pady = 5)

        panelNombreImagen = CTkFrame(panelColapsable1.content_frame, fg_color = "transparent", bg_color= "transparent", corner_radius=16)
        panelNombreImagen.pack(anchor = "nw",fill = "x", pady = 5)

        nombrePublicacion = mediumText(panelNombreImagen, "Nombre Publicación")
        nombrePublicacion.pack(side = "left", padx = 50)

        imagenPubliacion = mediumText(panelNombreImagen, "Imagen Publicación")
        imagenPubliacion.pack(side = "right", padx = 100)

        panelDescripcion = CTkFrame(panelColapsable1.content_frame, fg_color = "transparent", bg_color= "transparent", corner_radius=16)
        panelDescripcion.pack(anchor = "nw",fill = "x", pady = 5)

        entradaNombre = CTkEntry(panelDescripcion, width = 500, height = 50, corner_radius= 16, border_width=0, fg_color= "white", font = (("Labrada", 20)), justify = "left")
        entradaNombre.pack(side = "left", pady = 10, padx = 50)

        botonSubir1 = botonAccion(panelDescripcion, "Subir Nuevo Archivo", 20, "verde", 320, 34, lambda: None)
        botonSubir1.pack(side = "right", padx = 20)

        iconoSubir1 = icono(panelDescripcion, "UploadIcon1", 30, 30)
        iconoSubir1.pack(side = "right", padx = 10)        

        textoPublicacion = mediumText(panelColapsable1.content_frame, "Texto Publicación")
        textoPublicacion.pack(anchor = "nw", padx= 60)

        entradaTexto = CTkEntry(panelColapsable1.content_frame, width = 1000, height = 120, corner_radius= 16, border_width=0, fg_color= "white", font = (("Labrada", 20)), justify = "left")
        entradaTexto.pack(anchor = "nw", padx = 70, pady = 10)

        #Botones

        panelBotones = CTkFrame(panelColapsable1.content_frame, fg_color = "transparent")
        panelBotones.pack(anchor = "nw", fill = "x", pady = 30)

        botonDesclararDesierto = botonAccion(panelBotones, "Declarar Desierto", 33, "rojo", 380, 70, lambda: None)
        botonDesclararDesierto.pack(side = "left", padx = 40)

        botonPublicar = botonAccion(panelBotones, "Publicar Resultados", 33, "verde", 380, 70, lambda: None)
        botonPublicar.pack(side = "right", padx = 40)