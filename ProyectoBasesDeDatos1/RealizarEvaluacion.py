from customtkinter import *
import tkinter as tk
from PIL import Image
from Utilidades import *
import PantallaPrincipalEmpleado, PantallaPerfil, Cuestionarios
import sesionActual
import conectarMySql
import tkinter.messagebox as messagebox

class RealizarEvaluacion(CTkFrame):
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

        abrirConvocatoria = bigText(panelInformacion, "Evaluaciones por Realizar:")
        abrirConvocatoria.pack(anchor = "nw", padx = 50)

        panelScrollable = CTkScrollableFrame(panelInformacion, bg_color = "white", fg_color="transparent", corner_radius=16)
        panelScrollable.pack(expand = True, fill = "both", padx = 50, pady = 20)

        conexion = conectarMySql.MiConexion()


        for inscripcionPorCalificar in conexion.get_inscripciones_por_calificar(sesionActual.sesionActualEmpleado.idEmpleado):
            entradaInscripcion = EntradaEvaluacion(
                panelScrollable,
                inscripcionPorCalificar[0],
                inscripcionPorCalificar[1],
                inscripcionPorCalificar[2],
                inscripcionPorCalificar[3],
                inscripcionPorCalificar[4],
            )

            # Capturar referencia específica de cada entradaInscripcion
            entradaInscripcion.botonEvaluar.configure(
                command=lambda arg=inscripcionPorCalificar, ref=entradaInscripcion: ventanaSobreVentana(arg, ref)
            )
            entradaInscripcion.pack(anchor="nw", fill="x", pady=50)


        def ventanaSobreVentana(calificado, entrada_ref):
            nueva_Ventana = CTkToplevel(self)
            nueva_Ventana.title("Realizar Evaluación")
            nueva_Ventana.geometry("1280x720")
            nueva_Ventana.resizable(False, False)

            evaluacionEnProceso = EvaluacionEnProceso(nueva_Ventana, calificado)
            evaluacionEnProceso.pack(expand=True, fill="both")

            evaluacionEnProceso.botonFinalizarEvaluacion.configure(
                command=lambda: finalizarEvaluacion(entrada_ref, calificado, evaluacionEnProceso, nueva_Ventana)
            )


        def finalizarEvaluacion(entrada_inscripcion, calificado, evaluacion_en_proceso, ventana):
            if (
                evaluacion_en_proceso.total > 0
                and evaluacion_en_proceso.realizoEvalDoc
                and evaluacion_en_proceso.realizoEvalEntr
                and evaluacion_en_proceso.realizoEvalHoja
                and evaluacion_en_proceso.realizoEvalProp
            ):
                conexion.anadir_a_lista_elegibles(calificado[5], calificado[4], round(evaluacion_en_proceso.total, 2))
                
                # Cerrar la ventana y eliminar la entrada correspondiente
                ventana.destroy()
                entrada_inscripcion.pack_forget()
            else:
                messagebox.showerror("Error", "Hace falta llenar una o más calificaciones.")


class EvaluacionEnProceso(CTkFrame):

    def __init__(self, parent, calificado):
        
        super().__init__(parent, fg_color="white") 

                
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)

        #Cantidad Total de Puntos

        self.total = 0
        self.realizoEvalDoc = False
        self.realizoEvalProp = False
        self.realizoEvalHoja = False
        self.realizoEvalEntr = False


    
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
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white", command=lambda: parent.destroy())
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = "Usuario", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white", command=lambda: None)
        imagenUsuario = CTkImage(dark_image= Image.open("IconoUsuarioEjemplo.png"), size = (53,53))
        img_lab2 = CTkLabel(panelUsuario, image=imagenUsuario, text="")   


        img_lab2.pack(side = "right", padx = 20)
        nombreUsuario.pack(side = "right", padx = 20)

        #Mensaje Principal de Ventana

        panelTitulo = CTkFrame(panelInformacion, fg_color = "transparent", corner_radius=16)
        panelTitulo.pack(fill = "x")

        textoPrincipal = bigText(panelTitulo,"Está evaluando a:")
        textoPrincipal.pack(side = "left", padx = 50)

        textoProceso2 = tinyText(panelTitulo,calificado[4])
        textoProceso2.pack(side = "right", padx = 20)

        textoProceso1 = tinyText(panelTitulo,calificado[2])
        textoProceso1.pack(side = "right", padx = 20)

        textoProceso = tinyText(panelTitulo,calificado[1])
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

        botonIrSesion = botonAccion(panelSesion, "Ir", 25, "verde", 60, 34, lambda: ventanaSobreVentanaDocente())
        botonIrSesion.pack(side = "right", padx = 10)

        def ventanaSobreVentanaDocente():

            if self.realizoEvalDoc == False:
            
                nueva_Ventana = CTkToplevel(self)
                nueva_Ventana.title("Realizar Evaluación")
                nueva_Ventana.geometry("1280x720")
                nueva_Ventana.resizable(False, False)

                cuestionario = Cuestionarios.EvaluacionSesionDocente(nueva_Ventana, calificado)
                cuestionario.botonSubir.configure(command = lambda: finalizar())
                cuestionario.pack(expand=True, fill="both")

            def finalizar():
                if cuestionario.suma != 0:
                    self.realizoEvalDoc = True
                    messagebox.showinfo("", "Evaluación sesión docente finalizada")
                    self.total += cuestionario.suma
                    nueva_Ventana.destroy()
                    print(self.total)
            

            

        #Propuesta de Investigación


        panelPropuesta = CTkFrame(panelPrincipal, fg_color= "#DEEDFD", corner_radius=16, height = 80)
        panelPropuesta.pack(anchor = "nw", fill = "x", pady = 18)
        panelPropuesta.pack_propagate(False)

        textoPropuesta = mediumText(panelPropuesta, "Propuesta de Investigación")
        textoPropuesta.pack(side = "left", padx = 10)

        botonIrPropuesta = botonAccion(panelPropuesta, "Ir", 25, "verde", 60, 34, lambda: ventanaSobreVentanaPropuesta())
        botonIrPropuesta.pack(side = "right", padx = 10)

        def ventanaSobreVentanaPropuesta():

            if self.realizoEvalProp == False:
            
                nueva_Ventana = CTkToplevel(self)
                nueva_Ventana.title("Realizar Evaluación")
                nueva_Ventana.geometry("1280x720")
                nueva_Ventana.resizable(False, False)

                cuestionario = Cuestionarios.EvaluacionPropuestaInvestigacion(nueva_Ventana, calificado)
                cuestionario.botonSubir.configure(command = lambda: finalizar())
                cuestionario.pack(expand=True, fill="both")

            def finalizar():
                if cuestionario.suma != 0:
                    self.realizoEvalProp = True
                    messagebox.showinfo("", "Evaluación sesión propuesta finalizada")
                    self.total += cuestionario.suma
                    nueva_Ventana.destroy()
                    print(self.total)

        #Hoja de Vida

        panelHoja = CTkFrame(panelPrincipal, fg_color= "#DEEDFD", corner_radius=16, height = 80)
        panelHoja.pack(anchor = "nw", fill = "x")
        panelHoja.pack_propagate(False)

        textoHoja = mediumText(panelHoja, "Hoja de Vida")
        textoHoja.pack(side = "left", padx = 10)

        #Hay que modificar para saber si está en la modalidad de joven talento o en la modalidad general y de acuerdo a eso decidir cuál frame mostrar
        botonIrHoja = botonAccion(panelHoja, "Ir", 25, "verde", 60, 34, lambda: ventanaSobreVentanaHoja())
        botonIrHoja.pack(side = "right", padx = 10)


        def ventanaSobreVentanaHoja():

            if self.realizoEvalHoja == False:
            
                nueva_Ventana = CTkToplevel(self)
                nueva_Ventana.title("Realizar Evaluación")
                nueva_Ventana.geometry("1280x720")
                nueva_Ventana.resizable(False, False)

                cuestionario = Cuestionarios.EvaluacionHojaDeVidaJovenesTalentos(nueva_Ventana, calificado)
                cuestionario.botonSubir.configure(command = lambda: finalizar())
                cuestionario.pack(expand=True, fill="both")

            def finalizar():
                if cuestionario.suma != 0:
                    self.realizoEvalHoja = True
                    messagebox.showinfo("", "Evaluación hoja de vida finalizada")
                    self.total += cuestionario.suma
                    nueva_Ventana.destroy()
                    print(self.total)

        #Entrevista

        panelEntrevista = CTkFrame(panelPrincipal, fg_color= "#DEEDFD", corner_radius=16, height = 80)
        panelEntrevista.pack(anchor = "nw", fill = "x", pady = 18)
        panelEntrevista.pack_propagate(False)

        textoEntrevista = mediumText(panelEntrevista, "Entrevista")
        textoEntrevista.pack(side = "left", padx = 10)

        botonIrEntrevista = botonAccion(panelEntrevista, "Ir", 25, "verde", 60, 34, lambda: ventanaSobreVentanaEntrevista())
        botonIrEntrevista.pack(side = "right", padx = 10)

        
        def ventanaSobreVentanaEntrevista():
        
            if self.realizoEvalEntr == False:
            
                nueva_Ventana = CTkToplevel(self)
                nueva_Ventana.title("Realizar Evaluación")
                nueva_Ventana.geometry("1280x720")
                nueva_Ventana.resizable(False, False)

                cuestionario = Cuestionarios.EvaluacionEntrevista(nueva_Ventana, calificado)
                cuestionario.botonSubir.configure(command = lambda: finalizar())
                cuestionario.pack(expand=True, fill="both")

            def finalizar():
                if cuestionario.suma != 0:
                    self.realizoEvalEntr = True
                    messagebox.showinfo("", "Evaluación hoja de vida finalizada")
                    self.total += cuestionario.suma
                    nueva_Ventana.destroy()
                    print(self.total)  


        #Panel para finalizar Evaluación


        panelFinal = CTkFrame(panelPrincipal, fg_color= "transparent", corner_radius=16, height = 80)          
        panelFinal.pack(anchor = "nw", fill = "x")

        self.botonFinalizarEvaluacion = botonAccion(panelFinal,"Finalizar Evaluación", 20, "verde", 300, 40, lambda: None)
        self.botonFinalizarEvaluacion.pack(expand = True)

        

            






class EntradaEvaluacion(CTkFrame):

    def __init__(self, parent, text1, text2, text3, text4, text5):
        
        super().__init__(parent, fg_color="#DEEDFD", corner_radius=16) 

        self.infoAspirante = entradaLista(self,text1, text2, text3, text4, text5)
        self.infoAspirante.configure(fg_color = "transparent")
        self.infoAspirante.pack(anchor = "nw", pady = 10, expand = True, fill = "x")

        self.botonEvaluar = botonAccion(self,"Realizar Evaluación", 20, "verde", 300, 40, lambda: None)
        self.botonEvaluar.pack(expand = True, pady = 10)







        


