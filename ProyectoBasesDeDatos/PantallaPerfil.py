from customtkinter import *
import tkinter as tk
from PIL import Image
from Utilidades import *


class PantallaPerfil(CTkFrame):

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


        panelSuperior = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 70                  
        )


        panelInformacion = CTkFrame(
            frameBlancoFondo,
            fg_color= "transparent",
            height= 530
                     
        )


        #Dividir la pantalla en 2 paneles distintos
        panelSuperior.pack(expand = True, fill = "x")
        panelSuperior.pack_propagate(False)
        panelInformacion.pack(expand = True, fill = "x")
        panelInformacion.pack_propagate(False)


        #Ícono para volver atrás
        iconBack = iconoClickable(panelSuperior, "BackSymbol1", 51, 51, lambda: None)
        iconBack.pack(side = "left", padx = 20, pady = 10)

        #Panel de Usuario

        panelUsuario = CTkFrame(
            panelInformacion,
            fg_color= "transparent",
            height = 120                     
        )
        panelUsuario.pack(expand = True, fill = "x")

        #Panel de Info del Usuario Detallada

        panelInfoDetallada = CTkFrame(
            panelInformacion,
            fg_color= "transparent",                    
        )
        panelInfoDetallada.pack(expand = True, fill = "both")
        panelInfoDetallada.pack_propagate (False)


        #Panel del Usuario

        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemploGrande.png"), size = (130,130))
        img_lab1 = CTkLabel(panelUsuario, image=imagenUsuario, text="", bg_color="white", fg_color="white")
        img_lab1.pack(side = "left", padx = 60, pady = 10)

        panelNombre = CTkFrame(
            panelUsuario,
            fg_color= "transparent",                   
        )
        panelNombre.pack(side = "left", expand = True, fill = "x")

        #Etiquetas de nombres y nivel de acceso


        nombrePerfil = CTkLabel(panelNombre, text = "Nombre Usuario - Perfil", font=("Labrada", 40))
        nombrePerfil.pack(anchor = "nw")

        textoPublicacion = CTkLabel(panelNombre, text = "Aspirante / Nivel de Acceso", font=("Labrada", 20))
        textoPublicacion.pack(anchor = "nw", padx = 10)


        #Panel de Información Detallada del Usuario

        panelInfoDetallada.columnconfigure((0,1), weight=1)
        panelInfoDetallada.rowconfigure(0, weight=1)

        panelIzquierdo = CTkFrame(panelInfoDetallada,fg_color="transparent", corner_radius= 16)
        panelIzquierdo.grid(row = 0, column = 0, sticky = "nswe")

        panelDerecho = CTkFrame(panelInfoDetallada,fg_color="transparent", corner_radius= 16)
        panelDerecho.grid(row = 0, column = 1, sticky = "nswe")

        #Subpaneles para la info

        panelIzquierdo1 = CTkFrame(panelIzquierdo,fg_color="#F2F2F2", corner_radius= 16, width = 450, height = 320)
        panelIzquierdo1.pack(expand = True)
        panelIzquierdo1.pack_propagate(False)

        panelDerecho2 = CTkFrame(panelDerecho,fg_color="#F2F2F2", corner_radius= 16, width = 450, height = 320)
        panelDerecho2.pack(expand = True)
        panelDerecho2.pack_propagate(False)

        #Contenido del Panel Izquierdo
        #
        #

        paneltitulo = CTkFrame(panelIzquierdo1, fg_color="transparent")
        paneltitulo.pack(anchor = "nw")

        tituloInfo = mediumText(paneltitulo, "Información Personal")

        iconoUsuario = icono(paneltitulo,"iconoUsuarioSinColor",38,38)

        tituloInfo.pack(side = "left", padx = 10)
        iconoUsuario.pack(side = "left")


        #Sección del Nombre
        panelNombre1 = CTkFrame(panelIzquierdo1, fg_color="transparent")
        panelNombre1.pack(anchor = "nw", fill = "x")

        tituloNombre = smallText(panelNombre1, "Nombre")
        tituloNombre.pack(side = "left", padx = 30)


        nombreLabel = CTkEntry(
            panelIzquierdo1,
            placeholder_text= "Nombre",
            justify = CENTER,
            font= ("Labrada", 20),
            placeholder_text_color= "black",
            fg_color = "#F2F2F2",
            state= "normal",
            border_width=0
            )

        
        self.editando = False

        iconoLapiz1 = iconoClickable(panelNombre1, "PencilIcon", 29, 29, lambda: (
        nombreLabel.configure(state="normal") if self.editando else nombreLabel.configure(state="disabled", border_width=1),
        setattr(self, "editando", not self.editando)))  

        iconoLapiz1.pack(side = "left")
        nombreLabel.pack(anchor = "nw", padx = 20)  


        #Panel para apellidos

        panelApellidosTitulos = CTkFrame(panelIzquierdo1, fg_color = "transparent")
        panelApellidosTitulos.pack()                

        tituloApellido2 = smallText(panelApellidosTitulos, "Apellido 1")
        tituloApellido2.pack(side = "left", padx = 30)

        iconoLapiz3 = iconoClickable(panelApellidosTitulos, "PencilIcon", 29, 29, lambda: (
        nombreLabel.configure(state="normal") if self.editando else nombreLabel.configure(state="disabled", border_width=1),
        setattr(self, "editando", not self.editando)))  
        iconoLapiz3.pack(side = "left")

        tituloApellido1 = smallText(panelApellidosTitulos, "Apellido 2")
        tituloApellido1.pack(side = "left", padx = 50)

        iconoLapiz2 = iconoClickable(panelApellidosTitulos, "PencilIcon", 29, 29, lambda: (
        nombreLabel.configure(state="normal") if self.editando else nombreLabel.configure(state="disabled", border_width=1),
        setattr(self, "editando", not self.editando)))  
        iconoLapiz2.pack(side = "left")

        #Panel de Entrada de Apellidos

        panelApellidos = CTkFrame(panelIzquierdo1, fg_color = "transparent")
        panelApellidos.pack( fill = "x")

        apellido1Label = CTkEntry(
            panelApellidos,
            placeholder_text= "apellido_1",
            justify = CENTER,
            font= ("Labrada", 20),
            placeholder_text_color= "black",
            fg_color = "#F2F2F2",
            state= "normal",
            border_width=0
            )
        
        apellido1Label.pack(side = "left", padx = 30)

        apellido2Label = CTkEntry(
            panelApellidos,
            placeholder_text= "apellido_2",
            justify = CENTER,
            font= ("Labrada", 20),
            placeholder_text_color= "black",
            fg_color = "#F2F2F2",
            state= "normal",
            border_width=0
            )
        

        apellido2Label.pack(side = "left", padx = 40)

        #Entrada para la Ciudad

        panelCiudad = CTkFrame(panelIzquierdo1, fg_color="transparent")
        panelCiudad.pack(anchor = "nw", fill = "x")

        tituloCiudad = smallText(panelCiudad, "Ciudad")
        tituloCiudad.pack(side = "left", padx = 30)


        ciudadLabel = CTkEntry(
            panelIzquierdo1,
            placeholder_text= "Ciudad",
            justify = CENTER,
            font= ("Labrada", 20),
            placeholder_text_color= "black",
            fg_color = "#F2F2F2",
            state= "normal",
            border_width=0
            )


        iconoLapiz4 = iconoClickable(panelCiudad, "PencilIcon", 29, 29, lambda: (
        ciudadLabel.configure(state="normal") if self.editando else ciudadLabel.configure(state="disabled", border_width=1),
        setattr(self, "editando", not self.editando)))  

        iconoLapiz4.pack(side = "left")
        ciudadLabel.pack(anchor = "nw", padx = 20)  
        

        #Contenido del Panel Derecho
        #
        #

        hojoDeVidaPanel = CTkFrame(panelDerecho2, fg_color="transparent")
        hojoDeVidaPanel.pack(anchor = "nw")

        hojaDeVidaTitulo = mediumText(hojoDeVidaPanel, "Hoja de Vida")
        iconoUsuario = icono(hojoDeVidaPanel,"FolderIcon",38,38)

        hojaDeVidaTitulo.pack(side = "left", padx = 10)
        iconoUsuario.pack(side = "left")

        hojaActualPanel = CTkFrame(panelDerecho2, fg_color="transparent")
        hojaActualPanel.pack(anchor = "nw")

        hojaActual = smallText(hojaActualPanel, "Su Hoja de Vida actual:")
        hojaActual.pack(side = "left", padx = 30)

        iconoDescargar = iconoClickable(hojaActualPanel, "DownloadIcon1", 35,35, lambda: None)
        iconoDescargar.pack(side = "left")

        modificarHoja = smallText(panelDerecho2, "Modificar Hoja de Vida")
        modificarHoja.pack(anchor = "nw", padx = 20, pady = 20)

        panelSubirHoja = CTkFrame(panelDerecho2, fg_color = "transparent")
        panelSubirHoja.pack(expand = True)  

        iconoSubir = icono(panelSubirHoja, "UploadIcon", 35, 35)
        iconoSubir.pack(side = "left")

        botonSubir = botonAccion(panelSubirHoja, "Subir Nuevo Archivo", 20, "verde", 320, 34, lambda: None)
        botonSubir.pack(side = "left")

