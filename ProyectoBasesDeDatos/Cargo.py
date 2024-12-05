import customtkinter as ctk
import tkinter as tk
from PIL import Image
from Utilidades import *


class AnadirCargo(CTkFrame):


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

        abrirConvocatoria = bigText(panelInformacion, "Añadir Cargo/Concurso")
        abrirConvocatoria.pack(anchor = "nw", padx = 50)

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        #Paneles de Formulario - 1

        panel1 = CTkFrame(panelScrollable, fg_color = "transparent")
        panel1.pack(anchor = "nw", pady = 30, fill = "x")

        nombreCargo = formularioSimple(panel1, "Nombre Cargo:")
        nombreCargo.pack(side = "left", padx = 32)

        escuela = formularioSimple(panel1, "Escuela:")
        escuela.pack(side = "right", padx = 32)

        #Subtitulo

        perfil = mediumText(panelScrollable, "Perfil")
        perfil.pack(anchor = "nw", pady = 30, padx = 30)

        #Paneles de Formulario - 2

        panel2 = CTkFrame(panelScrollable, fg_color = "transparent")
        panel2.pack(anchor = "nw", pady = 30, fill = "x")

        areaDisciplinar = formularioSimple(panel2, "Area Disciplinar:")
        areaDisciplinar.pack(side = "left", padx = 32)

        titulacion = formularioSimple(panel2, "Titulación Requerida:")
        titulacion.pack(side = "right", padx = 32)


        #Paneles de Formulario - 3

        panel3 = CTkFrame(panelScrollable, fg_color = "transparent")
        panel3.pack(anchor = "nw", pady = 30, fill = "x")

        experiencia = formularioSimple(panel3, "Experiencia:")
        experiencia.pack(side = "left", padx = 32)

        areaAcademica = formularioSimple(panel3, "Área Académica:")
        areaAcademica.pack(side = "right", padx = 32)

        #Paneles de Formulario - 4

        panel4 = CTkFrame(panelScrollable, fg_color = "transparent")
        panel4.pack(anchor = "nw", pady = 30, fill = "x")

        modalidad = formularioSimple(panel4, "Modalidad:")
        modalidad.pack(side = "left", padx = 32)

        compromiso = formularioSimple(panel4, "Compromiso de Formación:")
        compromiso.pack(side = "right", padx = 32)

        #Subtitulo

        fechas = mediumText(panelScrollable, "Fechas")
        fechas.pack(anchor = "nw", pady = 30, padx = 30)

        #Frames fechas

        frameFechas1 = CTkFrame(panelScrollable, fg_color= "transparent", bg_color= "transparent", corner_radius= 16)
        frameFechas1.pack(anchor = "nw", padx = 20, fill = "x", pady = 20, expand = True)

        entradaFecha1 = entradaFecha(frameFechas1, "Fecha Inicio")
        entradaFecha1.pack(side = "left", padx = 40)

        entradaFecha2 = entradaFecha(frameFechas1, "Fecha Fin")
        entradaFecha2.pack(side = "right", padx = 40)

        frameFechas2 = CTkFrame(panelScrollable, fg_color= "transparent", bg_color= "transparent", corner_radius= 16)
        frameFechas2.pack(anchor = "nw", padx = 20, fill = "x", pady = 20, expand = True)

        entradaFecha3 = entradaFecha(frameFechas2, "Fecha Hojas \n de Vida")
        entradaFecha3.pack(side = "left", padx = 40)

        entradaFecha4 = entradaFecha(frameFechas2, "Fecha Prueba \n Psicotécn.")
        entradaFecha4.pack(side = "right", padx = 40)

        frameFechas3 = CTkFrame(panelScrollable, fg_color= "transparent", bg_color= "transparent", corner_radius= 16)
        frameFechas3.pack(anchor = "nw", padx = 20, fill = "x", pady = 20, expand = True)

        entradaFecha5 = entradaFecha(frameFechas3, "Fecha Sesión")
        entradaFecha5.pack(side = "left", padx = 40)

        entradaFecha6 = entradaFecha(frameFechas3, "Fecha Entrevista")
        entradaFecha6.pack(side = "right", padx = 40)

        #Botón para subir

        botonSubir = botonAccion(panelScrollable, "Añadir Concurso para Cargo", 20, "verde", 320, 35, lambda: None)
        botonSubir.pack(anchor = "nw", padx = 40, pady = 20)