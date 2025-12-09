from cobham import *
import customtkinter as ctk
from PIL import Image

class LangtoAFD(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cobham Implementación | Lenguaje a AFD")
        self.geometry("900x550")
        self.grid_columnconfigure((0, 1), weight=1)


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

