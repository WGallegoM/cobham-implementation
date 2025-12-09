from cobham import *
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from pythomata import SimpleDFA
import io
import cairosvg

class LangtoAFD(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cobham Implementación | Lenguaje a AFD")
        self.geometry("900x550")
        self.grid_columnconfigure((0, 1), weight=1)

        self.toplevel_window = None


        # --- Table Configuration ---
        self.rows = 2
        self.cols = 2
        self.headers = ["Entrada", "Imagen Morfismo"]
        self.entry_widgets = []  # List to hold the entry widgets

        # --- Table Frame ---
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Configure the grid inside the table_frame
        for i in range(self.cols):
            self.table_frame.grid_columnconfigure(i, weight=1)

        # --- Create Table Headers (Labels) ---
        for col, header_text in enumerate(self.headers):
            header_label = ctk.CTkLabel(
                self.table_frame,
                text=header_text,
                font=ctk.CTkFont(weight="bold")
            )
            header_label.grid(row=0, column=col, padx=10, pady=(10, 5), sticky="ew")

        # --- Create Input Table (CTkEntry Widgets) ---
        for row in range(self.rows):
            row_entries = []
            for col in range(self.cols):
                if row == 0 and col == 0:
                    entry = ctk.CTkEntry(
                    self.table_frame,
                    placeholder_text=f"Estado Inicial"
                )
                else:
                    entry = ctk.CTkEntry(
                        self.table_frame,
                        placeholder_text=""
                    )
                entry.grid(row=row + 1, column=col, padx=10, pady=5, sticky="ew")
                row_entries.append(entry)
            self.entry_widgets.append(row_entries)
        
        self.status_label = ctk.CTkLabel(self, text="", text_color="grey")
        self.status_label.grid(row=2, column=0, padx=20, pady=5)

        # --- Submit Button ---
        self.submit_button = ctk.CTkButton(
            self,
            text="Procesar Morfismo",
            command=self.get_table_data
        )
        self.submit_button.grid(row=1, column=0, padx=20, pady=(0, 20))


    def abrir_nueva_ventana(self):
        # 1. Crear la ventana secundaria (Toplevel)
        nueva_ventana = tk.Toplevel()
        nueva_ventana.title("Ventana con Imagen")
        nueva_ventana.geometry("900x700")

        try:
            # 2. Cargar la imagen
            # NOTA: Solo funciona con .png o .gif nativamente
            imagen = tk.PhotoImage(file="salida.png")

            # 3. Mostrar la imagen en una etiqueta (Label)
            label_imagen = tk.Label(nueva_ventana, image=imagen)
            label_imagen.pack(expand=True)

            # 4. ¡CRÍTICO! Guardar una referencia de la imagen
            # Si no haces esto, Python borrará la imagen de la memoria y no se verá.
            label_imagen.image = imagen
            
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            lbl_error = tk.Label(nueva_ventana, text="No se encontró el archivo 'mi_imagen.png'")
            lbl_error.pack()

    def get_table_data(self):

        try:
            data = []
            morfismo = {}
            for row_entries in self.entry_widgets:
                row_data = [entry.get() for entry in row_entries]
                data.append(row_data)
                morfismo[row_data[0]] = row_data[1]
            """
            print("--- Información del morfismo ---")
            for i, row in enumerate(data):
                print(f"Fila {i+1}: {row}")
            print("----------------------------")
            """

            print("Morfismo generado", morfismo)


            morfismoGenerado = morphism(morfismo)
            print(morfismoGenerado._info())
            # Estado inicial es el primero que ingresa
            estadoInicial = data[0][0]
            automataGenerado = morphismToAutomata(morfismoGenerado, estadoInicial)

            print(automataGenerado._info())
            # Imprime el morfismo aplicado 2^n veces
            self.status_label.configure(text=f"Primeros k^4 digitos: " + morfismoGenerado.apply(estadoInicial,4), text_color="green")

            # Usar pythomata para generar automata
            print(automataGenerado.transition_function)
            funcionTransicion = {
                '0' : {
                    '0': '1',
                    '1':'0' 
                },
                '1':{
                    '0':'0',
                    '1':'1'
                }
            }
            print(automataGenerado.output_function)
            print(set(automataGenerado.states))
            print(set(automataGenerado.language))
            print(estadoInicial)

            # Constuir DFA y grafica
            dfa = SimpleDFA(set(automataGenerado.states), set(automataGenerado.language), estadoInicial, set(automataGenerado.states), funcionTransicion )
            graph = dfa.trim().to_graphviz()
            graph.render("salida")

            # Pasar de svg a png
            png_data = cairosvg.svg2png(url="salida.svg" , write_to="salida.png",output_width=800, output_height=600)
            self.abrir_nueva_ventana()
            
            

        except ValueError as e:
            # 3. ERROR HANDLER: If the input cannot be converted to an integer
            self.status_label.configure(text=e, text_color="red")



        # Optional: Clear the entries after submission
        # self.clear_table()

    

    def clear_table(self):
        """Clears the text in all CTkEntry widgets."""
        for row_entries in self.entry_widgets:
            for entry in row_entries:
                entry.delete(0, tk.END)

        self.button1 = customtkinter.CTkButton(self, text="Volver", command=self.volver)
        self.button1.grid(row=3, column=0, padx=30, pady=(0, 20), sticky="w")

    # Botón para volver
    def volver(self):
        print("Volver")

class ImageWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Root = Tk()
        window = Root.TopLevel()

        self.title("Image Display")
        self.geometry("900x700")

        # 1. Load the image using PIL
        # Replace "path_to_your_image.jpg" with your actual file path
        image_path = "salida.png" 
        
        try:
            png_data = cairosvg.svg2png(url="salida.svg" , write_to=image_path,output_width=800, output_height=600)

            # 2. Open the bytes as a PIL Image
            pil_image = Image.open(image_path)
            
            # 2. Convert to CTkImage
            # 'size' argument is mandatory to set the display size
            self.my_image = ctk.CTkImage(light_image=pil_image, 
                                         dark_image=pil_image, 
                                         size=(300, 300))
            # 3. Display in a Label
            self.image_label = ctk.CTkLabel(self, text="", image=self.my_image)
            self.image_label.pack(expand=True, fill="both", padx=20, pady=20)

            # 3. Display in a Label
            self.image_label = ctk.CTkLabel(self, text="", image=self.my_image)
            self.image_label.pack(expand=True, fill="both", padx=20, pady=20)
            
        except FileNotFoundError:
            print(f"Error: Could not find image at {image_path}")
            self.error_label = ctk.CTkLabel(self, text="Image not found!")
            self.error_label.pack(pady=20)