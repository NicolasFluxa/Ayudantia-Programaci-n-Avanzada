"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                Estructurando Aplicaciones Tkinter con Clases (OOP)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Para aplicaciones Tkinter más grandes, es una buena práctica encapsular la
lógica de la GUI dentro de una clase. Esto mejora la organización,
reutilización y mantenibilidad del código.

Vamos a re-implementar la "Calculadora Simple de Suma" del ejercicio de la
Semana 8 (layout con grid), pero esta vez usando una clase.

1.  Define una clase, por ejemplo, `AppCalculadoraSuma`.
2.  El constructor `__init__(self, master_window)`:
    a.  `master_window` será la ventana raíz de Tkinter que se le pasará al crear la instancia.
    b.  Guarda `master_window` como un atributo de instancia (ej: `self.master = master_window`).
    c.  Configura el título y la geometría de `master_window`.
    d.  Llama a un método (ej: `self.crear_widgets()`) para construir la interfaz.
3.  Define un método `crear_widgets(self)`:
    a.  Dentro de este método, crea todos los widgets de la calculadora
        (Labels, Entries, Button para sumar, Label para resultado).
    b.  Almacena las referencias a los widgets que necesitarás manipular
        (como los Entries y la Label de resultado) como atributos de instancia
        (ej: `self.entry_num1`, `self.label_resultado`).
    c.  Organiza los widgets usando `grid()`.
    d.  Asigna el `command` del botón "Sumar" a otro método de la clase
        (ej: `self.realizar_suma`).
4.  Define el método `realizar_suma(self)`:
    a.  Este método contendrá la lógica para obtener los valores de
        `self.entry_num1` y `self.entry_num2`, calcular la suma y actualizar
        `self.label_resultado`.
    b.  Incluye manejo de `ValueError`.
5.  En el bloque principal del script (fuera de la clase, típicamente bajo
    `if __name__ == "__main__":`):
    a.  Crea la ventana raíz `tk.Tk()`.
    b.  Crea una instancia de tu clase `AppCalculadoraSuma`, pasándole la ventana raíz.
    c.  Inicia el `mainloop()` de la ventana raíz.
-------------------------------------------------------------------------------
"""
import tkinter as tk
from tkinter import messagebox


class AppCalculadoraSuma:
    def __init__(self, master_window):
        """
        Constructor de la aplicación calculadora.
        master_window es la ventana raíz de Tkinter.
        """
        self.master = master_window
        self.master.title("Calculadora OOP de Suma")
        self.master.geometry("320x220")
        self.master.configure(padx=15, pady=15)

        # Llamar al método para crear los widgets
        self.crear_widgets()

    def crear_widgets(self):
        """Crea y posiciona los widgets de la calculadora."""
        # --- Fila 0: Primer número ---
        tk.Label(self.master, text="Primer número:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_num1 = tk.Entry(self.master, width=15, font=("Arial", 11))
        self.entry_num1.grid(row=0, column=1, padx=5, pady=5)
        self.entry_num1.focus()  # Poner el foco en el primer Entry

        # --- Fila 1: Segundo número ---
        tk.Label(self.master, text="Segundo número:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_num2 = tk.Entry(self.master, width=15, font=("Arial", 11))
        self.entry_num2.grid(row=1, column=1, padx=5, pady=5)

        # --- Fila 2: Botón de Sumar ---
        boton_sumar = tk.Button(
            self.master,
            text="Sumar (+)",
            command=self.realizar_suma,  # Llama al método de la instancia
            font=("Arial", 10, "bold"),
            bg="lightgreen"
        )
        boton_sumar.grid(row=2, column=0, columnspan=2, padx=5, pady=12, sticky="ew")

        # --- Fila 3: Resultado ---
        tk.Label(self.master, text="Resultado:", font=("Arial", 11, "bold")).grid(row=3, column=0, padx=5, pady=5,
                                                                                  sticky="w")
        self.label_resultado = tk.Label(
            self.master,
            text="0.00",
            width=15,
            font=("Arial", 11, "bold"),
            relief="sunken",
            anchor="e",
            padx=5
        )
        self.label_resultado.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        # Configurar expansión de la columna de los Entry
        self.master.columnconfigure(1, weight=1)

    def realizar_suma(self):
        """Obtiene los números, los suma y muestra el resultado."""
        try:
            num1_str = self.entry_num1.get()
            num2_str = self.entry_num2.get()

            if not num1_str or not num2_str:
                messagebox.showwarning("Entrada Incompleta", "Por favor, ingresa ambos números.")
                return

            num1 = float(num1_str)
            num2 = float(num2_str)

            suma = num1 + num2
            self.label_resultado.config(text=f"{suma:.2f}")

        except ValueError:
            messagebox.showerror("Error de Entrada", "Ingresa solo números válidos.")
            self.label_resultado.config(text="Error")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")
            self.label_resultado.config(text="Error")


# --- Bloque Principal del Script ---
if __name__ == "__main__":
    print("Iniciando aplicación de calculadora (OOP)...")
    # a. Crear la ventana raíz
    ventana_principal = tk.Tk()
    # b. Crear una instancia de la aplicación, pasándole la ventana raíz
    app = AppCalculadoraSuma(ventana_principal)
    # c. Iniciar el bucle principal
    ventana_principal.mainloop()
    print("Aplicación de calculadora cerrada.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuáles son las principales ventajas de encapsular una aplicación Tkinter
    dentro de una clase en lugar de escribir todo el código de forma procedural?
2.  En el método `__init__`, ¿qué representa `master_window` y por qué se guarda
    como `self.master`?
3.  ¿Por qué los widgets como `self.entry_num1` y `self.label_resultado` se
    guardan como atributos de instancia (`self.nombre_widget`)?
4.  Cuando se define `command=self.realizar_suma` para el botón, ¿por qué
    `realizar_suma` debe ser un método de la clase (y por lo tanto tener `self`
    como primer parámetro)?
5.  Si quisieras añadir más funcionalidades a esta calculadora (resta, multiplicación),
    ¿cómo modificarías la clase `AppCalculadoraSuma` para incluirlas de forma organizada?
-------------------------------------------------------------------------------
"""