from customtkinter import *
import Login
from tkinter import font, Tk

class MainApp(CTk):
    
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("1280x720")
        self.resizable(False, False)

  
        
        # Crear contenedor para las interfaces y darle un fondo blanco
        self.container = CTkFrame(self, fg_color="white")  # Fondo blanco en el contenedor principal
        self.container.pack(fill="both", expand=True)
        
        # Diccionario para almacenar las interfaces
        self.frames = {}
        
        # Inicializar con la interfaz principal
        self.show_frame(Login.MainLogin)

    def show_frame(self, frame_class):
        # Ocultar el frame actual si ya hay uno visible
        for frame in self.frames.values():
            frame.pack_forget()

        # Crear la interfaz si no ha sido creada
        if frame_class not in self.frames:
            frame = frame_class(self.container, self)
            self.frames[frame_class] = frame
            frame.pack(fill="both", expand=True)

        # Mostrar la interfaz solicitada
        frame = self.frames[frame_class]
        frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()