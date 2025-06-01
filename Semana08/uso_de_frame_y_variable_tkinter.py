"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                 Uso de `Frame` y Variables de Control Tkinter (`StringVar`)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Los `Frame` son widgets contenedores que sirven para agrupar y organizar otros
widgets. Las `StringVar` (y otras como `IntVar`, `BooleanVar`) son variables
especiales de Tkinter que se pueden vincular a widgets para que se actualicen
automáticamente.

1.  Crea una ventana raíz de Tkinter.
2.  Crea una `StringVar` de Tkinter llamada `texto_compartido`. Inicialízala
    con un valor como "Texto inicial".
3.  Crea un `Frame` superior (`frame_arriba`). Empaquétalo en la raíz, haciendo
    que ocupe todo el ancho disponible (`fill='x'`).
    a.  Dentro de `frame_arriba`, crea una `Label` con el texto "Entrada:".
    b.  Dentro de `frame_arriba`, crea un `Entry` cuyo texto esté VINCULADO
        a `texto_compartido` usando la opción `textvariable`.
    c.  Empaqueta la Label y el Entry en `frame_arriba` (puedes usar `pack(side='left')`).

4.  Crea un `Frame` inferior (`frame_abajo`). Empaquétalo en la raíz (`fill='x'`).
    a.  Dentro de `frame_abajo`, crea una `Label` cuyo texto también esté VINCULADO
        a `texto_compartido` usando `textvariable`.
    b.  Empaqueta esta Label en `frame_abajo`.

5.  Define una función `actualizar_texto_variable()`:
    a.  Esta función debe cambiar el valor de `texto_compartido` usando su
        método `set()` (ej: a "Texto actualizado desde el botón!").
6.  Crea un `Button` en la ventana raíz (o en uno de los frames) con el texto
    "Actualizar Variable" y asócialo a la función `actualizar_texto_variable()`.
    Empaquétalo.

7.  Observa: Al escribir en el `Entry`, la `Label` de abajo se actualiza.
    Al presionar el botón, tanto el `Entry` como la `Label` se actualizan.
-------------------------------------------------------------------------------
"""
import tkinter as tk

# Variable de control de Tkinter
texto_compartido_global = None

def actualizar_texto_variable():
    """Actualiza el valor de la StringVar."""
    global texto_compartido_global
    if texto_compartido_global:
        nuevo_valor = "¡Texto actualizado desde el botón! 🎉"
        texto_compartido_global.set(nuevo_valor)
        print(f"StringVar actualizada a: '{nuevo_valor}'")

# 1. Crear ventana raíz
raiz = tk.Tk()
raiz.title("Frames y StringVar")
raiz.geometry("450x200")

# 2. Crear una StringVar
# Hacemos la variable global para que sea accesible
texto_compartido_var = tk.StringVar()
texto_compartido_var.set("Texto inicial en StringVar") # Establecer valor inicial
globals()['texto_compartido_global'] = texto_compartido_var


# 3. Crear Frame superior y sus widgets
frame_arriba = tk.Frame(raiz, bd=2, relief="groove", padx=5, pady=5) # bd y relief para borde
frame_arriba.pack(pady=10, padx=10, fill="x") # fill="x" para que ocupe el ancho

# 3a. Label dentro de frame_arriba
label_instruccion_entry = tk.Label(frame_arriba, text="Entrada vinculada:")
label_instruccion_entry.pack(side="left", padx=5)

# 3b. Entry vinculado a texto_compartido_var
entry_vinculado = tk.Entry(frame_arriba, textvariable=texto_compartido_var, width=30, font=("Arial", 12))
entry_vinculado.pack(side="left", padx=5, expand=True, fill="x")


# 4. Crear Frame inferior y sus widgets
frame_abajo = tk.Frame(raiz, bd=2, relief="sunken", padx=5, pady=5)
frame_abajo.pack(pady=10, padx=10, fill="x")

# 4a. Label dentro de frame_abajo, vinculada a la misma StringVar
label_titulo_eco = tk.Label(frame_abajo, text="Eco de la entrada (Label vinculada):")
label_titulo_eco.pack(anchor="w") # anchor="w" para alinear a la izquierda (west)

label_eco_vinculada = tk.Label(frame_abajo, textvariable=texto_compartido_var, font=("Arial", 12, "italic"), fg="purple")
label_eco_vinculada.pack(pady=5, anchor="w")


# 6. Crear un Button para actualizar la StringVar
boton_actualizar = tk.Button(
    raiz, # Se añade directamente a la raíz, fuera de los frames
    text="Actualizar Variable Programáticamente",
    command=actualizar_texto_variable,
    bg="skyblue"
)
boton_actualizar.pack(pady=10)


# 7. Observar el comportamiento
print("Interfaz con Frames y StringVar lista.")
print(f"Valor inicial de StringVar: '{texto_compartido_var.get()}'")

raiz.mainloop()
print("Aplicación cerrada.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es el propósito principal de un widget `Frame`? ¿Cómo ayuda a
    organizar interfaces más complejas?
2.  ¿Qué es una `StringVar` (o `IntVar`, `BooleanVar`, `DoubleVar`) en Tkinter?
    ¿Cuál es la principal ventaja de usarla con la opción `textvariable` de
    widgets como `Entry` o `Label`?
3.  ¿Cómo se obtiene el valor de una `StringVar` en Python? ¿Y cómo se establece
    o cambia su valor? (Ver `get()` y `set()`).
4.  Si modificas el texto directamente en el `Entry` que está vinculado a la
    `StringVar`, ¿por qué se actualiza automáticamente la `Label` que también
    está vinculada a la misma `StringVar`?
5.  ¿Podrías tener múltiples `Frame`s anidados (un `Frame` dentro de otro `Frame`)?
    ¿Para qué podría ser útil?
-------------------------------------------------------------------------------
"""