from customtkinter import *
import tkinter as tk
from PIL import Image
from Utilidades import *

class RealizarEvaluacion(CTkFrame):
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

        #Títlo principal de Ventana

        abrirConvocatoria = bigText(panelInformacion, "Evaluaciones por Realizar:")
        abrirConvocatoria.pack(anchor = "nw", padx = 50)

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="transparent", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        
        entrada1 = EntradaEvaluacion(panelScrollable,"nombre_cargo", "nombre_aspirante", "apellido1_aspirante", "apellido2_aspirante", "id_aspirante")
        entrada1.pack(anchor = "nw", fill = "x")




class EvaluacionEnProceso(CTkFrame):

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

        textoPrincipal = bigText(panelTitulo,"Está evaluando a:")
        textoPrincipal.pack(side = "left", padx = 50)

        textoProceso2 = tinyText(panelTitulo,"id_aspirante")
        textoProceso2.pack(side = "right", padx = 20)

        textoProceso1 = tinyText(panelTitulo,"apellido_aspirante")
        textoProceso1.pack(side = "right", padx = 20)

        textoProceso = tinyText(panelTitulo,"nombre_aspirante")
        textoProceso.pack(side = "right", padx = 20)
        
        #Panel de Información

        panelPrincipal = CTkFrame(panelInformacion, fg_color = "transparent", width = 1120, height = 420, corner_radius=16)
        panelPrincipal.pack(expand = True)
        panelPrincipal.pack_propagate(False)

        #Sesión Docente


        panelSesion = CTkFrame(panelPrincipal, fg_color= "#DEEDFD", corner_radius=16, height = 80)
        panelSesion.pack(anchor = "nw", fill = "x")
        panelSesion.pack_propagate(False)

        textoSesion = mediumText(panelSesion, "Sesión Docente")
        textoSesion.pack(side = "left", padx = 10)

        botonIrSesion = botonAccion(panelSesion, "Ir", 25, "verde", 60, 34, lambda: None)
        botonIrSesion.pack(side = "right", padx = 10)

        #Propuesta de Investigación


        panelPropuesta = CTkFrame(panelPrincipal, fg_color= "#DEEDFD", corner_radius=16, height = 80)
        panelPropuesta.pack(anchor = "nw", fill = "x", pady = 18)
        panelPropuesta.pack_propagate(False)

        textoPropuesta = mediumText(panelPropuesta, "Propuesta de Investigación")
        textoPropuesta.pack(side = "left", padx = 10)

        botonIrPropuesta = botonAccion(panelPropuesta, "Ir", 25, "verde", 60, 34, lambda: None)
        botonIrPropuesta.pack(side = "right", padx = 10)

        #Hoja de Vida

        panelHoja = CTkFrame(panelPrincipal, fg_color= "#DEEDFD", corner_radius=16, height = 80)
        panelHoja.pack(anchor = "nw", fill = "x")
        panelHoja.pack_propagate(False)

        textoHoja = mediumText(panelHoja, "Hoja de Vida")
        textoHoja.pack(side = "left", padx = 10)

        botonIrHoja = botonAccion(panelHoja, "Ir", 25, "verde", 60, 34, lambda: None)
        botonIrHoja.pack(side = "right", padx = 10)

        #Entrevista

        panelEntrevista = CTkFrame(panelPrincipal, fg_color= "#DEEDFD", corner_radius=16, height = 80)
        panelEntrevista.pack(anchor = "nw", fill = "x", pady = 18)
        panelEntrevista.pack_propagate(False)

        textoEntrevista = mediumText(panelEntrevista, "Entrevista")
        textoEntrevista.pack(side = "left", padx = 10)

        botonIrEntrevista = botonAccion(panelEntrevista, "Ir", 25, "verde", 60, 34, lambda: None)
        botonIrEntrevista.pack(side = "right", padx = 10)                




class EntradaEvaluacion(CTkFrame):

    def __init__(self, parent, text1, text2, text3, text4, text5):
        
        super().__init__(parent, fg_color="#DEEDFD", corner_radius=16) 

        infoAspirante = entradaLista(self,"nombre_cargo", "nombre_aspirante", "apellido1_aspirante", "apellido2_aspirante", "id_aspirante")
        infoAspirante.configure(fg_color = "transparent")
        infoAspirante.pack(anchor = "nw", pady = 10, expand = True, fill = "x")

        botonEvaluar = botonAccion(self,"Realizar Evaluación", 20, "verde", 300, 40, lambda: None)
        botonEvaluar.pack(expand = True, pady = 10)







        


