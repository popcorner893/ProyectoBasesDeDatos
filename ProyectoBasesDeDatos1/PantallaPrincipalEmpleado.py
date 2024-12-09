from customtkinter import *
import tkinter as tk
import tkinter.messagebox
from PIL import Image
from Utilidades import *
import Login, PantallaPerfil, Convocatoria, EvaluarInscripciones, Reclamaciones, RealizarEvaluacion, GestionUsuarios, FinalizarConvocatoria
import sesionActual

class MenuPrincipalUsuario(CTkFrame):

    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

        self.controller = controller
        imagenFondo = icono(self, "FondoDegradadoMain", 1280, 720)
        imagenFondo.place(relx = 0, rely = 0, anchor = "nw")    

        frameBlancoFondo = CTkFrame(
            self,
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
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white", command=lambda: goback())
        img_lab1.pack(side = "left", padx = 20, pady = 10)

        def goback():
            Login.sesionActual.sesionActualEmpleado.cerrarSesion()
            self.controller.show_frame(Login.MainLogin)
           

        #Tarjeta de Usuario
        nombreUsuario = CTkButton(panelUsuario, text = f"{sesionActual.sesionActualEmpleado.username}", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white", command=lambda: self.controller.show_frame(PantallaPerfil.PantallaPerfilEmpleado))
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Panel de Información, Scrollable

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="transparent")
        panelScrollable.pack(expand = True, fill = "both")


        #Mensaje de Bienvenida
        bienvenidaTexto = bigText(panelScrollable, f"BIENVENIDO, {Login.sesionActual.sesionActualEmpleado.username}")
        bienvenidaTexto.pack(anchor = "nw", padx = 50)

        #Qué desea hacer?

        queDeseaTexto = mediumText(panelScrollable, "¿Qué desea hacer?")
        queDeseaTexto.pack(anchor = "nw", padx = 50)

        #División de Paneles Según Nivel Acceso

        if sesionActual.sesionActualEmpleado.nivelAceso == "Vicerrector":
            #Primer Panel de Opciones
            panelOpciones1 = CTkFrame(panelScrollable, fg_color="transparent", corner_radius= 16, height = 400)
            panelOpciones1.pack(expand = True, fill = "x", padx = 50, pady = 20)
            panelOpciones1.pack_propagate(False)

            #Segundo Panel de Opciones
            panelOpciones2 = CTkFrame(panelScrollable, fg_color="transparent", corner_radius= 16, height = 400)
            panelOpciones2.pack(expand = True, fill = "x", padx = 50, pady = 20)
            panelOpciones2.pack_propagate(False)
            
            panelIzquierdo1 = frameOpcion(panelOpciones1, "Convocatoria", "AbrirConvocatoriaIcon",1, self.controller)
            panelIzquierdo1.pack(expand = True, side = "left")
            panelIzquierdo1.pack_propagate(False)

            panelDerecho1 = frameOpcion(panelOpciones1, "Gestionar Usuarios", "GestionarUsuariosIcon",5, self.controller)
            panelDerecho1.pack(expand = True, side = "left")
            panelDerecho1.pack_propagate(False)

            panelIzquierdo2 = frameOpcion(panelOpciones2, "Finalizar Convocatoria", "FinalizarConvocatoriaIcon",6, self.controller)
            panelIzquierdo2.pack(expand = True, side = "left")
            panelIzquierdo2.pack_propagate(False)

        if sesionActual.sesionActualEmpleado.nivelAceso == "Vicerrectoría":
            #Primer Panel de Opciones
            panelOpciones1 = CTkFrame(panelScrollable, fg_color="transparent", corner_radius= 16, height = 400)
            panelOpciones1.pack(expand = True, fill = "x", padx = 50, pady = 20)
            panelOpciones1.pack_propagate(False)
            
            panelIzquierdo1 = frameOpcion(panelOpciones1, "Evaluar Inscripciones", "EvaluarInscripcionesIcon",2, self.controller)
            panelIzquierdo1.pack(expand = True, side = "left")
            panelIzquierdo1.pack_propagate(False)


        if sesionActual.sesionActualEmpleado.nivelAceso == "Comité Evaluación":
            #Primer Panel de Opciones
            panelOpciones1 = CTkFrame(panelScrollable, fg_color="transparent", corner_radius= 16, height = 400)
            panelOpciones1.pack(expand = True, fill = "x", padx = 50, pady = 20)
            panelOpciones1.pack_propagate(False)

            #Segundo Panel de Opciones
            panelOpciones2 = CTkFrame(panelScrollable, fg_color="transparent", corner_radius= 16, height = 400)
            panelOpciones2.pack(expand = True, fill = "x", padx = 50, pady = 20)
            panelOpciones2.pack_propagate(False)
            
            panelIzquierdo1 = frameOpcion(panelOpciones1, "Evaluar Inscripciones", "EvaluarInscripcionesIcon",2, self.controller)
            panelIzquierdo1.pack(expand = True, side = "left")
            panelIzquierdo1.pack_propagate(False)

            panelDerecho1 = frameOpcion(panelOpciones1, "Resolver Reclamaciones", "ResolverReclamacionesIcon",3, self.controller)
            panelDerecho1.pack(expand = True, side = "left")
            panelDerecho1.pack_propagate(False)

            panelIzquierdo2 = frameOpcion(panelOpciones2, "Realizar Evaluación", "RealizarEvaluacionIcon",4, self.controller)
            panelIzquierdo2.pack(expand = True, side = "left")
            panelIzquierdo2.pack_propagate(False)
            
        if sesionActual.sesionActualEmpleado.nivelAceso == "Equipo de Desarrollo":
            #Primer Panel de Opciones
            panelOpciones1 = CTkFrame(panelScrollable, fg_color="transparent", corner_radius= 16, height = 400)
            panelOpciones1.pack(expand = True, fill = "x", padx = 50, pady = 20)
            panelOpciones1.pack_propagate(False)
            
            panelIzquierdo1 = frameOpcion(panelOpciones1, "Finalizar Convocatoria", "FinalizarConvocatoriaIcon",6, self.controller)
            panelIzquierdo1.pack(expand = True, side = "left")
            panelIzquierdo1.pack_propagate(False)
        
        
class frameOpcion(CTkFrame):

    def __init__(self, parent, titulo, dir, ventana, controller):
        
        super().__init__(parent, fg_color="#DEEDFD", corner_radius= 16, width = 530, height = 340) 

        if ventana == 1:
            botonDescripcion = botonAccion(self, titulo, 33, "verde", 530, 70, lambda: controller.show_frame(Convocatoria.AbrirConvocatoria))
            botonDescripcion.pack(side = "bottom")

        elif ventana == 2:
            botonDescripcion = botonAccion(self, titulo, 33, "verde", 530, 70, lambda: controller.show_frame(EvaluarInscripciones.EvaluarInscripcion))
            botonDescripcion.pack(side = "bottom")

        elif ventana == 3:
            botonDescripcion = botonAccion(self, titulo, 33, "verde", 530, 70, lambda: controller.show_frame(Reclamaciones.ReclamacionRevisar))
            botonDescripcion.pack(side = "bottom")

        elif ventana == 4:
            botonDescripcion = botonAccion(self, titulo, 33, "verde", 530, 70, lambda: controller.show_frame(RealizarEvaluacion.RealizarEvaluacion))
            botonDescripcion.pack(side = "bottom")

        elif ventana == 5:
            botonDescripcion = botonAccion(self, titulo, 33, "verde", 530, 70, lambda: controller.show_frame(GestionUsuarios.GestionarUsuariosPrincipal))
            botonDescripcion.pack(side = "bottom")

        else:
            botonDescripcion = botonAccion(self, titulo, 33, "verde", 530, 70, lambda: controller.show_frame(FinalizarConvocatoria.FinalizarConvocatoria))
            botonDescripcion.pack(side = "bottom")

    
        

        img = icono(self, dir, 300, 258)
        img.pack(side = "bottom", pady = 10)
