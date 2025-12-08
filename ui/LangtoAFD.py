import customtkinter
from PIL import Image

class LangtoAFD(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cobham Implementación | Lenguaje a AFD")
        self.geometry("900x550")
        self.grid_columnconfigure((0, 1), weight=1)
        self.button1 = customtkinter.CTkButton(self, text="Volver", command=self.volver)
        self.button1.grid(row=2, column=0, padx=30, pady=(0, 20), sticky="w")

    


    # Botón para volver
    def volver(self):
        print("Volver")

