from customtkinter import *
import tkinter as tk
from PIL import Image
import PantallaPrincipalAspirante
import PantallaPrincipalEmpleado
import sesionActual
from Utilidades import *
import conectarMySql
import tkinter.messagebox as messagebox

class MainLogin(CTkFrame):
    
    def __init__(self, parent, controller):


        super().__init__(parent, fg_color="white") 

        def siguienteLogIn(index):
            if index == 0:
                return controller.show_frame(IngresoAspirante)
            else: 
                return controller.show_frame(IngresoEmpleados)

        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)


        mitadIzquierda = CTkFrame(self,fg_color="white")
        mitadIzquierda.grid(row = 0, column = 0, sticky = "nswe")

        imagenLogin = CTkImage(dark_image= Image.open("LoginIlustracion.png"), size = (614,560))
        img_lab1 = CTkLabel(mitadIzquierda, image=imagenLogin, text="")
        img_lab1.pack(pady = 80)

        # Crear mitad derecha
        mitadDerecha = CTkFrame(self, fg_color="white")
        mitadDerecha.grid(row=0, column=1, sticky="nswe")

        # Crear canvas para manejar la imagen y el texto
        canvas = tk.Canvas(mitadDerecha, width=640, height=721, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # Cargar y mostrar la imagen de fondo
        self.img_fondo = tk.PhotoImage(file="FondoLogInDegradado.png")  # Mantener referencia a la imagen
        canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")  # Colocar la imagen en la esquina superior izquierda

        # Agregar texto sobre la imagen
        canvas.create_text(
            320, 200,  # Coordenadas del texto
            text="BIENVENIDO",
            font=("Labrada", 40),
            fill="white"  # Color del texto
        )
        canvas.create_text(
            320, 260,  # Coordenadas del texto
            text="SISTEMA DE SELECCIÓN DE PROFESORES",
            font=("Labrada", 20),
            fill="white"  # Color del texto
        )


        ingresoAspirantes = CTkButton(
            self,
            width=512,
            height=65,
            text= "Ingreso Aspirantes",
            font= ("Labrada", 27),
            text_color= "black",
            fg_color = "#02E1B5",
            hover_color = "#02E1B5",
            command = lambda: siguienteLogIn(0)
            )
        
        canvas.create_window(320, 360, window=ingresoAspirantes, anchor="center")

        ingresoEmpleados = CTkButton(
            self,
            width=512,
            height=65,
            text= "Ingreso Empleados",
            font= ("Labrada", 27),
            text_color= "black",
            fg_color = "#02E1B5",
            hover_color = "#02E1B5",
            command = lambda: siguienteLogIn(1)
            )
        
        canvas.create_window(320, 460, window=ingresoEmpleados, anchor="center")        


class IngresoAspirante(CTkFrame):
    
    def __init__(self, parent, controller):


        super().__init__(parent, fg_color="white")
        self.controller = controller

        def volver():
            return controller.show_frame(MainLogin)

        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)


        mitadIzquierda = CTkFrame(self,fg_color="white")
        mitadIzquierda.grid(row = 0, column = 0, sticky = "nswe")

        imagenLogin = CTkImage(dark_image= Image.open("LoginIlustracion.png"), size = (614,560))
        img_lab1 = CTkLabel(mitadIzquierda, image=imagenLogin, text="")
        img_lab1.pack(pady = 80)

        # Crear mitad derecha
        mitadDerecha = CTkFrame(self, fg_color="white")
        mitadDerecha.grid(row=0, column=1, sticky="nswe")

        # Crear canvas para manejar la imagen y el texto
        canvas = tk.Canvas(mitadDerecha, width=640, height=721, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # Cargar y mostrar la imagen de fondo
        self.img_fondo = tk.PhotoImage(file="FondoLogInDegradado.png")  # Mantener referencia a la imagen
        canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")  # Colocar la imagen en la esquina superior izquierda

        botonBack = iconoClickable(mitadDerecha, "BackSymbol", 54, 54, lambda: volver())    

        # Agregar texto sobre la imagen
        canvas.create_text(
            310, 115,  # Coordenadas del texto
            text="Ingreso Aspirantes",
            font=("Labrada", 40),
            fill="white"  # Color del texto
        )

        self.usuario = CTkEntry(
            mitadDerecha,
            width=512,
            height=65,
            placeholder_text= "Usuario",
            justify = CENTER,
            font= ("Labrada", 27),
            placeholder_text_color= "black",
            fg_color = "white",
            )
        
        self.contrasena = CTkEntry(
            mitadDerecha,
            width=512,
            height=65,
            placeholder_text= "Contraseña",
            justify = CENTER,
            font= ("Labrada", 27),
            placeholder_text_color= "black",
            fg_color = "white",
            )
             
        ingreso = CTkButton(
            self,
            width=512,
            height=65,
            text= "Ingresar",
            font= ("Labrada", 27),
            text_color= "black",
            fg_color = "#02E1B5",
            hover_color = "#02E1B5",
            command=self.verificar_login_aspirante #Funcionalidad boton
            )
      
        canvas.create_window(50, 122, window=botonBack, anchor="center", width=54, height = 54)
        canvas.create_window(320, 280, window=self.usuario, anchor="center")
        canvas.create_window(320, 380, window=self.contrasena, anchor="center")
        canvas.create_window(320, 480, window=ingreso, anchor="center")        
        
    def verificar_login_aspirante(self):
        # Obtener los valores de los campos de texto (usuario y contraseña)
        usuario = self.usuario.get()  # Suponiendo que usuario es un campo de texto
        contrasena = self.contrasena.get()  # Suponiendo que contrasena es un campo de texto

        # Conexion con la base de datos
        conexion = conectarMySql.MiConexion()

        # Verificar si el usuario existe en la base de datos
        usuario_bd = conexion.busca_user_Aspirante(usuario)
    
        # Verificar si la contraseña es correcta para el usuario
        if usuario_bd:
            contrasena_bd = conexion.busca_password_Aspirante(contrasena)
        
        ##cambiar mensajes
        
            if contrasena_bd:
                # Si el usuario y la contraseña son correctos
                messagebox.showinfo("Login exitoso", "¡Bienvenido!")
                sesionActual.sesionActualAspirante.crearSesion(usuario, contrasena)
                return self.controller.show_frame(PantallaPrincipalAspirante.MenuPrincipalUsuario)
                
            else:
                # Si la contraseña es incorrecta
                messagebox.showerror("Error", "Usuario y/o contraseña incorrecta")
        else:
        # Si el usuario no existe
            messagebox.showerror("Error", "Usuario y/o contraseña incorrecta")

class IngresoEmpleados(CTkFrame):
    
    def __init__(self, parent, controller):


        super().__init__(parent, fg_color="white")
        self.controller = controller 

        def volver():
            return controller.show_frame(MainLogin)


        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)


        mitadIzquierda = CTkFrame(self,fg_color="white")
        mitadIzquierda.grid(row = 0, column = 0, sticky = "nswe")

        imagenLogin = CTkImage(dark_image= Image.open("LoginIlustracion.png"), size = (614,560))
        img_lab1 = CTkLabel(mitadIzquierda, image=imagenLogin, text="")
        img_lab1.pack(pady = 80)

        # Crear mitad derecha

        mitadDerecha = CTkFrame(self, fg_color="white")
        mitadDerecha.grid(row=0, column=1, sticky="nswe")

        # Crear canvas para manejar la imagen y el texto

        canvas = tk.Canvas(mitadDerecha, width=640, height=721, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # Cargar y mostrar la imagen de fondo

        self.img_fondo = tk.PhotoImage(file="FondoLogInDegradado.png")  # Mantener referencia a la imagen
        canvas.create_image(0, 0, image=self.img_fondo, anchor="nw")  # Colocar la imagen en la esquina superior izquierda

        botonBack = iconoClickable(mitadDerecha, "BackSymbol", 54, 54, lambda: volver())

       

        # Agregar texto sobre la imagen
        canvas.create_text(
            310, 115,  # Coordenadas del texto
            text="Ingreso Empleados",
            font=("Labrada", 40),
            fill="white"  # Color del texto
        )

        self.usuario = CTkEntry(
            mitadDerecha,
            width=512,
            height=65,
            placeholder_text= "Usuario",
            justify = CENTER,
            font= ("Labrada", 27),
            placeholder_text_color= "black",
            fg_color = "white",
            )
        
        self.contrasena = CTkEntry(
            mitadDerecha,
            width=512,
            height=65,
            placeholder_text= "Contraseña",
            justify = CENTER,
            font= ("Labrada", 27),
            placeholder_text_color= "black",
            fg_color = "white",
            )
             
        ingreso = CTkButton(
            self,
            width=512,
            height=65,
            text="Ingresar",
            font=("Labrada", 27),
            text_color="black",
            fg_color="#02E1B5",
            hover_color="#02E1B5",
            command=self.verificar_login_empleado  # Funcionalidad boton
        )

        canvas.create_window(50, 122, window=botonBack, anchor="center", width=54, height=54)
        canvas.create_window(320, 280, window=self.usuario, anchor="center")
        canvas.create_window(320, 380, window=self.contrasena, anchor="center")
        canvas.create_window(320, 480, window=ingreso, anchor="center")

    def verificar_login_empleado(self):
        # Obtener los valores de los campos de texto (usuario y contraseña)
        usuario = self.usuario.get()  # Suponiendo que usuario es un campo de texto
        contrasena = self.contrasena.get()  # Suponiendo que contrasena es un campo de texto

        # Conexion con la base de datos
        conexion = conectarMySql.MiConexion()

        # Verificar si el usuario existe en la base de datos
        usuario_bd = conexion.busca_user_Empleado(usuario)
    
        # Verificar si la contraseña es correcta para el usuario
        if usuario_bd:
            contrasena_bd = conexion.busca_password_Empleado(contrasena)
        
        ##cambiar mensajes

            if contrasena_bd:
                # Si el usuario y la contraseña son correctos
                messagebox.showinfo("Login exitoso", "¡Bienvenido!")
                sesionActual.sesionActualEmpleado.crearSesion(usuario, contrasena)
                return self.controller.show_frame(PantallaPrincipalEmpleado.MenuPrincipalUsuario)
                
            else:
                # Si la contraseña es incorrecta
                messagebox.showerror("Error", "Usuario y/o contraseña incorrecta")
        else:
        # Si el usuario no existe
            messagebox.showerror("Error", "Usuario y/o contraseña incorrecta")

