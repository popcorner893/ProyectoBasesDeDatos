import customtkinter as ctk
import tkinter as tk
from PIL import Image
from Utilidades import *


class AbrirConvocatoria(CTkFrame):


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

        abrirConvocatoria = bigText(panelInformacion, "Abrir Convocatoria")
        abrirConvocatoria.pack(anchor = "nw", padx = 50)

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        nombreConvocatoria = mediumText(panelScrollable,"Nombre Convocatoria:")
        nombreConvocatoria.pack(anchor = "nw", padx = 20)

        entradaTexto = CTkEntry(panelScrollable, width = 1064, height = 55, corner_radius= 16, border_width=0, fg_color= "white", font = (("Labrada", 20)), justify = "left")
        entradaTexto.pack(anchor = "nw", padx = 20, pady = 20)


        #Cargos
        concursosYCargos = mediumText(panelScrollable,"Concursos y Cargos:")
        concursosYCargos.pack(anchor = "nw", padx = 20)

        cargosFrame = CTkFrame(panelScrollable, fg_color= "white", bg_color= "transparent", corner_radius= 16)
        cargosFrame.pack(anchor = "nw", padx = 20, fill = "x", pady = 20, expand = True)

        entradaCargo1 = entradaLista(cargosFrame, "Nombre Cargo", "Escuela", "Modalidad", "Fecha Inicio", "Fecha Fin")
        entradaCargo1.pack(anchor = "nw", pady = 20, expand = True, fill = "x")

        entradaCargo2 = entradaLista(cargosFrame, "Pescador", "Ing. Pesquería", "Jóvenes Talentos", "2005-06-11", "2005-06-11")
        entradaCargo2.pack(anchor = "nw", pady = 20, expand = True, fill = "x")

        addCargo = botonAccion(cargosFrame, "Añadir Cargo", 20, "verde", 220, 34, lambda: None)
        addCargo.pack(anchor = "nw",padx = 20, pady = 20)

        #Seleccion de Fechas

        seleccionFechas = mediumText(panelScrollable,"Selección de Fechas:")
        seleccionFechas.pack(anchor = "nw", padx = 20)

        #Frame fechas

        frameFechas = CTkFrame(panelScrollable, fg_color= "transparent", bg_color= "transparent", corner_radius= 16)
        frameFechas.pack(anchor = "nw", padx = 20, fill = "x", pady = 20, expand = True)

        entradaFecha1 = entradaFecha(frameFechas, "Fecha Inicio")
        entradaFecha1.pack(side = "left", padx = 40)

        entradaFecha2 = entradaFecha(frameFechas, "Fecha Fin")
        entradaFecha2.pack(side = "right", padx = 40)


        #Comité de Evaluación

        comite = mediumText(panelScrollable,"Comité de Evaluación:")
        comite.pack(anchor = "nw", padx = 20)

        miembrosFrame = CTkFrame(panelScrollable, fg_color= "white", bg_color= "transparent", corner_radius= 16)
        miembrosFrame.pack(anchor = "nw", padx = 20, fill = "x", pady = 20, expand = True)

        entradaComite1 = entradaLista(miembrosFrame, "nombre", "apellido1", "apellido2", "ciudad", "idEmpleado")
        entradaComite1.pack(anchor = "nw", pady = 20, expand = True, fill = "x")

        entradaComite2 = entradaLista(miembrosFrame, "nombre", "apellido1", "apellido2", "ciudad", "idEmpleado")
        entradaComite2.pack(anchor = "nw", pady = 20, expand = True, fill = "x")

        addMiembro = botonAccion(miembrosFrame, "Añadir Miembro", 20, "verde", 220, 34, lambda: None)
        addMiembro.pack(anchor = "nw",padx = 20, pady = 20)


        #Acuerdo de Aprobacion

        acuerdo = mediumText(panelScrollable,"Acuerdo de Aprobación:")
        acuerdo.pack(anchor = "nw", padx = 20)

        frameAcuerdo = CTkFrame(panelScrollable, fg_color= "transparent", bg_color= "transparent", corner_radius= 16)
        frameAcuerdo.pack(anchor = "nw", padx = 20, fill = "x", pady = 30)

        archivoAcuerdo = smallText(frameAcuerdo, "Archivo de Acuerdo:")
        archivoAcuerdo.pack(side = "left")

        panelSubirHoja = CTkFrame(frameAcuerdo, fg_color = "transparent")
        panelSubirHoja.pack(side = "left", padx = 30)  

        iconoSubir = icono(panelSubirHoja, "UploadIcon1", 30, 30)
        iconoSubir.pack(side = "left")

        botonSubir = botonAccion(panelSubirHoja, "Subir Nuevo Archivo", 20, "verde", 320, 34, lambda: None)
        botonSubir.pack(side = "left", padx = 20)


        #Imagen de Publicación

        publicacion = mediumText(panelScrollable,"Imagen de Publicación:")
        publicacion.pack(anchor = "nw", padx = 20)

        framePublicacion = CTkFrame(panelScrollable, fg_color= "transparent", bg_color= "transparent", corner_radius= 16)
        framePublicacion.pack(anchor = "nw", padx = 20, fill = "x", pady = 30)

        archivoPublicacion = smallText(framePublicacion, "Archivo de Acuerdo:")
        archivoPublicacion.pack(side = "left")

        panelSubirHoja1 = CTkFrame(framePublicacion, fg_color = "transparent")
        panelSubirHoja1.pack(side = "left", padx = 30)  

        iconoSubir1 = icono(panelSubirHoja1, "UploadIcon1", 30, 30)
        iconoSubir1.pack(side = "left")

        botonSubir1 = botonAccion(panelSubirHoja1, "Subir Nuevo Archivo", 20, "verde", 320, 34, lambda: None)
        botonSubir1.pack(side = "left", padx = 20)

        #Botón Final

        botonSubirConvocatoria = botonAccion(panelScrollable, "Subir Convocatoria", 33, "verde", 470, 60, lambda: None)
        botonSubirConvocatoria.pack(anchor = "nw", padx = 20)








    
