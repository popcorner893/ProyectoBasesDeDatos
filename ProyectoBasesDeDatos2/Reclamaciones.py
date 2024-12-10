from customtkinter import *
import tkinter as tk
from PIL import Image
from Utilidades import *
import PantallaPrincipalEmpleado,  PantallaPerfil
from tkinter import messagebox
from conectarMySql import *
import os


class ReclamacionDiligenciar(CTkFrame):


    def __init__(self, parent):
        
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

        textoPrincipal = bigText(panelTitulo,"Realizar Reclamación")
        textoPrincipal.pack(side = "left", padx = 50)


        

        #Panel de Información

        panelPrincipal = CTkFrame(panelInformacion, fg_color = "#DEEDFD", width = 1120, height = 420, corner_radius=16)
        panelPrincipal.pack(expand = True)
        panelPrincipal.pack_propagate(False)


        #Contenido del Panel

        descripcion = mediumText(panelPrincipal,"Descripción Reclamación:")
        descripcion.pack(anchor = "nw", padx = 20)

        self.ruta = None

        self.entradaTexto = CTkEntry(panelPrincipal, width = 1064, height = 55, corner_radius= 16, border_width=0, fg_color= "white", font = (("Labrada", 20)), justify = "left")
        self.entradaTexto.pack(anchor = "nw", padx = 20, pady = 10)

        archivosAdicionales = mediumText(panelPrincipal,"Archivos Adicionales:")
        archivosAdicionales.pack(anchor = "nw", padx = 20)

        panelSubirHoja = CTkFrame(panelPrincipal, fg_color = "transparent")
        panelSubirHoja.pack(anchor = "nw", padx = 50, pady = 40)  

        iconoSubir = icono(panelSubirHoja, "UploadIcon1", 30, 30)
        iconoSubir.pack(side = "left")

        botonSubir = botonAccion(panelSubirHoja, "Subir Nuevo Archivo", 20, "verde", 320, 34, lambda: seleccionar_archivo())
        botonSubir.pack(side = "left")

        def seleccionar_archivo():
            # Abrir el explorador de archivos
            ruta_archivo = filedialog.askopenfilename(
                title="Seleccionar archivo",
                filetypes=[("Todos los archivos", "*.*"), ("PDF Files", "*.pdf"), ("Imágenes", "*.jpg;*.png;*.jpeg")]
            )

            if ruta_archivo:  # Verificar si se seleccionó un archivo
                self.ruta = ruta_archivo
                print(f"Archivo seleccionado: {self.ruta}")
                messagebox.showinfo("Archivo Seleccionado", f"Archivo seleccionado:\n{self.ruta}")

        self.botonDiligenciar = botonAccion(panelPrincipal, "Diligenciar Reclamación", 33, "rojo", 530, 70,lambda: None)
        self.botonDiligenciar.pack(expand = True)


class ReclamacionRevisar(CTkFrame):

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

        #Títlo principal de Ventana

        abrirConvocatoria = bigText(panelInformacion, "Reclamaciones por Revisar:")
        abrirConvocatoria.pack(anchor = "nw", padx = 50)

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="transparent", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        #Paneles colapsables

        conexion = MiConexion()

        for reclamacion in conexion.get_reclamaciones():
            # Crear un panel para cada convocatoria
            panel = panelColapsableConvocatoria(panelScrollable, reclamacion[0], reclamacion[1], reclamacion[2])
            panel.pack(anchor="nw", fill="x", pady=10)

        


class panelColapsableConvocatoria(CTkFrame):

    def __init__(self, parent, idReclamacion, contenido_reclamacion, archivo_reclamacion):
        super().__init__(parent, fg_color="white") 

        #Paneles Colapsables - 1

        panelColapsable1 = CollapsiblePanel(self, "Reclamación")
        panelColapsable1.pack(anchor = "nw",fill = "x", pady = 5)

        tipoReclamacion = mediumText(panelColapsable1.content_frame, "Reclamación a Publicación")
        tipoReclamacion.pack(anchor = "nw", padx= 60)

        contenidoReclamacion = tinyText(panelColapsable1.content_frame, contenido_reclamacion)
        contenidoReclamacion.pack(anchor = "nw", padx= 80)

        frameArchivo = CTkFrame(panelColapsable1.content_frame, fg_color = "transparent", bg_color= "transparent", corner_radius=16)
        frameArchivo.pack(fill = "x", anchor = "nw")

        archivoAdjunto = smallText(frameArchivo, "Archivo Adjunto:")
        archivoAdjunto.pack(side = "left", padx= 60)

        iconoDescarga = iconoClickable(frameArchivo, "DownloadIcon2", 35, 35, lambda: abrir_archivo(archivo_reclamacion))
        iconoDescarga.pack(side="left")

        def abrir_archivo(archivo_reclamacion):
            try:
                if os.path.exists(archivo_reclamacion):  # Verificar si el archivo existe
                    os.startfile(archivo_reclamacion)  # Abrir el archivo con la aplicación predeterminada
                else:
                    messagebox.showerror("Error", f"El archivo '{archivo_reclamacion}' no existe.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")

        respuestaReclamacion = mediumText(panelColapsable1.content_frame, "Respuesta a Reclamación:")
        respuestaReclamacion.pack(anchor = "nw", padx= 60)

        entradaTexto = CTkEntry(panelColapsable1.content_frame, width = 1000, height = 120, corner_radius= 16, border_width=0, fg_color= "white", font = (("Labrada", 20)), justify = "left")
        entradaTexto.pack(anchor = "nw", padx = 70, pady = 10)

        #Botones

        panelBotones = CTkFrame(panelColapsable1.content_frame, fg_color = "transparent")
        panelBotones.pack(anchor = "nw", fill = "x", pady = 30)

        botonRechazar = botonAccion(panelBotones, "Rechazar Reclamación", 33, "rojo", 380, 70, lambda: completarReclamacion(idReclamacion))
        botonRechazar.pack(side = "left", padx = 40)

        botonAceptar = botonAccion(panelBotones, "Aprobar Reclamación", 33, "verde", 380, 70, lambda: completarReclamacion(idReclamacion))
        botonAceptar.pack(side = "right", padx = 40)

        def completarReclamacion(id):
            conexion = MiConexion()
            conexion.eliminar_reclamacion(id)
            messagebox.showinfo("Completado", "Revisión de la reclamación completada con éxito")
            self.pack_forget()






        
