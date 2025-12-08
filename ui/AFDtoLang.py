import customtkinter
from PIL import Image

import customtkinter
from PIL import Image

class AFDtoLang(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cobham Implementación | AFD a Lenguaje")
        self.geometry("900x550")
        self.grid_columnconfigure((0, 1), weight=1)
        self.button1 = customtkinter.CTkButton(self, text="Volver", command=self.volver)
        self.button1.grid(row=2, column=0, padx=30, pady=(0, 20), sticky="w")

    # Botón para volver
    def volver(self):
        print("Volver")

