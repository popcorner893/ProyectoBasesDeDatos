class AbrirConvocatoria(CTkFrame):


    def __init__(self, parent, controller):
        
        super().__init__(parent, fg_color="white") 

        self.controller = controller

        self.mi_conexion = conectarMySql.MiConexion()

        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)

        # Crear canvas para manejar la imagen y el texto
        canvas = tk.Canvas(self, width=640, height=721, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        #Imagen de Fondo
        self.img_fondo = tk.PhotoImage(file="FondoDegradadoMain.png")  # Mantener referencia a la imagen
        canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")  # Colocar la imagen en la esquina superior izquierda

        # Variable para almacenar la ruta del archivo
        self.ruta_archivo = None    


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
        img_lab1 = CTkButton(panelUsuario, image=iconBack, text="", bg_color="white", fg_color="white", width=51, height=51, hover_color = "white", command=lambda: self.controller.show_frame(PantallaPrincipalEmpleado.MenuPrincipalUsuario))
        img_lab1.pack(side = "left", padx = 20, pady = 10)


        #Tarjeta de Usuario


        nombreUsuario = CTkButton(panelUsuario, text = f"{Login.sesionActual.sesionActualEmpleado.username}", font=("Labrada", 30), bg_color="white", fg_color="white", text_color= "black", hover_color="white", command = lambda: self.controller.show_frame(PantallaPerfil.PantallaPerfilEmpleado))
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

        entradaCargo2 = entradaLista(cargosFrame, "", "", "", "", "")
        entradaCargo2.pack(anchor = "nw", pady = 20, expand = True, fill = "x")

        addCargo = botonAccion(cargosFrame, "Añadir Cargo", 20, "verde", 220, 34, lambda: cargoSobreVentana())
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

        entradaComite1 = entradaLista(miembrosFrame, "", "", "", "", "")
        entradaComite1.pack(anchor = "nw", pady = 20, expand = True, fill = "x")

        entradaComite2 = entradaLista(miembrosFrame, "", "", "", "", "")
        entradaComite2.pack(anchor = "nw", pady = 20, expand = True, fill = "x")

        addMiembro = botonAccion(miembrosFrame, "Añadir Miembro", 20, "verde", 220, 34, lambda: comiteSobreVentana())
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

        botonSubir = botonAccion(panelSubirHoja, "Subir Nuevo Archivo", 20, "verde", 320, 34, lambda: seleccionar_archivo())
        botonSubir.pack(side = "left", padx = 20)


        #Imagen de Publicación

        publicacion = mediumText(panelScrollable,"Imagen de Publicación:")
        publicacion.pack(anchor = "nw", padx = 20)

        framePublicacion = CTkFrame(panelScrollable, fg_color= "transparent", bg_color= "transparent", corner_radius= 16)
        framePublicacion.pack(anchor = "nw", padx = 20, fill = "x", pady = 30)

        archivoPublicacion = smallText(framePublicacion, "Archivo de Publicación:")
        archivoPublicacion.pack(side = "left")

        panelSubirHoja1 = CTkFrame(framePublicacion, fg_color = "transparent")
        panelSubirHoja1.pack(side = "left", padx = 30)  

        iconoSubir1 = icono(panelSubirHoja1, "UploadIcon1", 30, 30)
        iconoSubir1.pack(side = "left")

        botonSubir1 = botonAccion(panelSubirHoja1, "Subir Nuevo Archivo", 20, "verde", 320, 34, lambda: seleccionar_img())
        botonSubir1.pack(side = "left", padx = 20)

        #Botón Final

        botonSubirConvocatoria = botonAccion(panelScrollable, "Subir Convocatoria", 33, "verde", 470, 60, lambda: asa())
        botonSubirConvocatoria.pack(anchor = "nw", padx = 20)


        def comiteSobreVentana():
            if not hasattr(self, 'idConvocatoria') or self.idConvocatoria is None:
                messagebox.showerror("Error", "Debe ingresar primero una convocatoria")
            else:
                self.idComite = self.mi_conexion.insertar_datos_comite()
                nueva_ventanaC = CTkToplevel(self)
                nueva_ventanaC.title("Añadir comite")
                nueva_ventanaC.geometry("1280x720")
                nueva_ventanaC.resizable(False,False)
                idComite = self.idComite
                anadirMiembro = AnadirMiembro.AnadirMiembro(nueva_ventanaC, idComite)
                anadirMiembro.pack(expand=True, fill = "both")



        def cargoSobreVentana():
            
            if not hasattr(self, 'idConvocatoria') or self.idConvocatoria is None:
                messagebox.showerror("Error", "Debe ingresar primero una convocatoria")
            elif not hasattr(self,'idComite') or self.idComite is None:
                messagebox.showerror("Error", "Debe ingresar primero un comite")
            else:
                nueva_ventana = CTkToplevel(self)
                nueva_ventana.title("Añadir cargo(s)")
                nueva_ventana.geometry("1280x720")
                nueva_ventana.resizable(False,False)
                idConvocatoria = self.idConvocatoria
                idComite = self.idComite
                anadircargo = Cargo.AnadirCargo(nueva_ventana,idConvocatoria,idComite)
                anadircargo.pack(expand = True, fill = "both")

            


        def seleccionar_archivo():

        # Abre el explorador de archivos y guarda la ruta seleccionada
            archivo = filedialog.askopenfilename(title="Selecciona un archivo")
            if archivo:  # Si se seleccionó un archivo
                self.ruta_archivo = archivo
                self.idAcuerdo = self.mi_conexion.insertar_datos_acuerdo(self.ruta_archivo)

        def seleccionar_img():

        # Abre el explorador de archivos y guarda la ruta seleccionada para la publicacion "imagenconv"
            self.img = filedialog.askopenfilename(title="Selecciona un archivo")
            if self.img:  # Si se seleccionó un archivo
                self.ruta_archivo = self.img

        # creo la convocatoria
        def asa():
            nombreConvQuery = entradaTexto.get()
            fechaInicioConv = entradaFecha1.fecha_seleccionada
            fechaFinConv = entradaFecha2.fecha_seleccionada
            if not nombreConvQuery.strip() or not fechaInicioConv or not fechaFinConv or not self.img or not self.ruta_archivo:
                messagebox.showerror("Error", "Alguno de los campos se encuentra vacío")
            else:    
                idCalendarioQuery = self.mi_conexion.insertar_datos_calendario(fechaInicioConv,fechaFinConv)
                self.idConvocatoria = self.mi_conexion.insertar_datos_convocatoria(nombreConvQuery, idCalendarioQuery, self.idAcuerdo, self.img)







    
