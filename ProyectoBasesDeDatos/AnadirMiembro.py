from customtkinter import *
import tkinter as tk
from PIL import Image
from Utilidades import *


class AnadirMiembro(CTkFrame):


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

        textoPrincipal = bigText(panelTitulo,"Añadir Miembros al Comité de Evaluación")
        textoPrincipal.pack(side = "left", padx = 50)
        

        #Panel de Información

        panelPrincipal = CTkFrame(panelInformacion, fg_color = "#DEEDFD", width = 1120, height = 420, corner_radius=16)
        panelPrincipal.pack(expand = True)
        panelPrincipal.pack_propagate(False)


        #Contenido del Panel

        descripcion = mediumText(panelPrincipal,"Código de Empleado:")
        descripcion.pack(anchor = "nw", padx = 20)

        entradaTexto = CTkEntry(panelPrincipal, width = 500, height = 55, corner_radius= 16, border_width=0, fg_color= "white", font = (("Labrada", 20)), justify = "left")
        entradaTexto.pack(anchor = "nw", padx = 20, pady = 10)

        #Botón para Enviar

        botonAnadir = botonAccion(panelPrincipal, "Añadir al Comité de Evaluación", 20, "verde", 360, 35, lambda: None)
        botonAnadir.pack(anchor = "nw", padx = 30, pady = 20)