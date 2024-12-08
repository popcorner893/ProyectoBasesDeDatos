from customtkinter import *
import tkinter as tk
from PIL import Image
import Login
import PantallaPerfil
import sesionActual
import conectarMySql

class MenuPrincipalUsuario(CTkFrame):

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
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white", command=lambda: self.controller.show_frame(Login.MainLogin))
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario

        nombreUsuario = CTkButton(panelUsuario, text = sesionActual.sesionActualAspirante.username, font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white", command=lambda: self.controller.show_frame(PantallaPerfil.PantallaPerfilAspirante))
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Panel de Información, Scrollable

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="transparent")
        panelScrollable.pack(expand = True, fill = "both")


        bienvenidaTexto = CTkLabel(panelScrollable, text = "BIENVENIDO, " + sesionActual.sesionActualAspirante.nombre, font=("Labrada", 40))
        bienvenidaTexto.pack(anchor = "nw", padx = 50)

        #Subpanel de Postulaciones
        panelPostulacionesArray = []
        for cargo in sesionActual.sesionActualAspirante.cargos:
            panelPostulaciones = CTkScrollableFrame(panelScrollable, fg_color="#F2F2F2", corner_radius= 16, height = 400)
            panelPostulaciones.pack(expand = True, fill = "x", padx = 50, pady = 20)
            panelPostulacionesArray.append(panelPostulaciones)
        
        #Texto de Postulaciones

        textoPostulaciones = CTkLabel(panelPostulaciones, text = "Sus postulaciones:", font=("Labrada", 35))
        textoPostulaciones.pack(anchor = "nw", padx = 20)    


        #Crea instancias de cada postulación
        for panelPostulacionesPrueba in panelPostulacionesArray:
            postulacionPrueba = Postulacion(panelPostulaciones)
            postulacionPrueba.pack(expand = True, fill = "both", padx = 30, pady = 20)
        Postulacion.contador=0 #resetea el contador de paneles para un proximo usuario


        #Subpanel de Convocatorias Abiertas
        panelConvocatoriasArray = []
        for convocatoria in sesionActual.sesionActualAspirante.convocatoria:
            panelConvocatorias = CTkScrollableFrame(panelScrollable, fg_color="#F2F2F2", corner_radius= 16, height = 400)
            panelConvocatorias.pack(expand = True, fill = "x", padx = 50, pady = 20)
            panelConvocatoriasArray.append(panelConvocatorias)

        #Texto de Convocatorias

        textoConvocatorias = CTkLabel(panelConvocatorias, text = "Convocatorias Abiertas:", font=("Labrada", 35))
        textoConvocatorias.pack(anchor = "nw", padx = 20)

        #Crea instancias de convocatorias
        for convocatoriaPrueba in panelConvocatoriasArray:
            convocatoriaPrueba = Convocatoria(panelConvocatorias)
            convocatoriaPrueba.pack(expand = True, fill = "both", padx = 30, pady = 20)

        #Subpanel de Publicaciones Recientes

        panelPublicaciones = CTkScrollableFrame(panelScrollable, fg_color="#F2F2F2", corner_radius= 16, height = 400)
        panelPublicaciones.pack(expand = True, fill = "x", padx = 50, pady = 20)

        #Texto de Publicaciones

        textoPublicaciones = CTkLabel(panelPublicaciones, text = "Publicaciones Recientes:", font=("Labrada", 35))
        textoPublicaciones.pack(anchor = "nw", padx = 20)

        #Crea instancias de publicaciones

        postulacionPrueba = Publicacion(panelPublicaciones)
        postulacionPrueba.pack(expand = True, fill = "both", padx = 30, pady = 20)

        postulacionPrueba = Publicacion(panelPublicaciones)
        postulacionPrueba.pack(expand = True, fill = "both", padx = 30, pady = 20)



class Postulacion(CTkFrame):

    #Clase para crear las postulaciones y no tener que hacerla por separado para cada una
    contador=0 # lleva un registro de la postulacion en la que se encuentra
    def __init__(self, parent):
        
        super().__init__(parent, fg_color="#DEEDFD", corner_radius= 16, bg_color= "transparent") 

        self.columnconfigure(0, weight=7)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        panelIzquierdo = CTkFrame(self,fg_color="transparent", corner_radius= 16)
        panelIzquierdo.grid(row = 0, column = 0, sticky = "nswe")

        panelDerecho = CTkFrame(self,fg_color="transparent", corner_radius= 16)
        panelDerecho.grid(row = 0, column = 1, sticky = "nswe")  
        
        cargo = sesionActual.sesionActualAspirante.cargos[Postulacion.contador]
        idConcurso = sesionActual.sesionActualAspirante.idconcursos[Postulacion.contador]
        conexion = conectarMySql.MiConexion()
                   
        # Contenido Panel Izquierdo    

        nombre_cargo = CTkLabel(panelIzquierdo, text = cargo, font=("Labrada", 25))
        nombre_cargo.pack(anchor = "nw", padx = 26)

        numero_concurso = CTkLabel(panelIzquierdo, text = "Concurso Número: "+ str(idConcurso), font=("Labrada", 20))
        numero_concurso.pack(anchor = "nw", padx = 30)

        perfil_cargo = CTkLabel(panelIzquierdo, text = "Perfil del Cargo", font=("Labrada", 25))
        perfil_cargo.pack(anchor = "nw", padx = 26, pady = 20)

        descripcionCargoFrame = CTkFrame(panelIzquierdo,fg_color="transparent", corner_radius= 16)
        descripcionCargoFrame.columnconfigure((0,1), weight = 1)
        descripcionCargoFrame.rowconfigure((0,1), weight= 1)
        descripcionCargoFrame.pack(anchor = "nw", padx = 26, pady = 20)

        #dupla con area diciplinar y titulo minimo requerido
        perfiles = conexion.get_perfiles_concurso(idConcurso)
        
        area_disciplinar = CTkLabel(descripcionCargoFrame, text = "Área Disciplinar:", font=("Labrada", 20))
        area_disciplinar.grid(row = 0, column = 0)
        area_disciplinar1 = CTkLabel(descripcionCargoFrame, text = perfiles[0], font=("Labrada", 20))
        area_disciplinar1.grid(row = 0, column = 1)

        titulacion_minima = CTkLabel(descripcionCargoFrame, text = "Titulación Mínima:", font=("Labrada", 20))
        titulacion_minima.grid(row = 1, column = 0, padx = 20)

        titulacion_minima = CTkLabel(descripcionCargoFrame, text = perfiles[1], font=("Labrada", 20))
        titulacion_minima.grid(row = 1, column = 1, padx = 20)

        estadoFrame = CTkFrame(panelIzquierdo,fg_color="transparent")
        estadoFrame.pack(anchor = "nw", pady = 20)

        estado_Persona = CTkLabel(estadoFrame, text = "estado_persona", font=("Labrada", 20))
        estado_Persona.pack(side = "right", padx = 20)

        estadoConcurso = CTkLabel(estadoFrame, text = "Concurso: "+conexion.get_estado_concurso(idConcurso), font=("Labrada", 20))
        estadoConcurso.pack(side = "right", padx = 20)

        estadoConcurso1 = CTkLabel(estadoFrame, text = "Estado del Concurso", font=("Labrada", 25))
        estadoConcurso1.pack(side = "right", padx = 26)

        #Contenido Panel Derecho

        frameCronograma = CTkFrame(panelDerecho,fg_color="#F2F2F2", corner_radius=16, width=300, height=280)
        frameCronograma.pack(expand = True, padx = 30)
        frameCronograma.pack_propagate(False)        

        subframeCronograma = CTkFrame(frameCronograma,fg_color="transparent")
        subframeCronograma.pack(fill = "x")

        cronograma = CTkLabel(subframeCronograma, text = "Cronograma", font=("Labrada", 25))
        cronograma.pack(side = "left", padx = 20)

        imagenCronograma = CTkImage(dark_image= Image.open("calendarIcon.png"), size = (42,42))
        cronogramaImagen = CTkLabel(subframeCronograma, image = imagenCronograma, text = "")
        cronogramaImagen.pack(side = "right", padx = 20)
        
        #dupla con fecha de inicio del concuro y fecha para subir hoja de vida
        fechas = conexion.get_fecha_inicio_hojavida_concurso(idConcurso)

        fechaDeInicio = CTkLabel(frameCronograma, text = "Fecha de Inicio:", font=("Labrada", 20))
        fechaDeInicio.pack(anchor = "nw", padx = 20, pady = 10)

        fechaDeInicio1 = CTkLabel(frameCronograma, text = fechas[0] , font=("Labrada", 20))
        fechaDeInicio1.pack(anchor = "nw", padx = 30, pady = 5)

        fechaHojasDeVida = CTkLabel(frameCronograma, text = "Fecha Hojas de Vida:", font=("Labrada", 20))
        fechaHojasDeVida.pack(anchor = "nw", padx = 20, pady = 10)

        fechaHojasDeVida1 = CTkLabel(frameCronograma, text = fechas[1], font=("Labrada", 20))
        fechaHojasDeVida1.pack(anchor = "nw", padx = 30, pady = 5)
        
        Postulacion.contador+=1


class Convocatoria(CTkFrame):

    #Clase para crear las postulaciones y no tener que hacerla por separado para cada una
    contador=0 #lleva un conteo de la convocatoria en la que se encuentra

    def __init__(self, parent):
        
        super().__init__(parent, fg_color="#DEEDFD", corner_radius= 16, bg_color= "transparent") 

        self.columnconfigure(0, weight=7)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        panelIzquierdo = CTkFrame(self,fg_color="transparent", corner_radius= 16)
        panelIzquierdo.grid(row = 0, column = 0, sticky = "nswe")

        panelDerecho = CTkFrame(self,fg_color="transparent", corner_radius= 16)
        panelDerecho.grid(row = 0, column = 1, sticky = "nswe")  
        
        conexion = conectarMySql.MiConexion()
        #dupla de la fomra (nombreConvocatoria, idConvocatoria)
        ConvocatoriaActual = conexion.get_name_all_convocatorias()[Convocatoria.contador]
        cargosConvocatoriaActual = conexion.get_cargos_convocatoria(ConvocatoriaActual[1])

        #Contenido Panel Izquierdo    

        nombre_convocatoria = CTkLabel(panelIzquierdo, text = ConvocatoriaActual[0], font=("Labrada", 25))
        nombre_convocatoria.pack(anchor = "nw", padx = 26)

        numero_convocatoria = CTkLabel(panelIzquierdo, text = "ID_Convocatoria: "+str(ConvocatoriaActual[1]), font=("Labrada", 20))
        numero_convocatoria.pack(anchor = "nw", padx = 30)

        cargosDisponiblesLabel = CTkLabel(panelIzquierdo, text = "Cargos Disponibles", font=("Labrada", 25))
        cargosDisponiblesLabel.pack(anchor = "nw", padx = 26, pady = 20)

        cargosDisponiblesFrame = CTkFrame(panelIzquierdo,fg_color="white", corner_radius= 16, width=500, bg_color= "transparent")
        cargosDisponiblesFrame.pack(anchor = "nw", padx = 26, pady = 30, expand = True, fill = "both")

        #Añadir Instancias de Cargos

        for cargo in cargosConvocatoriaActual:
            cargoEjemplo = cargoDisponible(cargosDisponiblesFrame,cargo)
            cargoEjemplo.pack(expand = True, fill = "both")




        #Contenido Panel Derecho

        frameImagen = CTkFrame(panelDerecho,fg_color="#F2F2F2", corner_radius=16, width=300, height=280)
        frameImagen.pack(expand = True, padx = 30)
        frameImagen.pack_propagate(False)        

        imagenConvocatoria = CTkLabel(frameImagen, text = "imagen_convocatoria", font=("Labrada", 25))
        imagenConvocatoria.pack(expand = True)
        Convocatoria.contador+=1



class cargoDisponible (CTkFrame):

    #Clase para crear las postulaciones y no tener que hacerla por separado para cada una

    def __init__(self, parent, nombre_cargo):
        
        super().__init__(parent, fg_color="transparent", corner_radius= 16, bg_color= "transparent")

        nombreCargoLabel = CTkLabel(self, text = nombre_cargo, font=("Labrada", 25))
        nombreCargoLabel.pack(side = "left", padx = 26, pady = 20)

        nombreCargoLabel = CTkButton(self, text = "Ir",corner_radius=16, font=("Labrada", 25), fg_color= "#02E1B5", bg_color= "transparent", text_color= "black")
        nombreCargoLabel.pack(side = "right", padx = 26, pady = 20)


class Publicacion(CTkFrame):

    #Clase para crear las postulaciones y no tener que hacerla por separado para cada una

    def __init__(self, parent):
        
        super().__init__(parent, fg_color="#DEEDFD", corner_radius= 16, bg_color= "transparent") 

        self.columnconfigure(0, weight=7)
        self.columnconfigure(1, weight=3)
        self.rowconfigure(0, weight=1)

        panelIzquierdo = CTkFrame(self,fg_color="transparent", corner_radius= 16)
        panelIzquierdo.grid(row = 0, column = 0, sticky = "nswe")

        panelDerecho = CTkFrame(self,fg_color="transparent", corner_radius= 16)
        panelDerecho.grid(row = 0, column = 1, sticky = "nswe")  

        #Contenido Panel Izquierdo    

        tituloPublicacion = CTkLabel(panelIzquierdo, text = "titulo_publicacion", font=("Labrada", 25))
        tituloPublicacion.pack(anchor = "nw", padx = 26)

        textoPublicacion = CTkLabel(panelIzquierdo, text = "texto_publicacion", font=("Labrada", 20))
        textoPublicacion.pack(anchor = "nw", padx = 30)

        reglamentacionLabel = CTkLabel(panelIzquierdo, text = "Se reglamenta el final de la convocatoria a través del acuerdo:", font=("Labrada", 20))
        reglamentacionLabel.pack(anchor = "nw", padx = 26, pady = 20)

        reglamentacionBoton = CTkButton(panelIzquierdo, text = "archivo_acuerdo", text_color= "#4393E5", bg_color= "transparent", fg_color= "transparent", font=("Labrada", 20))
        reglamentacionBoton.pack(anchor = "nw", padx = 26)        

        tituloLista = CTkLabel(panelIzquierdo, text = "lista_concursos", font=("Labrada", 25))
        tituloLista.pack(anchor = "nw", padx = 26)

        #Panel para la lista de concursos
        concursosFrame = CTkFrame(panelIzquierdo,fg_color="white", corner_radius= 16, width=500, bg_color= "transparent")
        concursosFrame.pack(anchor = "nw", padx = 26, pady = 30, expand = True, fill = "both")

        #Añadir Instancias de concursos

        concursoEjemplo1 = concursoPublicacion(concursosFrame,"Pescador")
        concursoEjemplo1.pack(expand = True, fill = "both")

        concursoEjemplo2 = concursoPublicacion(concursosFrame,"Pescador")
        concursoEjemplo2.pack(expand = True, fill = "both")


        #Contenido Panel Derecho

        frameImagen = CTkFrame(panelDerecho,fg_color="#F2F2F2", corner_radius=16, width=300, height=280)
        frameImagen.pack(expand = True, padx = 30)
        frameImagen.pack_propagate(False)        

        imagenPublicacion = CTkLabel(frameImagen, text = "imagen_publicacion", font=("Labrada", 25))
        imagenPublicacion.pack(expand = True)



class concursoPublicacion (CTkFrame):

    #Clase para crear las postulaciones y no tener que hacerla por separado para cada una

    def __init__(self, parent, nombre_cargo):
        
        super().__init__(parent, fg_color="transparent", corner_radius= 16, bg_color= "transparent")

        nombreCargoLabel = CTkLabel(self, text = nombre_cargo, font=("Labrada", 20))
        nombreCargoLabel.pack(side = "left", padx = 26, pady = 10)

        nombreCargoLabel = CTkButton(self, text = "Descargar Reporte Elegibles",corner_radius=16, font=("Labrada", 25), fg_color= "#02E1B5", bg_color= "transparent", text_color= "black")
        nombreCargoLabel.pack(side = "right", padx = 26, pady = 10)

        imagenDescarga = CTkImage(dark_image= Image.open("DownloadIcon.png"), size = (35,35))
        imagenDescarga1 = CTkLabel(self, image = imagenDescarga, text = "")
        imagenDescarga1.pack(side = "right", padx = 20)

