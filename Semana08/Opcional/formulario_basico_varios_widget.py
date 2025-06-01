"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
             Formulario Básico con Varios Widgets Tkinter y `grid()`
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea un formulario de "registro" simple utilizando una variedad de widgets
de Tkinter y el gestor de geometría `grid()`.

El formulario debe incluir:
1.  `Label` y `Entry` para "Nombre:"
2.  `Label` y `Entry` para "Apellido:"
3.  `Label` y `Radiobutton`s para "Género:":
    (Opciones: "Masculino", "Femenino", "Otro"). Usar una `StringVar` para
    manejar la selección del radio button.
4.  `Label` y `Checkbutton` para "Intereses:":
    (Opciones como "Deportes", "Música", "Lectura"). Usar `IntVar` o `BooleanVar`
    para cada checkbutton.
5.  Una `Label` "Comentarios:" y un widget `Text` para entrada de texto multilínea.
6.  Un `Button` "Registrar".
7.  Una función que se ejecute al presionar "Registrar":
    a.  Debe recolectar todos los datos ingresados/seleccionados en el formulario.
    b.  Debe imprimir estos datos en la consola de forma legible.

Organiza todos los widgets usando `grid()`. Puedes usar `Frame`s si lo
consideras útil para agrupar secciones del formulario.
-------------------------------------------------------------------------------
"""
import tkinter as tk
from tkinter import messagebox

# Variables de control de Tkinter
var_nombre = None
var_apellido = None
var_genero = None
var_interes_deportes = None
var_interes_musica = None
var_interes_lectura = None
text_comentarios = None


def registrar_datos():
    """Recolecta y muestra los datos del formulario."""
    global var_nombre, var_apellido, var_genero, var_interes_deportes, \
        var_interes_musica, var_interes_lectura, text_comentarios

    nombre = var_nombre.get()
    apellido = var_apellido.get()
    genero = var_genero.get()  # Obtiene el valor del Radiobutton seleccionado

    intereses = []
    if var_interes_deportes.get() == 1:  # 1 si está marcado, 0 si no
        intereses.append("Deportes")
    if var_interes_musica.get() == 1:
        intereses.append("Música")
    if var_interes_lectura.get() == 1:
        intereses.append("Lectura")

    # Para el widget Text, se obtiene desde el índice "1.0" (línea 1, carácter 0)
    # hasta "end-1c" (final menos el último carácter newline que Text añade).
    comentarios = text_comentarios.get("1.0", "end-1c")

    # Validar que nombre y apellido no estén vacíos
    if not nombre.strip() or not apellido.strip():
        messagebox.showwarning("Campos Vacíos", "Nombre y Apellido son obligatorios.")
        return

    # Construir el mensaje de resumen
    resumen = f"--- Datos Registrados ---\n"
    resumen += f"Nombre: {nombre}\n"
    resumen += f"Apellido: {apellido}\n"
    resumen += f"Género: {genero if genero else 'No especificado'}\n"  # Manejar si no se selecciona género
    resumen += f"Intereses: {', '.join(intereses) if intereses else 'Ninguno seleccionado'}\n"
    resumen += f"Comentarios:\n{comentarios if comentarios.strip() else '(Sin comentarios)'}\n"
    resumen += "-------------------------"

    print(resumen)  # Imprimir en consola
    messagebox.showinfo("Registro Exitoso", "Datos registrados en la consola.\n\n" + resumen)


# --- Configuración de la Ventana Principal ---
raiz = tk.Tk()
raiz.title("Formulario de Registro Básico")
raiz.geometry("500x550")  # Ajustar tamaño
raiz.configure(padx=15, pady=15)

# --- Variables de Control Tkinter ---
# Para Entry
globals()['var_nombre'] = tk.StringVar()
globals()['var_apellido'] = tk.StringVar()

# Para Radiobuttons de Género
globals()['var_genero'] = tk.StringVar()
var_genero.set("No especificado")  # Valor inicial opcional

# Para Checkbuttons de Intereses (usamos IntVar, 1 para marcado, 0 para no marcado)
globals()['var_interes_deportes'] = tk.IntVar()
globals()['var_interes_musica'] = tk.IntVar()
globals()['var_interes_lectura'] = tk.IntVar()

# --- Creación y Posicionamiento de Widgets usando grid() ---

# Sección Datos Personales
frame_datos_personales = tk.LabelFrame(raiz, text="Datos Personales", padx=10, pady=10)
frame_datos_personales.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

tk.Label(frame_datos_personales, text="Nombre:").grid(row=0, column=0, sticky="w", pady=2)
entry_nombre = tk.Entry(frame_datos_personales, textvariable=var_nombre, width=40)
entry_nombre.grid(row=0, column=1, sticky="ew", pady=2)

tk.Label(frame_datos_personales, text="Apellido:").grid(row=1, column=0, sticky="w", pady=2)
entry_apellido = tk.Entry(frame_datos_personales, textvariable=var_apellido, width=40)
entry_apellido.grid(row=1, column=1, sticky="ew", pady=2)

# Sección Género
frame_genero = tk.LabelFrame(raiz, text="Género", padx=10, pady=10)
frame_genero.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

tk.Radiobutton(frame_genero, text="Masculino", variable=var_genero, value="Masculino").pack(anchor="w")
tk.Radiobutton(frame_genero, text="Femenino", variable=var_genero, value="Femenino").pack(anchor="w")
tk.Radiobutton(frame_genero, text="Otro", variable=var_genero, value="Otro").pack(anchor="w")
tk.Radiobutton(frame_genero, text="Prefiero no decir", variable=var_genero, value="No especificado").pack(anchor="w")

# Sección Intereses
frame_intereses = tk.LabelFrame(raiz, text="Intereses", padx=10, pady=10)
frame_intereses.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

tk.Checkbutton(frame_intereses, text="Deportes", variable=var_interes_deportes).pack(anchor="w")
tk.Checkbutton(frame_intereses, text="Música", variable=var_interes_musica).pack(anchor="w")
tk.Checkbutton(frame_intereses, text="Lectura", variable=var_interes_lectura).pack(anchor="w")

# Sección Comentarios
tk.Label(raiz, text="Comentarios:").grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=(10, 0))
# Hacemos global la referencia al widget Text
text_comentarios_ref = tk.Text(raiz, height=5, width=50,
                               wrap="word")  # wrap="word" para que el texto se ajuste por palabras
text_comentarios_ref.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
globals()['text_comentarios'] = text_comentarios_ref

# Scrollbar para el widget Text (opcional pero útil)
scrollbar_comentarios = tk.Scrollbar(raiz, command=text_comentarios_ref.yview)
scrollbar_comentarios.grid(row=4, column=2, sticky="ns")  # 'ns' para que se estire verticalmente
text_comentarios_ref.config(yscrollcommand=scrollbar_comentarios.set)

# Botón de Registro
boton_registrar = tk.Button(raiz, text="Registrar Datos", command=registrar_datos, bg="teal", fg="white",
                            font=("Arial", 12, "bold"))
boton_registrar.grid(row=5, column=0, columnspan=2, padx=5, pady=15, sticky="ew")

# Configurar expansión de columnas para mejor redimensionamiento
frame_datos_personales.columnconfigure(1, weight=1)  # Columna de Entries en frame_datos_personales
raiz.columnconfigure(0, weight=1)  # Permite que la columna principal se expanda
raiz.columnconfigure(1, weight=1)  # Si hubiera segunda columna principal

# --- Iniciar Bucle Principal ---
print("Formulario de registro básico listo.")
raiz.mainloop()
print("Aplicación de formulario cerrada.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Para qué sirve el widget `Radiobutton`? ¿Cómo se asegura que solo una opción
    de un grupo de radio buttons esté seleccionada a la vez (qué propiedad comparten)?
2.  ¿Para qué sirve el widget `Checkbutton`? ¿Cómo obtienes su estado (marcado/no marcado)?
3.  El widget `Text` permite entrada multilínea. ¿Cómo se obtiene todo el texto
    contenido en él? (Ver `text_comentarios.get("1.0", "end-1c")`). ¿Qué significan
    esos índices "1.0" y "end-1c"?
4.  ¿Qué es un `LabelFrame` y cómo se diferencia de un `Frame` normal?
5.  En este formulario, la función `registrar_datos()` usa variables globales para
    acceder a las variables de control de Tkinter y al widget Text. Si estuvieras
    estructurando esto con una clase para la GUI, ¿cómo pasarías estas referencias
    o accederías a estos widgets/variables desde un método de la clase?
-------------------------------------------------------------------------------
"""