import customtkinter
from PIL import Image
from LangtoAFD import LangtoAFD
from AFDtoLang import AFDtoLang

customtkinter.set_default_color_theme("dark-blue")  

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cobham Implementación")
        self.geometry("900x550")
        self.grid_columnconfigure((0, 1), weight=1)

        self.img = customtkinter.CTkImage(light_image=Image.open("img\icono.png"),
                                  dark_image=Image.open("img\icono.png"),
                                  size=(200, 200))
        self.img_label = customtkinter.CTkLabel(self, image=self.img, text="") 
        self.img_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        self.label = customtkinter.CTkLabel(self, text="Implementación Cobham\nTranforma Autómatas a lenguajes o lenguajes a Autómatas", fg_color="transparent", font=("Roboto",30))
        self.label.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        
        self.button1 = customtkinter.CTkButton(self, text="AFDO -> Lenguaje", command=self.abrirAFDtoLang)
        self.button1.grid(row=2, column=0, padx=30, pady=(0, 20), sticky="w")
        self.button2 = customtkinter.CTkButton(self, text="Lenguaje -> AFDO", command=self.abrirLangtoAFD)
        self.button2.grid(row=2, column=1, padx=30, pady=(0, 20), sticky="w")
        
    def abrirLangtoAFD(self):
        # self.destroy()
        window2_main = LangtoAFD()
        window2_main.mainloop()
    def abrirAFDtoLang(self):
        
        window2_main = AFDtoLang()
        window2_main.mainloop()

app = App()
app.mainloop()