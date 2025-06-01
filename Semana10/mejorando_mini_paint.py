"""
-------------------------------------------------------------------------------
                              PROYECTO 02
                      Mejoras al Mini Paint Básico
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Toma como base el `proyecto_01_mini_paint_basico_tkinter.py` y añadele
al menos dos de las siguientes mejoras:

**Mejora 1: Selector de Grosor de Línea**
1.  Añade controles (pueden ser `Radiobutton`s o un `Scale` (slider) widget)
    en el `frame_controles` para permitir al usuario seleccionar diferentes
    grosores para el lápiz (ej: Fino (2px), Medio (5px), Grueso (10px)).
2.  Modifica la lógica de dibujo para que use el grosor seleccionado.

**Mejora 2: Herramienta de Borrador**
1.  Añade un botón "Borrador" en el `frame_controles`.
2.  Al seleccionar "Borrador", el "color de dibujo" debe cambiar al color de
    fondo del canvas (generalmente blanco).
3.  Considera que el grosor del borrador también podría ser ajustable.

**Mejora 3: (Opcional Avanzado) Paleta de Colores Más Amplia**
1.  En lugar de botones individuales para unos pocos colores, implementa una forma
    de seleccionar entre más colores. Podría ser usando `tkinter.colorchooser.askcolor()`
    que abre un diálogo estándar de selección de color.

**Instrucciones Adicionales:**
* Continúa usando la estructura de clases para la aplicación.
* Asegúrate de que la interfaz siga siendo intuitiva.
* Documenta los cambios y nuevas funciones que implementes.

Este archivo puede comenzar como una copia del anterior, y luego modificarlo.
Aquí se presentará una solución que implementa el Selector de Grosor y el Borrador.
-------------------------------------------------------------------------------
"""
import tkinter as tk
from tkinter import colorchooser  # Para la mejora opcional de paleta de colores


class AppMiniPaintMejorado:
    def __init__(self, master):
        self.master = master
        master.title("Mini Paint Mejorado")
        master.geometry("750x600")  # Un poco más grande para los controles

        # Atributos para el dibujo
        self.color_dibujo_actual = "black"
        self.color_fondo_canvas = "white"  # Guardar para el borrador
        self.grosor_linea_actual = 2
        self.ultima_pos_x = None
        self.ultima_pos_y = None

        # Variable de control para el grosor (si usamos Radiobuttons)
        self.var_grosor = tk.IntVar(value=self.grosor_linea_actual)

        self.crear_widgets_control()
        self.crear_canvas_dibujo()

    def crear_widgets_control(self):
        """Crea el frame de controles (colores, grosor, borrador, limpiar)."""
        frame_controles_principal = tk.Frame(self.master, relief=tk.RAISED, bd=2, padx=5, pady=5)
        frame_controles_principal.pack(side=tk.TOP, fill=tk.X)

        # --- Sección Colores ---
        frame_colores = tk.LabelFrame(frame_controles_principal, text="Colores", padx=5, pady=5)
        frame_colores.pack(side=tk.LEFT, padx=10)

        colores = {"Negro": "black", "Rojo": "red", "Verde": "green", "Azul": "blue", "Amarillo": "yellow"}
        for nombre_color, valor_color in colores.items():
            btn_color = tk.Button(
                frame_colores, text=nombre_color, bg=valor_color,
                fg="white" if valor_color in ["black", "blue", "green", "red"] else "black",
                width=8, command=lambda c=valor_color: self.seleccionar_color(c)
            )
            btn_color.pack(side=tk.LEFT, padx=2, pady=2)

        # (Opcional) Botón para paleta de colores avanzada
        btn_paleta = tk.Button(frame_colores, text="Más...", command=self.elegir_color_paleta, width=5)
        btn_paleta.pack(side=tk.LEFT, padx=2, pady=2)

        # --- Sección Grosor (Mejora 1) ---
        frame_grosor = tk.LabelFrame(frame_controles_principal, text="Grosor", padx=5, pady=5)
        frame_grosor.pack(side=tk.LEFT, padx=10)

        grosores = {"Fino": 2, "Medio": 5, "Grueso": 10, "Muy Grueso": 15}
        for texto_grosor, valor_grosor in grosores.items():
            rb_grosor = tk.Radiobutton(
                frame_grosor, text=texto_grosor, variable=self.var_grosor,
                value=valor_grosor, command=self.actualizar_grosor_desde_radio
            )
            rb_grosor.pack(anchor=tk.W)  # Alinea a la izquierda (West)

        # Alternativa con Scale:
        # self.scale_grosor = tk.Scale(frame_grosor, from_=1, to=20, orient=tk.HORIZONTAL,
        #                              label="Grosor:", command=self.actualizar_grosor_desde_scale)
        # self.scale_grosor.set(self.grosor_linea_actual)
        # self.scale_grosor.pack()

        # --- Sección Herramientas (Borrador, Limpiar) ---
        frame_herramientas = tk.LabelFrame(frame_controles_principal, text="Herramientas", padx=5, pady=5)
        frame_herramientas.pack(side=tk.LEFT, padx=10)

        btn_borrador = tk.Button(
            frame_herramientas, text="Borrador", width=10, command=self.activar_borrador
        )
        btn_borrador.pack(pady=3)

        btn_limpiar = tk.Button(
            frame_herramientas, text="Limpiar Canvas", width=12, command=self.limpiar_canvas
        )
        btn_limpiar.pack(pady=3)

    def crear_canvas_dibujo(self):
        self.canvas = tk.Canvas(self.master, bg=self.color_fondo_canvas, relief=tk.SUNKEN, bd=2)
        self.canvas.pack(expand=True, fill="both", padx=5, pady=5)
        self.canvas.bind("<Button-1>", self.iniciar_dibujo)
        self.canvas.bind("<B1-Motion>", self.dibujar)
        self.canvas.bind("<ButtonRelease-1>", self.detener_dibujo)

    def seleccionar_color(self, nuevo_color):
        self.color_dibujo_actual = nuevo_color
        print(f"Color de dibujo cambiado a: {nuevo_color}")

    def elegir_color_paleta(self):  # Mejora Opcional 3
        color_seleccionado = colorchooser.askcolor(title="Elige un color")
        if color_seleccionado and color_seleccionado[1]:  # askcolor retorna (rgb_tuple, hex_string)
            self.seleccionar_color(color_seleccionado[1])  # Usamos el string hexadecimal

    def actualizar_grosor_desde_radio(self):  # Mejora 1
        self.grosor_linea_actual = self.var_grosor.get()
        print(f"Grosor de línea cambiado a: {self.grosor_linea_actual}")

    # def actualizar_grosor_desde_scale(self, valor_scale): # Alternativa para Scale
    #     self.grosor_linea_actual = int(valor_scale)
    #     print(f"Grosor de línea cambiado a: {self.grosor_linea_actual}")

    def activar_borrador(self):  # Mejora 2
        """Activa el modo borrador cambiando el color de dibujo al color de fondo."""
        self.color_dibujo_actual = self.color_fondo_canvas
        print(f"Modo Borrador activado. (Dibujando con color {self.color_fondo_canvas})")
        # Podríamos también querer un grosor específico para el borrador
        # self.var_grosor.set(15) # Ejemplo: borrador más grueso por defecto
        # self.actualizar_grosor_desde_radio()

    def limpiar_canvas(self):
        self.canvas.delete("all")
        print("Canvas limpiado.")

    def iniciar_dibujo(self, event):
        self.ultima_pos_x = event.x
        self.ultima_pos_y = event.y

    def dibujar(self, event):
        if self.ultima_pos_x is not None and self.ultima_pos_y is not None:
            x, y = event.x, event.y
            self.canvas.create_line(
                self.ultima_pos_x, self.ultima_pos_y, x, y,
                fill=self.color_dibujo_actual,
                width=self.grosor_linea_actual,
                capstyle=tk.ROUND, smooth=tk.TRUE
            )
            self.ultima_pos_x = x
            self.ultima_pos_y = y

    def detener_dibujo(self, event):
        self.ultima_pos_x = None
        self.ultima_pos_y = None


# --- Bloque Principal ---
if __name__ == "__main__":
    print("Iniciando Mini Paint Mejorado...")
    ventana_raiz = tk.Tk()
    app_paint_mejorado = AppMiniPaintMejorado(ventana_raiz)
    ventana_raiz.mainloop()
    print("Mini Paint Mejorado cerrado.")

"""
-------------------------------------------------------------------------------
## PUNTOS CLAVE Y PREGUNTAS GUÍA:
## --------------------------------
1.  **Selector de Grosor:** ¿Cómo se utilizó `tk.Radiobutton` y `tk.IntVar` para
    permitir al usuario cambiar el grosor? ¿Qué otra widget podría haberse usado?
2.  **Herramienta Borrador:** ¿Cuál es la lógica detrás de la herramienta de borrador?
    ¿Cómo se simula "borrar" en un canvas?
3.  **Organización con `LabelFrame`:** ¿Cómo ayudó `LabelFrame` a organizar
    visualmente los nuevos grupos de controles?
4.  **(Si implementaste la paleta de colores avanzada)** ¿Cómo funciona
    `tkinter.colorchooser.askcolor()`? ¿Qué tipo de valor retorna?
5.  **Modularidad:** ¿Qué tan fácil fue añadir estas nuevas funcionalidades a la
    clase `AppMiniPaint` existente? ¿Qué principios de la POO facilitaron esto?
6.  **Más Mejoras (Ideas):**
    a. ¿Cómo podrías guardar el dibujo actual como una imagen (esto podría requerir
       bibliotecas externas como Pillow, o investigar el método `postscript` del canvas
       y luego convertirlo)?
    b. ¿Cómo implementarías una funcionalidad de "Deshacer" el último trazo? (Pista:
       necesitarías almacenar los trazos o los IDs de los ítems del canvas).
-------------------------------------------------------------------------------
"""