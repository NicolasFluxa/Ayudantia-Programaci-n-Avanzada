"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                       Mi Primera Ventana con Tkinter
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio te guiará para crear tu primera ventana básica usando Tkinter
y añadir un simple mensaje.

1.  Importa el módulo `tkinter` (comúnmente como `tk`).
2.  Crea la ventana principal de la aplicación (la ventana raíz).
    Generalmente se hace con `raiz = tk.Tk()`.
3.  Establece un título para la ventana (ej: "Mi Primera Ventana").
    Usa el método `title()` de la ventana raíz.
4.  Define las dimensiones iniciales de la ventana (ej: "300x200" para
    300 píxeles de ancho y 200 de alto). Usa el método `geometry()`.
5.  Crea un widget `Label` (etiqueta) para mostrar un texto.
    a.  El primer argumento del constructor `Label` es la ventana padre (tu raíz).
    b.  Usa el argumento `text` para especificar el mensaje (ej: "¡Hola, Tkinter!").
6.  "Empaqueta" el widget `Label` en la ventana para que sea visible.
    Usa el método `pack()` del widget Label. Este es el gestor de geometría más simple.
7.  Inicia el bucle principal de eventos de Tkinter (`mainloop()`). Esto mantiene
    la ventana visible y receptiva a eventos hasta que se cierre.
-------------------------------------------------------------------------------
"""

# 1. Importar el módulo tkinter
import tkinter as tk

# 2. Crear la ventana principal (raíz)
raiz = tk.Tk()

# 3. Establecer el título de la ventana
raiz.title("Mi Primera Ventana con Tkinter")

# 4. Definir las dimensiones iniciales de la ventana (ancho x alto)
raiz.geometry("400x250") # Ancho de 400px, Alto de 250px

# Configuración adicional opcional: hacer que la ventana no sea redimensionable
# raiz.resizable(False, False) # El primer False es para ancho, el segundo para alto

print("Ventana raíz creada. Añadiendo widgets...")

# 5. Crear un widget Label (etiqueta)
#   a. El primer argumento es el widget padre (la ventana raíz 'raiz')
#   b. 'text' es el texto que mostrará la etiqueta
etiqueta_saludo = tk.Label(raiz, text="¡Hola, Tkinter! Bienvenido/a.", font=("Arial", 16))

# 6. Empaquetar el widget Label en la ventana para hacerlo visible
# pack() es un gestor de geometría que organiza los widgets en bloques.
etiqueta_saludo.pack(pady=20) # pady añade un poco de espacio vertical alrededor de la etiqueta

# Crear otra etiqueta para demostrar el empaquetado
etiqueta_info = tk.Label(raiz, text="Este es un ejemplo básico de GUI con Python.", font=("Helvetica", 12))
etiqueta_info.pack(pady=10)

print("Widgets añadidos y empaquetados. Iniciando bucle principal...")
# 7. Iniciar el bucle principal de eventos de Tkinter
# Esto mantiene la ventana abierta y receptiva hasta que el usuario la cierre.
raiz.mainloop()

print("El bucle principal ha terminado (ventana cerrada).")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es el propósito de `import tkinter as tk`? ¿Podrías importar tkinter
    de otra forma? ¿Cuál es la convención?
2.  ¿Qué es la "ventana raíz" en una aplicación Tkinter? ¿Cuántas puedes tener
    normalmente en una aplicación simple?
3.  ¿Qué hace el método `pack()`? ¿Qué sucedería si olvidaras llamar a `.pack()`
    (u otro método de gestor de geometría como `.grid()` o `.place()`) en un widget?
4.  ¿Para qué sirve `raiz.mainloop()`? ¿Qué ocurre si omites esta línea?
5.  ¿Cómo podrías cambiar el color de fondo de la ventana raíz o el color del
    texto de la `Label`? (Investiga las opciones `bg` y `fg`).
-------------------------------------------------------------------------------
"""