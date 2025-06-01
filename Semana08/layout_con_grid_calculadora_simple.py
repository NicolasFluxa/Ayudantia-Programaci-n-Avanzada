"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                 Layout con `grid()` - Calculadora Simple (Suma)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
El gestor de geometría `grid()` permite organizar widgets en una estructura
de filas y columnas, ofreciendo más control que `pack()`.
Crearemos una interfaz muy simple para una calculadora que solo sume dos números.

1.  Crea una ventana raíz de Tkinter.
2.  Crea los siguientes widgets:
    a.  Una `Label` con el texto "Primer número:".
    b.  Un `Entry` para que el usuario ingrese el primer número.
    c.  Una `Label` con el texto "Segundo número:".
    d.  Un `Entry` para el segundo número.
    e.  Una `Label` para el texto "Resultado:".
    f.  Una `Label` (inicialmente vacía o con "0") para MOSTRAR el resultado.
    g.  Un `Button` con el texto "Sumar".
3.  Organiza estos widgets usando el método `grid()`:
    * La primera Label y el primer Entry en la fila 0.
    * La segunda Label y el segundo Entry en la fila 1.
    * El botón "Sumar" en la fila 2 (puede ocupar varias columnas o estar centrado).
    * La Label "Resultado:" y la Label para el resultado en la fila 3.
    Usa opciones como `row`, `column`, `sticky` (para alineación), `padx`, `pady`.
4.  Define una función `realizar_suma()`:
    a.  Debe obtener los valores de los dos `Entry` (recordar convertirlos a número).
    b.  Calcular la suma.
    c.  Actualizar el texto de la `Label` del resultado.
    d.  Manejar posibles `ValueError` si la entrada no es numérica.
5.  Asocia `realizar_suma()` al `command` del botón "Sumar".
6.  Inicia el `mainloop`.
-------------------------------------------------------------------------------
"""
import tkinter as tk
from tkinter import messagebox  # Para mostrar errores de forma más visual

# Variables para los widgets que necesitamos referenciar
entry_num1 = None
entry_num2 = None
label_resultado_valor = None


def realizar_suma():
    """Obtiene los números de los Entry, los suma y muestra el resultado."""
    global entry_num1, entry_num2, label_resultado_valor

    try:
        num1_str = entry_num1.get()
        num2_str = entry_num2.get()

        if not num1_str or not num2_str:  # Verificar si están vacíos
            messagebox.showwarning("Entrada Vacía", "Por favor, ingresa ambos números.")
            return

        num1 = float(num1_str)
        num2 = float(num2_str)

        suma = num1 + num2
        label_resultado_valor.config(text=f"{suma:.2f}")  # Mostrar con 2 decimales

    except ValueError:
        messagebox.showerror("Error de Entrada", "Por favor, ingresa solo números válidos.")
        label_resultado_valor.config(text="Error")
    except Exception as e:
        messagebox.showerror("Error Inesperado", f"Ocurrió un error: {e}")
        label_resultado_valor.config(text="Error")


# 1. Crear ventana raíz
raiz = tk.Tk()
raiz.title("Calculadora de Suma con grid()")
raiz.geometry("300x200")  # Ajustar tamaño según necesidad

# Configurar padding general para la ventana raíz para que los widgets no estén pegados a los bordes
raiz.configure(padx=10, pady=10)

# 2. Crear widgets y 3. Organizar con grid()

# Fila 0
label_num1 = tk.Label(raiz, text="Primer número:")
label_num1.grid(row=0, column=0, padx=5, pady=5, sticky="w")  # sticky="w" (west) para alinear a la izquierda

entry_num1_ref = tk.Entry(raiz, width=15)
entry_num1_ref.grid(row=0, column=1, padx=5, pady=5)
globals()['entry_num1'] = entry_num1_ref

# Fila 1
label_num2 = tk.Label(raiz, text="Segundo número:")
label_num2.grid(row=1, column=0, padx=5, pady=5, sticky="w")

entry_num2_ref = tk.Entry(raiz, width=15)
entry_num2_ref.grid(row=1, column=1, padx=5, pady=5)
globals()['entry_num2'] = entry_num2_ref

# Fila 2
boton_sumar = tk.Button(raiz, text="Sumar", command=realizar_suma, width=10)
# columnspan=2 para que el botón ocupe el espacio de dos columnas
# sticky="ew" para que se expanda horizontalmente (east-west)
boton_sumar.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

# Fila 3
label_resultado_texto = tk.Label(raiz, text="Resultado:")
label_resultado_texto.grid(row=3, column=0, padx=5, pady=5, sticky="w")

label_resultado_valor_ref = tk.Label(raiz, text="0.00", width=15, relief="sunken",
                                     anchor="e")  # anchor="e" (east) para alinear texto a la derecha
label_resultado_valor_ref.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
globals()['label_resultado_valor'] = label_resultado_valor_ref

# Configurar pesos de las columnas para que el Entry se expanda si la ventana se redimensiona
# La columna 1 (donde están los Entry) se expandirá
raiz.columnconfigure(1, weight=1)

# 6. Iniciar bucle principal
print("Calculadora simple (suma) lista.")
raiz.mainloop()
print("Calculadora cerrada.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la diferencia principal entre `pack()` y `grid()` como gestores de geometría?
    ¿En qué situaciones `grid()` podría ser más ventajoso?
2.  Explica qué hacen las opciones `row`, `column`, `columnspan` y `sticky` en el método `grid()`.
    ¿Qué significan valores como `sticky="w"` o `sticky="ew"`?
3.  En la función `realizar_suma()`, ¿por qué es importante usar `try-except` al
    convertir las entradas de los `Entry` a números?
4.  La línea `raiz.columnconfigure(1, weight=1)` se usa para el comportamiento de redimensión.
    ¿Qué efecto tiene `weight=1` en una columna (o fila con `rowconfigure`)?
5.  ¿Cómo modificarías esta calculadora para que también tenga un botón "Restar" y
    realice la resta de los dos números, mostrando el resultado en la misma etiqueta?
-------------------------------------------------------------------------------
"""