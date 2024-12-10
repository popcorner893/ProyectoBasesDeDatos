from customtkinter import *
import tkinter as tk
from PIL import Image
from Utilidades import *
import PantallaPrincipalEmpleado, PantallaPerfil, Convocatoria, conectarMySql, Login
import tkinter.messagebox as messagebox


class AnadirMiembro(CTkFrame):


    def __init__(self, parent, idComite):
        
        super().__init__(parent, fg_color="white") 

        self.mi_conexion = conectarMySql.MiConexion()
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)



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
        self.iconBack = CTkImage(dark_image= Image.open("BackSymbol1.png"), size = (51,51))
        self.img_lab1 = CTkButton(panelUsuario, image=self.iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white")
        self.img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = f"{Login.sesionActual.sesionActualEmpleado.username}", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white")
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

        botonAnadir = botonAccion(panelPrincipal, "Añadir al Comité de Evaluación", 20, "verde", 360, 35, lambda: Anadir())
        botonAnadir.pack(anchor = "nw", padx = 30, pady = 20)

        def Anadir():
            idEmp = entradaTexto.get()
            if not idEmp.strip():
                messagebox.showerror("Error", "Ingrese un empleado")
            else:
                idNivelAcceso = self.mi_conexion.hallar_nivel_acceso(idEmp)
                if idNivelAcceso == 3:
                    self.mi_conexion.anadir_comite_empleado(idComite, idEmp)
                else:
                    messagebox.showerror("Error", "El empleado no hace parte del comite de evaluación")  
