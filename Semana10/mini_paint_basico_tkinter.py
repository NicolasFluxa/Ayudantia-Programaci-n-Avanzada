"""
-------------------------------------------------------------------------------
                              PROYECTO 01
                        Mini Paint Básico con Tkinter
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Desarrolla una aplicación "Mini Paint" muy simple que permita al usuario
dibujar a mano alzada sobre un lienzo (Canvas) con el mouse.

**Funcionalidades Requeridas:**

1.  **Ventana Principal con Canvas:**
    * Un widget `Canvas` de un tamaño considerable (ej: 600x400) que será el área de dibujo.
    * Debe tener un color de fondo (ej: blanco).

2.  **Herramienta de Dibujo (Lápiz):**
    * Cuando el usuario presiona el botón izquierdo del mouse (`<Button-1>`)
        sobre el canvas, se debe registrar la posición inicial.
    * Mientras el usuario mueve el mouse con el botón izquierdo presionado
        (`<B1-Motion>`), se deben dibujar pequeñas líneas (o círculos/óvalos muy pequeños)
        entre la posición anterior del mouse y la actual, creando un efecto de dibujo.
    * Se necesitarán variables para guardar la posición anterior del mouse.

3.  **Controles (pueden ser botones fuera del canvas o un menú simple):**
    * **Selección de Color:** Al menos 3 botones para cambiar el color del lápiz
        (ej: "Rojo", "Verde", "Azul", "Negro"). Al presionar un botón, el color
        de dibujo actual cambia.
    * **Botón "Limpiar Canvas":** Borra todo el contenido del canvas.

4.  **Estructura de Clase:**
    * Organiza la aplicación dentro de una clase (ej: `AppMiniPaint`).

**Pistas:**
* Widget `Canvas`:
    * `create_line(x0, y0, x1, y1, fill="color", width=grosor)`
    * `create_oval(x0, y0, x1, y1, fill="color", outline="color")` (para puntos gruesos)
    * `delete("all")` para limpiar el canvas.
* Eventos del Mouse en Canvas:
    * `canvas.bind("<Button-1>", funcion_inicio_dibujo)`
    * `canvas.bind("<B1-Motion>", funcion_dibujar)`
    * `canvas.bind("<ButtonRelease-1>", funcion_fin_dibujo)` (opcional, para resetear la última posición)
    * Las funciones de evento reciben un objeto `event` que tiene atributos
        `event.x` y `event.y` con las coordenadas del mouse.
-------------------------------------------------------------------------------
"""
import tkinter as tk


class AppMiniPaint:
    def __init__(self, master):
        self.master = master
        master.title("Mini Paint Básico")
        master.geometry("700x550")

        # Atributos para el dibujo
        self.color_dibujo_actual = "black"
        self.grosor_linea_actual = 2
        self.ultima_pos_x = None
        self.ultima_pos_y = None

        self.crear_widgets_control()
        self.crear_canvas_dibujo()

    def crear_widgets_control(self):
        """Crea el frame de controles (botones de color, limpiar)."""
        frame_controles = tk.Frame(self.master, relief=tk.RAISED, bd=2, padx=5, pady=5)
        frame_controles.pack(side=tk.TOP, fill=tk.X)

        tk.Label(frame_controles, text="Color:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)

        colores = {"Negro": "black", "Rojo": "red", "Verde": "green", "Azul": "blue", "Amarillo": "yellow"}
        for nombre_color, valor_color in colores.items():
            # Usamos lambda para pasar el valor_color a la función en el momento de la definición del command
            btn_color = tk.Button(
                frame_controles,
                text=nombre_color,
                bg=valor_color,  # Para que el botón mismo muestre el color
                fg="white" if valor_color in ["black", "blue", "green", "red"] else "black",  # Contraste de texto
                width=8,
                command=lambda c=valor_color: self.seleccionar_color(c)
            )
            btn_color.pack(side=tk.LEFT, padx=3)

        btn_limpiar = tk.Button(
            frame_controles,
            text="Limpiar Canvas",
            width=12,
            command=self.limpiar_canvas
        )
        btn_limpiar.pack(side=tk.RIGHT, padx=20)  # A la derecha

    def crear_canvas_dibujo(self):
        """Crea el widget Canvas para dibujar."""
        self.canvas = tk.Canvas(self.master, bg="white", relief=tk.SUNKEN, bd=2)
        self.canvas.pack(expand=True, fill="both", padx=5, pady=5)

        # --- Vincular eventos del mouse al Canvas ---
        self.canvas.bind("<Button-1>", self.iniciar_dibujo)  # Clic izquierdo presionado
        self.canvas.bind("<B1-Motion>", self.dibujar)  # Movimiento con clic izquierdo presionado
        self.canvas.bind("<ButtonRelease-1>", self.detener_dibujo)  # Clic izquierdo liberado

    def seleccionar_color(self, nuevo_color):
        """Cambia el color de dibujo actual."""
        self.color_dibujo_actual = nuevo_color
        print(f"Color de dibujo cambiado a: {nuevo_color}")

    def limpiar_canvas(self):
        """Borra todo el contenido del Canvas."""
        self.canvas.delete("all")  # "all" es una etiqueta especial que se refiere a todos los ítems del canvas
        print("Canvas limpiado.")

    def iniciar_dibujo(self, event):
        """Se llama al presionar el botón izquierdo del mouse. Guarda la posición inicial."""
        self.ultima_pos_x = event.x
        self.ultima_pos_y = event.y
        # print(f"Inicio dibujo en: ({event.x}, {event.y})")

    def dibujar(self, event):
        """Se llama al mover el mouse con el botón izquierdo presionado."""
        if self.ultima_pos_x is not None and self.ultima_pos_y is not None:
            x, y = event.x, event.y
            # Dibuja una línea desde la última posición hasta la actual
            self.canvas.create_line(
                self.ultima_pos_x, self.ultima_pos_y, x, y,
                fill=self.color_dibujo_actual,
                width=self.grosor_linea_actual,
                capstyle=tk.ROUND,  # Extremos de línea redondeados
                smooth=tk.TRUE  # Línea suavizada
            )
            # Actualizar la última posición
            self.ultima_pos_x = x
            self.ultima_pos_y = y
            # print(f"Dibujando a: ({x}, {y})")

    def detener_dibujo(self, event):
        """Se llama al liberar el botón izquierdo del mouse. Resetea la última posición."""
        self.ultima_pos_x = None
        self.ultima_pos_y = None
        # print("Fin del trazo de dibujo.")


# --- Bloque Principal ---
if __name__ == "__main__":
    print("Iniciando Mini Paint Básico...")
    ventana_raiz = tk.Tk()
    app_paint = AppMiniPaint(ventana_raiz)
    ventana_raiz.mainloop()
    print("Mini Paint cerrado.")

"""
-------------------------------------------------------------------------------
## PUNTOS CLAVE Y PREGUNTAS GUÍA:
## --------------------------------
1.  ¿Cuál es el propósito del widget `Canvas`? ¿Qué tipo de elementos gráficos
    puedes dibujar en él?
2.  Explica los eventos del mouse utilizados (`<Button-1>`, `<B1-Motion>`,
    `<ButtonRelease-1>`) y qué información proporciona el objeto `event`
    que reciben las funciones callback.
3.  En `dibujar()`, ¿por qué es importante actualizar `self.ultima_pos_x` y
    `self.ultima_pos_y` en cada paso?
4.  La función `lambda c=valor_color: self.seleccionar_color(c)` se usa en los
    botones de color. ¿Por qué se necesita `lambda` aquí? ¿Qué problema soluciona
    al pasar argumentos a una función `command`?
5.  ¿Cómo funciona `self.canvas.delete("all")`?
6.  **Ideas para Mejoras (a discutir o implementar en el siguiente ejercicio):**
    a. ¿Cómo añadirías una opción para cambiar el grosor del lápiz?
    b. ¿Cómo implementarías una herramienta de "borrador" (pista: dibujar con
       el color de fondo del canvas)?
    c. ¿Sería posible dibujar otras formas (rectángulos, óvalos) en lugar de
       solo líneas a mano alzada? ¿Cómo cambiarías la lógica?
-------------------------------------------------------------------------------
"""