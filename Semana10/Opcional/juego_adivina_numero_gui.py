"""
-------------------------------------------------------------------------------
                        PROYECTO OPCIONAL 01
                 Juego "Adivina el Número" con Interfaz Gráfica
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Reimplementa el clásico juego de "Adivina el Número" (donde la computadora
"piensa" un número y el usuario intenta adivinarlo) pero esta vez con una
interfaz gráfica de usuario (GUI) utilizando Tkinter.

**Funcionalidades Requeridas:**

1.  **Generación del Número Secreto:**
    * Al iniciar la aplicación (o al presionar un botón "Nuevo Juego"), la
        computadora debe generar un número aleatorio secreto entre 1 y 100.
        (Usa el módulo `random`: `random.randint(1, 100)`).
2.  **Interfaz Gráfica:**
    * Una `Label` para dar instrucciones al usuario (ej: "Adivina un número entre 1 y 100").
    * Un `Entry` para que el usuario ingrese su intento.
    * Un `Button` "Adivinar" para enviar el intento.
    * Una `Label` para mostrar retroalimentación (ej: "Muy alto", "Muy bajo",
        "¡Correcto!", "Ingresa un número válido.").
    * (Opcional) Una `Label` para mostrar el número de intentos realizados.
3.  **Lógica del Juego:**
    * Cuando el usuario presiona "Adivinar":
        a.  Obtener el número del `Entry`. Validar que sea un número entero.
        b.  Incrementar el contador de intentos.
        c.  Comparar el intento con el número secreto.
        d.  Actualizar la `Label` de retroalimentación:
            * Si el intento es menor: "Muy bajo. Intenta de nuevo."
            * Si el intento es mayor: "Muy alto. Intenta de nuevo."
            * Si es correcto: "¡Felicidades! Adivinaste en [X] intentos."
                En este caso, el `Entry` y el botón "Adivinar" podrían deshabilitarse
                hasta que se inicie un "Nuevo Juego".
4.  **Botón "Nuevo Juego":**
    * Debe resetear el juego: generar un nuevo número secreto, limpiar el
        `Entry`, resetear la `Label` de retroalimentación y el contador de
        intentos, y rehabilitar los controles si estaban deshabilitados.
5.  **Estructura:**
    * Organiza la aplicación usando una clase.
-------------------------------------------------------------------------------
"""
import tkinter as tk
from tkinter import messagebox
import random


class JuegoAdivinaNumeroGUI:
    def __init__(self, master):
        self.master = master
        master.title("Adivina el Número")
        master.geometry("400x300")
        master.configure(padx=15, pady=15)

        self.numero_secreto = 0
        self.intentos_realizados = 0

        # Variables de control de Tkinter
        self.var_intento_usuario = tk.StringVar()
        self.var_retroalimentacion = tk.StringVar()
        self.var_contador_intentos = tk.StringVar()

        self.crear_widgets()
        self.iniciar_nuevo_juego()  # Inicia el primer juego automáticamente

    def crear_widgets(self):
        """Crea y posiciona los widgets de la interfaz."""
        tk.Label(self.master, text="He pensado un número entre 1 y 100.", font=("Arial", 12)).pack(pady=5)

        frame_entrada = tk.Frame(self.master)
        frame_entrada.pack(pady=10)

        tk.Label(frame_entrada, text="Tu intento:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.entry_intento = tk.Entry(frame_entrada, textvariable=self.var_intento_usuario, width=10,
                                      font=("Arial", 10))
        self.entry_intento.pack(side=tk.LEFT, padx=5)
        self.entry_intento.focus()
        # Bind Enter key to a adivinar_numero method
        self.entry_intento.bind("<Return>", lambda event: self.procesar_intento())

        self.boton_adivinar = tk.Button(self.master, text="Adivinar", command=self.procesar_intento,
                                        font=("Arial", 10, "bold"), bg="lightblue")
        self.boton_adivinar.pack(pady=5)

        self.label_retroalimentacion = tk.Label(self.master, textvariable=self.var_retroalimentacion,
                                                font=("Arial", 11, "italic"), fg="navy")
        self.label_retroalimentacion.pack(pady=10)

        self.label_contador_intentos = tk.Label(self.master, textvariable=self.var_contador_intentos,
                                                font=("Arial", 10))
        self.label_contador_intentos.pack(pady=5)

        self.boton_nuevo_juego = tk.Button(self.master, text="Nuevo Juego", command=self.iniciar_nuevo_juego,
                                           font=("Arial", 10), bg="lightgreen")
        self.boton_nuevo_juego.pack(pady=10)

    def iniciar_nuevo_juego(self):
        """Resetea el estado del juego para una nueva partida."""
        self.numero_secreto = random.randint(1, 100)
        self.intentos_realizados = 0

        self.var_intento_usuario.set("")  # Limpiar Entry
        self.var_retroalimentacion.set("Ingresa tu primer intento.")
        self.var_contador_intentos.set("Intentos: 0")

        self.entry_intento.config(state=tk.NORMAL)  # Habilitar Entry
        self.boton_adivinar.config(state=tk.NORMAL)  # Habilitar Botón
        self.entry_intento.focus()
        print(f"Nuevo juego iniciado. Número secreto (para depuración): {self.numero_secreto}")

    def procesar_intento(self):
        """Procesa el intento del usuario."""
        try:
            intento = int(self.var_intento_usuario.get())
            if not (1 <= intento <= 100):
                self.var_retroalimentacion.set("Por favor, ingresa un número entre 1 y 100.")
                messagebox.showwarning("Entrada Inválida", "El número debe estar entre 1 y 100.")
                self.var_intento_usuario.set("")
                return

            self.intentos_realizados += 1
            self.var_contador_intentos.set(f"Intentos: {self.intentos_realizados}")

            if intento < self.numero_secreto:
                self.var_retroalimentacion.set(f"'{intento}' es MUY BAJO. ¡Intenta de nuevo!")
            elif intento > self.numero_secreto:
                self.var_retroalimentacion.set(f"'{intento}' es MUY ALTO. ¡Intenta de nuevo!")
            else:  # ¡Correcto!
                mensaje_exito = f"¡CORRECTO! 🎉 Adivinaste el número {self.numero_secreto} en {self.intentos_realizados} intentos."
                self.var_retroalimentacion.set(mensaje_exito)
                messagebox.showinfo("¡Felicidades!", mensaje_exito)
                self.entry_intento.config(state=tk.DISABLED)  # Deshabilitar Entry
                self.boton_adivinar.config(state=tk.DISABLED)  # Deshabilitar Botón

        except ValueError:
            self.var_retroalimentacion.set("Entrada inválida. Ingresa solo NÚMEROS enteros.")
            messagebox.showerror("Error de Entrada", "Debes ingresar un número entero.")

        self.var_intento_usuario.set("")  # Limpiar Entry para el siguiente intento
        self.entry_intento.focus()


# --- Bloque Principal ---
if __name__ == "__main__":
    print("Iniciando Juego 'Adivina el Número' con GUI...")
    ventana_raiz = tk.Tk()
    juego_app = JuegoAdivinaNumeroGUI(ventana_raiz)
    ventana_raiz.mainloop()
    print("Juego cerrado.")

"""
-------------------------------------------------------------------------------
## PUNTOS CLAVE Y PREGUNTAS GUÍA:
## --------------------------------
1.  **Estado del Juego:** ¿Qué variables de instancia (`self.numero_secreto`,
    `self.intentos_realizados`) son cruciales para mantener el estado del juego?
2.  **Variables de Control Tkinter:** ¿Cómo se usan `StringVar` para actualizar
    dinámicamente el texto de las `Label`s y obtener el texto del `Entry`?
3.  **Flujo del Juego:** Describe el flujo lógico que ocurre cuando el usuario
    ingresa un número y presiona "Adivinar".
4.  **Reinicio del Juego:** ¿Qué acciones realiza la función `iniciar_nuevo_juego()`
    para preparar una nueva partida?
5.  **Deshabilitar Widgets:** ¿Por qué y cómo se deshabilitan el `Entry` y el botón
    "Adivinar" una vez que el usuario adivina correctamente? ¿Cómo se vuelven a
    habilitar? (Ver la opción `state` de los widgets).
6.  **Manejo de Errores:** ¿Qué tipo de error se maneja con `try-except` en
    `procesar_intento()`? ¿Qué otros errores podrían considerarse?
7.  **Mejora (Binding de Evento):** La línea `self.entry_intento.bind("<Return>", lambda event: self.procesar_intento())`
    permite que el usuario presione Enter en el Entry para adivinar. Explica brevemente
    cómo funciona `bind` y qué es `lambda event: ...` en este contexto.
-------------------------------------------------------------------------------
"""