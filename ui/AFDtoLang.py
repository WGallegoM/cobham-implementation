import customtkinter as ctk
from cobham import *
from PIL import Image


class VentanaResultados(ctk.CTkToplevel):
    def __init__(self, morfismo, estadoInicial):
        super().__init__()
        
        self.title("Resultados del Autómata | Morfismo Generado")
        self.geometry("400x500")
        
        # Hacemos que la ventana sea "modal" (bloquea la anterior hasta cerrar esta)
        # Si no quieres que bloquee, quita las siguientes dos líneas:
        self.grab_set() 
        self.focus()

        lbl_titulo = ctk.CTkLabel(self, text="Autómata Procesado", font=("Arial", 18, "bold"))
        lbl_titulo.pack(pady=20)

        # Usamos un cuadro de texto para mostrar el resumen
        self.texto_resumen = ctk.CTkTextbox(self, width=350, height=200)
        self.texto_resumen.pack(pady=10)

        # Construimos el texto a mostrar
        resumen = morfismo._info()
        
        self.texto_resumen.insert("0.0", resumen)
        self.texto_resumen.configure(state="disabled") # Para que sea solo lectura

        # Imprime el morfismo aplicado 2^n veces
        self.status_label = ctk.CTkLabel(self, text=f"Primeros k^4 digitos: " + morfismo.apply(estadoInicial,4), text_color="green")
        self.status_label.pack(pady=5)

class AFDtoLang(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Formulario de Autómata")
        self.geometry("800x700")

        # Variable para almacenar K
        self.k_valor = 0

        # En lugar de llamar a setup_ui directamente, llamamos a la pantalla de entrada
        self.pantalla_pedir_k()
        # Referencia para la ventana hija
        self.ventana_hija = None

    def pantalla_pedir_k(self):
        """Muestra solo el input para K al inicio"""
        
        # Frame central para que se vea ordenado
        self.frame_inicial = ctk.CTkFrame(self)
        self.frame_inicial.place(relx=0.5, rely=0.5, anchor="center")

        lbl = ctk.CTkLabel(self.frame_inicial, text="Ingrese el valor de K (número de estados):", font=("roboto", 16, "bold"))
        lbl.pack(pady=20, padx=20)

        self.entry_k_inicial = ctk.CTkEntry(self.frame_inicial, placeholder_text="Ej: 3", width=200)
        self.entry_k_inicial.pack(pady=10)

        btn_continuar = ctk.CTkButton(self.frame_inicial, text="Continuar", command=self.validar_y_avanzar)
        btn_continuar.pack(pady=20)

    def validar_y_avanzar(self):
        """Valida que K sea un número y carga la UI principal"""
        try:
            valor = int(self.entry_k_inicial.get())
            if valor < 1:
                raise ValueError("El número debe ser mayor a 0")
            
            self.k_valor = valor
            
            # 1. Destruir el frame inicial para limpiar la ventana
            self.frame_inicial.destroy()
            
            # 2. Ejecutar la UI principal ahora que tenemos el dato
            self.setup_ui()
            
        except ValueError:
            # Usamos un print o messagebox si no es un número válido
            print("Error: Por favor ingrese un número entero válido.")

    def setup_ui(self):
        """Construye el formulario grande basado en K"""
        
        # Scrollable Frame principal
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=480, height=650)
        self.scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Mostrar el valor de K seleccionado (solo lectura)
        self.lbl_info = ctk.CTkLabel(self.scroll_frame, text=f"Configuración para K = {self.k_valor}", text_color="cyan")
        self.lbl_info.pack(pady=5)

        # --- 2. Tabla Kx1 (Estados) ---
        # Ahora usamos self.k_valor para definir las filas (rows)
        self.lbl_estados = ctk.CTkLabel(self.scroll_frame, text=f"2. Estados (Tabla {self.k_valor}x1)", font=("roboto", 14, "bold"))
        self.lbl_estados.pack(pady=(20, 5), anchor="w")
        
        self.matrix_estados = self.crear_matriz_entradas(rows=self.k_valor, cols=1, headers=["Estado"])

        # --- 3. Estado Inicial ---
        self.lbl_inicial = ctk.CTkLabel(self.scroll_frame, text="3. Estado Inicial", font=("roboto", 14, "bold"))
        self.lbl_inicial.pack(pady=(20, 5), anchor="w")

        self.entry_inicial = ctk.CTkEntry(self.scroll_frame, placeholder_text="Ej: q0")
        self.entry_inicial.pack(pady=5, fill="x")

        # --- 4. Función Transición (Tabla Kx2) ---
        # Asumimos 2 columnas de entrada (0 y 1), pero K filas de estados
        self.lbl_transicion = ctk.CTkLabel(self.scroll_frame, text=f"4. Función Transición (Tabla {self.k_valor}x2)", font=("roboto", 14, "bold"))
        self.lbl_transicion.pack(pady=(20, 5), anchor="w")

        self.matrix_transicion = self.crear_matriz_entradas(rows=self.k_valor, cols=2, headers=["In 0", "In 1"])

        # --- 5. Función de Salida (Tabla Kx1) ---
        self.lbl_salida = ctk.CTkLabel(self.scroll_frame, text=f"5. Función de Salida (Tabla {self.k_valor}x1)", font=("roboto", 14, "bold"))
        self.lbl_salida.pack(pady=(20, 5), anchor="w")

        self.matrix_salida = self.crear_matriz_entradas(rows=self.k_valor, cols=1, headers=["Salida"])

        # --- Botón de Guardar ---
        self.btn_guardar = ctk.CTkButton(self.scroll_frame, text="Procesar Datos", command=self.obtener_datos)
        self.btn_guardar.pack(pady=30)

    def crear_matriz_entradas(self, rows, cols, headers=None):
        frame_contenedor = ctk.CTkFrame(self.scroll_frame)
        frame_contenedor.pack(pady=5)
        entradas = []

        if headers:
            for j, header in enumerate(headers):
                lbl = ctk.CTkLabel(frame_contenedor, text=header, text_color="gray")
                lbl.grid(row=0, column=j, padx=5, pady=2)

        start_row = 1 if headers else 0

        for i in range(rows):
            fila_entradas = []
            for j in range(cols):
                entry = ctk.CTkEntry(frame_contenedor, width=120, placeholder_text=f"({i},{j})")
                entry.grid(row=i+start_row, column=j, padx=5, pady=5)
                fila_entradas.append(entry)
            entradas.append(fila_entradas)
        return entradas

    def obtener_datos(self):
        print(f"--- DATOS PARA K={self.k_valor} ---")
        print(f"Estado Inicial: {self.entry_inicial.get()}")
        estadoInicial = self.entry_inicial.get()
        # Recuperamos datos dinámicamente
        
        estadosSinProcesar = [[e.get() for e in row] for row in self.matrix_estados]
        # limpiar estados
        estados = []
        for i in estadosSinProcesar:
            estados.append(i[0])
        transicion = [[e.get() for e in row] for row in self.matrix_transicion]
        # limpiar salida
        salidaSinProcesar = [[e.get() for e in row] for row in self.matrix_salida]
        salida = []
        for i in salidaSinProcesar:
            salida.append(i[0])
        
        print("Matriz Estados:", estados)
        print("Matriz Transición:", transicion)
        print("Matriz Salida:", salida)

        # Generar lenguaje a partir de información dada
        lenguaje = output_automata(
            self.k_valor,
            estados,
            estadoInicial,
            transicion,
            k_language(self.k_valor),
            salida
        )
        morfismoGenerado = automataToMorphism(lenguaje)
        print(morfismoGenerado._info())
        # mostrar en una nueva ventana
        if self.ventana_hija is None or not self.ventana_hija.winfo_exists():
            # 3. Crear la nueva ventana pasando los datos
            self.ventana_hija = VentanaResultados(
                morfismoGenerado,
                estadoInicial
            )
        else:
            self.ventana_hija.focus() # Si ya existe, traer al frente
        
        