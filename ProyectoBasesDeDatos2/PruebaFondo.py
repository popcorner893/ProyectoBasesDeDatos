import customtkinter as ctk
from Utilidades import *



class CollapsiblePanel(ctk.CTkFrame):
    def __init__(self, parent, title, *args, **kwargs):
        super().__init__(parent, fg_color= "#DEEDFD", *args, **kwargs)

        #Vista colapsada

        vistaColapsadaFrame = CTkFrame(self, fg_color= "transparent")
        vistaColapsadaFrame.pack(fill="x", padx=5, pady=5, expand=True)

        self.titulo = smallText(vistaColapsadaFrame, title)
        self.titulo.pack(side = "left", padx = 20)
        
        # Botón para expandir/colapsar el contenido
        self.toggle_button = iconoClickable(vistaColapsadaFrame, "ExpandIcon", 35, 35, self.toggle)
        self.toggle_button.pack(side="right", padx=20)
        
        # Frame interno que contiene el contenido del panel
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="x", padx=5, pady=5)

        
        
        # Iniciar colapsado
        self._is_collapsed = True
        self.content_frame.pack_forget()

    def toggle(self):
        """Expandir o colapsar el contenido del panel."""
        if self._is_collapsed:
            self.content_frame.pack(fill="x", padx=5, pady=5)
        else:
            self.content_frame.pack_forget()
        self._is_collapsed = not self._is_collapsed





