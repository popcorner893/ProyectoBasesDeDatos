import customtkinter as ctk
import tkinter as tk
from PIL import Image
from Utilidades import *
import PantallaPrincipalEmpleado, PantallaPerfil


class EvaluarInscripcion(CTkFrame):


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

        abrirConvocatoria = bigText(panelInformacion, "Inscripciones por Revisar:")
        abrirConvocatoria.pack(anchor = "nw", padx = 50)

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="transparent", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        #Paneles Colapsables - 1

        panelColapsable1 = CollapsiblePanel(panelScrollable, "Nombre_cargo")
        panelColapsable1.pack(anchor = "nw",fill = "x", pady = 5)

        informacionAspirante = mediumText(panelColapsable1.content_frame, "Información Aspirante:")
        informacionAspirante.pack(anchor = "nw", padx= 60)

        #Panel blanco de Información
        infoFrame = CTkFrame(panelColapsable1.content_frame, fg_color= "white", bg_color= "transparent", corner_radius= 16)
        infoFrame.pack(anchor = "nw", padx = 20, fill = "x", pady = 20, expand = True)

        entradaInfo = entradaLista(infoFrame, "nombre", "apellido1", "apellido2", "ciudad", "IdAspirante")
        entradaInfo.pack(anchor = "nw", pady = 20, expand = True, fill = "x")

        frameHoja = CTkFrame(infoFrame, fg_color = "transparent", bg_color= "transparent", corner_radius=16)
        frameHoja.pack(fill = "x", anchor = "nw")

        hojaDeVida = smallText(frameHoja, "Hoja de Vida:")
        hojaDeVida.pack(side = "left", padx= 60)

        iconoDescarga = iconoClickable(frameHoja, "DownloadIcon", 35,35, lambda: None)
        iconoDescarga.pack(side = "left")

        informacionAspirante = mediumText(panelColapsable1.content_frame, "Perfil Requerido:")
        informacionAspirante.pack(anchor = "nw", padx= 60)

        #Paneles de Información del Perfil

        panel1 = CTkFrame(panelColapsable1.content_frame, fg_color = "transparent")
        panel1.pack(anchor = "nw", pady = 30, fill = "x")

        areaDisciplinar = tituloSubtituloSimple(panel1, "Area Disciplinar:", "area_disciplinar")
        areaDisciplinar.pack(side = "left", padx = 70)

        titulacion = tituloSubtituloSimple(panel1, "Titulación Requerida:", "titulacion_requerida")
        titulacion.pack(side = "left")

        panel2 = CTkFrame(panelColapsable1.content_frame, fg_color = "transparent")
        panel2.pack(anchor = "nw", pady = 30, fill = "x")

        experiencia = tituloSubtituloSimple(panel2, "Experiencia:", "experiencia")
        experiencia.pack(side = "left", padx = 70)

        areaAcademica = tituloSubtituloSimple(panel2, "Área Académica:", "area_academica")
        areaAcademica.pack(side = "left")

        panel3 = CTkFrame(panelColapsable1.content_frame, fg_color = "transparent")
        panel3.pack(anchor = "nw", pady = 30, fill = "x")

        modalidad = tituloSubtituloSimple(panel3, "Modalidad:", "modalidad")
        modalidad.pack(side = "left", padx = 70)

        compromiso = tituloSubtituloSimple(panel3, "Compromiso de Formación:", "compromiso_formacion")
        compromiso.pack(side = "left")

        #Razón de rechazo

        razonRechazo = mediumText(panelColapsable1.content_frame, "Comentario/Razón de Rechazo")
        razonRechazo.pack(anchor = "nw", padx= 60)

        entradaTexto = CTkEntry(panelColapsable1.content_frame, width = 1000, height = 120, corner_radius= 16, border_width=0, fg_color= "white", font = (("Labrada", 20)), justify = "left")
        entradaTexto.pack(anchor = "nw", padx = 70, pady = 10)


        #Botones para aceptar o rechazar

        panelBotones = CTkFrame(panelColapsable1.content_frame, fg_color = "transparent")
        panelBotones.pack(anchor = "nw", fill = "x", pady = 30)

        botonRechazar = botonAccion(panelBotones, "Rechazar Inscripción", 33, "rojo", 380, 70, lambda: None)
        botonRechazar.pack(side = "left", padx = 40)

        botonAceptar = botonAccion(panelBotones, "Aprobar Inscripción", 33, "verde", 380, 70, lambda: None)
        botonAceptar.pack(side = "right", padx = 40)

        


        



        
        


        