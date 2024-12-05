from customtkinter import *
import tkinter as tk
from PIL import Image
from Utilidades import *


class EvaluacionSesionDocente(CTkFrame):

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
        
        #Panel de Información:, Scrollable

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)


        panelGuia = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        panelGuia.pack(anchor = "nw", fill = "x")

        criterios = bigText(panelGuia, "Sesión Docente - Criterios")
        criterios.pack(side = "left", padx = 20)

        puntajeGuia = mediumText(panelGuia, "Puntaje (0.00 - 1.00)")
        puntajeGuia.pack(side = "right", padx = 60)

        #Crea instancias de cada cuestionario

        preguntas = {

        }

        requisitos = [
            "1. Calidad de los procesos lógicos",
            "2. Calidad, profundidad y complejidad de los conocimientos tratados",
            "3. Estrategias de aprovechamiento de recursos didácticos y de interacción que permitan la comprensión del tema tratado",
            "4. Flexibilidad del plan o de la estrategia planificada para ser adecuada a la realidad de la interacción en el desarrollo de la sesión docente"
        ]

        for i, requisito in enumerate(requisitos):

            pregunta = preguntaCuestionario(panelScrollable, requisito, 1)
            pregunta.pack(anchor = "nw", fill = "x", pady = 10)

            preguntas[i] = pregunta

        #Calcular el Total
        frameTotal = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameTotal.pack(anchor = "nw", fill = "x", pady = 20)

        total = bigText(frameTotal, "Total Puntaje")
        total.pack(side = "left", padx = 20)

        botonTotal = botonAccion(frameTotal, "", 20, "blanco", 180, 40, lambda: None)
        botonTotal.pack(side = "right", padx = 100)

        #Subir la Calificación

        frameSubirPuntaje = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameSubirPuntaje.pack(anchor = "nw", fill = "x", pady = 30)

        matrizValoracion = tinyText(frameSubirPuntaje, "Matriz de Valoración: ")
        matrizValoracion.pack(side = "left", padx = 30)

        downloadIcon = iconoClickable(frameSubirPuntaje, "DownloadIcon2", 35, 35, lambda: None)
        downloadIcon.pack(side = "left", padx = 20)

        botonSubir = botonAccion(frameSubirPuntaje, "Subir Puntaje", 25, "verde", 350, 45, lambda: None)
        botonSubir.pack(side = "right", padx = 100)



class EvaluacionPropuestaInvestigacion(CTkFrame):


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
        
        #Panel de Información:, Scrollable

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        #Componente Escrito

        propuestaTexto = bigText(panelScrollable, "Propuesta de Investigación - Componente Escrito")
        propuestaTexto.pack(anchor = "nw")


        panelGuia = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        panelGuia.pack(anchor = "nw", fill = "x")

        criterios = bigText(panelGuia, "Criterios")
        criterios.pack(side = "left", padx = 20)

        puntajeGuia = mediumText(panelGuia, "Puntaje (0 - 100)")
        puntajeGuia.pack(side = "right", padx = 60)

        #Crea instancias de cada cuestionario    
        

        requisitos1 = [
            "1. Pertinencia y actualidad del Estado del Arte",
            "2. Claridad en la descripción de la pregunta o problema",
            "3. Actualidad y vigencia de los planteamientos expuestos",
            "4. Viabilidad institucional de ejecución de la propuesta",
        ]


        segmento1 = cuestionarioSegmentado(panelScrollable,"A. Planteamiento de la Pregunta o Problema de Investigación", 2, requisitos1)
        segmento1.pack(anchor = "nw", fill = "x")

        requisitos2 = [
            "5. Concordancia con el problema o pregunta"
        ]

        segmento2 = cuestionarioSegmentado(panelScrollable,"B. Objetivos", 2, requisitos2)
        segmento2.pack(anchor = "nw", fill = "x")

        requisitos3 = [
            "6. Pertinencia de la metodología para el logro de los objetivos"
        ]

        segmento3 = cuestionarioSegmentado(panelScrollable,"C. Metodología", 2, requisitos3)
        segmento3.pack(anchor = "nw", fill = "x")

        requisitos4 = [
            "7. Correspondencia con las exigencias teóricas y metodológicas"
        ]

        segmento4 = cuestionarioSegmentado(panelScrollable,"D. Cronograma", 2, requisitos4)
        segmento4.pack(anchor = "nw", fill = "x")


        requisitos5 = [
            "8. La generación de nuevo conocimiento",
            "9. El fortalecimiento de la comunidad científica",
            "10. Las estrategias de divulgación"    
        ]

        segmento5 = cuestionarioSegmentado(panelScrollable,"E. Calidad e impacto de los resultados esperados en:", 2, requisitos5)
        segmento5.pack(anchor = "nw", fill = "x")


        requisitos6 = [
            "11. Redacción y ortografía"    
        ]

        segmento6 = cuestionarioSegmentado(panelScrollable,"F. Presentación de la propuesta", 2, requisitos6)
        segmento6.pack(anchor = "nw", fill = "x")

        requisitos7 = [
            "12. Pertinencia y actualidad"    
        ]

        segmento7 = cuestionarioSegmentado(panelScrollable,"G. Bibliografía", 2, requisitos7)
        segmento7.pack(anchor = "nw", fill = "x")

        requisitos8 = [
            "13. Pertinencia de los rubros",
            "14. Fuentes de Financiación"
        ]

        segmento8 = cuestionarioSegmentado(panelScrollable,"H. Presupuesto", 2, requisitos8)
        segmento8.pack(anchor = "nw", fill = "x")


        #Panel para el subtotal
        
        frameSubTotal = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameSubTotal.pack(anchor = "nw", fill = "x", pady = 20)

        subTotal = bigText(frameSubTotal, "Subtotal")
        subTotal.pack(side = "left", padx = 20)

        botonSubTotal = botonAccion(frameSubTotal, "", 20, "blanco", 180, 40, lambda: None)
        botonSubTotal.pack(side = "right", padx = 100)

        #Panel para la matriz de valoración del componente escrito

        frameMatrizSubtotal = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameMatrizSubtotal.pack(anchor = "nw", fill = "x", pady = 10)

        matrizValoracion1 = tinyText(frameMatrizSubtotal, "Matriz de Valoración: ")
        matrizValoracion1.pack(side = "left", padx = 30)

        downloadIcon1 = iconoClickable(frameMatrizSubtotal, "DownloadIcon2", 35, 35, lambda: None)
        downloadIcon1.pack(side = "left", padx = 20)


        #Sustentación

        #Crea instancias de cada cuestionario

        preguntasSustentacion = {

        }

        requisitos9 = [
            "15. Introducción",
            "16. Planteamiento del problema",
            "17. Metodología",
            "18. Relevancia de la información",
            "19. Expresión oral",
            "20. Adecuación del tiempo establecido",
            "21. Recursos Audiovisuales"

        ]


        #Separador para la sección de sustentación 
        
        propuestaTexto = bigText(panelScrollable, "Propuesta de Investigación - Sustentación")
        propuestaTexto.pack(anchor = "nw")

        panelGuia = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        panelGuia.pack(anchor = "nw", fill = "x")

        criterios = bigText(panelGuia, "Criterios")
        criterios.pack(side = "left", padx = 20)

        puntajeGuia = mediumText(panelGuia, "Puntaje (0.00 - 5.00)")
        puntajeGuia.pack(side = "right", padx = 60)

        for i, requisito in enumerate(requisitos9):

            pregunta = preguntaCuestionario(panelScrollable, requisito, 3)
            pregunta.pack(anchor = "nw", fill = "x", pady = 10)

            preguntasSustentacion[i] = pregunta
        

        #Panel para el segundo subtotal

        frameSubTotal = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameSubTotal.pack(anchor = "nw", fill = "x", pady = 20)

        subTotal1 = bigText(frameSubTotal, "Subtotal")
        subTotal1.pack(side = "left", padx = 20)

        botonSubTotal1 = botonAccion(frameSubTotal, "", 20, "blanco", 180, 40, lambda: None)
        botonSubTotal1.pack(side = "right", padx = 100)

        #Panel para la matriz de valoración de la sustentación

        frameMatrizSubtotal1 = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameMatrizSubtotal1.pack(anchor = "nw", fill = "x", pady = 10)

        matrizValoracion2 = tinyText(frameMatrizSubtotal1, "Matriz de Valoración: ")
        matrizValoracion2.pack(side = "left", padx = 30)

        downloadIcon2 = iconoClickable(frameMatrizSubtotal1, "DownloadIcon2", 35, 35, lambda: None)
        downloadIcon2.pack(side = "left", padx = 20)


        #Botón final para calcular el total

        frameTotal = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameTotal.pack(anchor = "nw", fill = "x", pady = 20)

        total = bigText(frameTotal, "Total Puntaje")
        total.pack(side = "left", padx = 20)

        botonTotal = botonAccion(frameTotal, "", 20, "blanco", 180, 40, lambda: None)
        botonTotal.pack(side = "right", padx = 100)

        botonSubir = botonAccion(panelScrollable, "Subir Puntaje", 25, "verde", 350, 45, lambda: None)
        botonSubir.pack(side = "right", padx = 100)



class EvaluacionHojaDeVidaJovenesTalentos(CTkFrame):

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
        
        #Panel de Información:, Scrollable

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)


        panelGuia = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        panelGuia.pack(anchor = "nw", fill = "x")

        criterios = bigText(panelGuia, "Hoja de Vida - Criterios")
        criterios.pack(side = "left", padx = 20)

        puntajeGuia = mediumText(panelGuia, "Puntaje")
        puntajeGuia.pack(side = "right", padx = 140)

        #Crea instancias de cada cuestionario

        #Puntaje Fijo

        puntajeFijo = CTkFrame(panelScrollable, fg_color="transparent", corner_radius=16)
        puntajeFijo.pack(anchor = "nw", fill = "x")

        puntajeFijoTexto = smallText(puntajeFijo, "1. Cumplimiento de los requisitos exigidos en el perfil (Valor fijo)")
        puntajeFijoTexto.pack(side="left", padx=30)

        puntajeFijoValor = smallText(puntajeFijo, "240")
        puntajeFijoValor.pack(side="left", padx=170)



        #Crea instancias de cada cuestionario

        requisitos1 = [
            "Título superior al grado"
        ]


        segmento1 = cuestionarioSegmentado(panelScrollable,"I. Estudios (máx = 10)", 4, requisitos1)
        segmento1.pack(anchor = "nw", fill = "x")

        requisitos2 = [
            "En docencia, investigación, extensión, profesional diferente a la docente"
        ]


        segmento2 = cuestionarioSegmentado(panelScrollable,"II. Experiencia (máx = 20)", 5, requisitos2)
        segmento2.pack(anchor = "nw", fill = "x")

        requisitos3 = [
            "En el campo de la investigación, servicio a la sociedad, extensión, académicas"
        ]


        segmento3 = cuestionarioSegmentado(panelScrollable,"III. Distinciones Reglamenentadas (máx = 20)", 5, requisitos3)
        segmento3.pack(anchor = "nw", fill = "x")

        requisitos4 = [
            "Publicaciones en revistas internacionales indexadas",
            "Publicaciones en revistas nacionales indexadas",
            "Patentes",
            "Libro o capítulo de libro"
        ]


        segmento4 = cuestionarioSegmentado(panelScrollable,"IV. Productividad Académica (máx = 10)", 4, requisitos4)
        segmento4.pack(anchor = "nw", fill = "x")


        #Calcular el Total
        frameTotal = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameTotal.pack(anchor = "nw", fill = "x", pady = 20)

        total = bigText(frameTotal, "Total Puntaje")
        total.pack(side = "left", padx = 20)

        botonTotal = botonAccion(frameTotal, "", 20, "blanco", 180, 40, lambda: None)
        botonTotal.pack(side = "right", padx = 100)

        #Subir la Calificación

        frameSubirPuntaje = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameSubirPuntaje.pack(anchor = "nw", fill = "x", pady = 30)

        matrizValoracion = tinyText(frameSubirPuntaje, "Matriz de Valoración: ")
        matrizValoracion.pack(side = "left", padx = 30)

        downloadIcon = iconoClickable(frameSubirPuntaje, "DownloadIcon2", 35, 35, lambda: None)
        downloadIcon.pack(side = "left", padx = 20)

        botonSubir = botonAccion(frameSubirPuntaje, "Subir Puntaje", 25, "verde", 350, 45, lambda: None)
        botonSubir.pack(side = "right", padx = 100)

        
class EvaluacionHojaDeVidaGeneral(CTkFrame):

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
        
        #Panel de Información:, Scrollable

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)


        panelGuia = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        panelGuia.pack(anchor = "nw", fill = "x")

        criterios = bigText(panelGuia, "Hoja de Vida - Criterios")
        criterios.pack(side = "left", padx = 20)

        puntajeGuia = mediumText(panelGuia, "Puntaje")
        puntajeGuia.pack(side = "right", padx = 140)

        #Crea instancias de cada cuestionario

        #Puntaje Fijo

        puntajeFijo = CTkFrame(panelScrollable, fg_color="transparent", corner_radius=16)
        puntajeFijo.pack(anchor = "nw", fill = "x")

        puntajeFijoTexto = smallText(puntajeFijo, "1. Cumplimiento de los requisitos exigidos en el perfil (Valor fijo)")
        puntajeFijoTexto.pack(side="left", padx=30)

        puntajeFijoValor = smallText(puntajeFijo, "160")
        puntajeFijoValor.pack(side="left", padx=115)



        #Crea instancias de cada cuestionario

        requisitos1 = [
            "Título superior al requisito exigido en el perfil, en caso del requisito ser doctorado se asignará la totalidad de los puntos al canidato"
        ]


        segmento1 = cuestionarioSegmentado(panelScrollable,"I. Estudios (máx = 40)", 6, requisitos1)
        segmento1.pack(anchor = "nw", fill = "x")

        requisitos2 = [
            "Docencia universitaria, investigación, profesional diferente a la docente",
            "Experiencia posterior al cargo exigido en el perfil"
        ]


        segmento2 = cuestionarioSegmentado(panelScrollable,"II. Experiencia (máx = 20)", 5, requisitos2)
        segmento2.pack(anchor = "nw", fill = "x")


        requisitos3 = [
            "Publicaciones en revistas internacionales indexadas",
            "Publicaciones en revistas nacionales indexadas",
            "Patentes",
            "Libro o capítulo de libro"
        ]


        segmento3 = cuestionarioSegmentado(panelScrollable,"IV. Productividad Académica (máx = 60)", 7, requisitos3)
        segmento3.pack(anchor = "nw", fill = "x")


        #Calcular el Total
        frameTotal = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameTotal.pack(anchor = "nw", fill = "x", pady = 20)

        total = bigText(frameTotal, "Total Puntaje")
        total.pack(side = "left", padx = 20)

        botonTotal = botonAccion(frameTotal, "", 20, "blanco", 180, 40, lambda: None)
        botonTotal.pack(side = "right", padx = 100)

        #Subir la Calificación

        frameSubirPuntaje = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameSubirPuntaje.pack(anchor = "nw", fill = "x", pady = 30)

        matrizValoracion = tinyText(frameSubirPuntaje, "Matriz de Valoración: ")
        matrizValoracion.pack(side = "left", padx = 30)

        downloadIcon = iconoClickable(frameSubirPuntaje, "DownloadIcon2", 35, 35, lambda: None)
        downloadIcon.pack(side = "left", padx = 20)

        botonSubir = botonAccion(frameSubirPuntaje, "Subir Puntaje", 25, "verde", 350, 45, lambda: None)
        botonSubir.pack(side = "right", padx = 100)


class EvaluacionEntrevista(CTkFrame):

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
        
        #Panel de Información:, Scrollable

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="#DEEDFD", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)


        panelGuia = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        panelGuia.pack(anchor = "nw", fill = "x")

        criterios = bigText(panelGuia, "Entrevista - Aspectos")
        criterios.pack(side = "left", padx = 20)

        puntajeGuia = mediumText(panelGuia, "Puntaje (0 - 20)")
        puntajeGuia.pack(side = "right", padx = 85)

        #Crea instancias de cada cuestionario

        preguntas = {

        }

        requisitos = [
            "1. Habilidades de interacción",
            "2. Actitud hacia la escucha",
            "3. Manejo de autoestima y entorno personal",
            "4. Autorrealización personal y laboral",
            "5. Empatía institucional"
        ]

        for i, requisito in enumerate(requisitos):

            pregunta = preguntaCuestionario(panelScrollable, requisito, 1)
            pregunta.pack(anchor = "nw", fill = "x", pady = 10)

            preguntas[i] = pregunta

        #Calcular el Total
        frameTotal = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameTotal.pack(anchor = "nw", fill = "x", pady = 20)

        total = bigText(frameTotal, "Total Puntaje")
        total.pack(side = "left", padx = 20)

        botonTotal = botonAccion(frameTotal, "", 20, "blanco", 180, 40, lambda: None)
        botonTotal.pack(side = "right", padx = 100)

        #Subir la Calificación

        frameSubirPuntaje = CTkFrame(panelScrollable, fg_color = "transparent", corner_radius= 16)
        frameSubirPuntaje.pack(anchor = "nw", fill = "x", pady = 30)

        matrizValoracion = tinyText(frameSubirPuntaje, "Matriz de Valoración: ")
        matrizValoracion.pack(side = "left", padx = 30)

        downloadIcon = iconoClickable(frameSubirPuntaje, "DownloadIcon2", 35, 35, lambda: None)
        downloadIcon.pack(side = "left", padx = 20)

        botonSubir = botonAccion(frameSubirPuntaje, "Subir Puntaje", 25, "verde", 350, 45, lambda: None)
        botonSubir.pack(side = "right", padx = 100)


class cuestionarioSegmentado(CTkFrame):

    def __init__(self, parent, label, modo, requisitos):
        super().__init__(parent, fg_color="transparent", corner_radius=16)

        self.division = smallText(self, label)
        self.division.pack(anchor = "nw", padx = 30, pady = 20)


        self.preguntas = {}


        for i, requisito in enumerate(requisitos):

            pregunta = preguntaCuestionario(self, requisito, modo)
            pregunta.pack(anchor = "nw", fill = "x", pady = 10)

            self.preguntas[i] = pregunta





        

            






