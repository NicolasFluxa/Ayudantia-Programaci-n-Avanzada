"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
                    Editor de Texto Simple con Tkinter
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Crea un editor de texto muy básico que permita abrir archivos de texto,
modificarlos y guardarlos. Este ejercicio integrará el widget `Text`, menús
y diálogos de archivo.

**Funcionalidades Requeridas:**

1.  **Ventana Principal:**
    * Un widget `Text` que ocupe la mayor parte de la ventana, donde el
        usuario pueda escribir y editar texto. Habilitar scrollbars para el
        widget Text.
2.  **Barra de Menú:**
    * **Menú "Archivo":**
        * **"Abrir..."**: Debe abrir un diálogo de selección de archivo
            (`filedialog.askopenfilename`). Si el usuario selecciona un archivo,
            su contenido debe cargarse en el widget `Text` (borrando el contenido anterior).
            Manejar posibles errores si el archivo no es de texto o no se puede leer.
        * **"Guardar Como..."**: Debe abrir un diálogo para guardar archivo
            (`filedialog.asksaveasfilename`). El contenido actual del widget `Text`
            debe guardarse en el archivo seleccionado por el usuario.
            Manejar posibles errores de escritura.
        * **"Guardar"**: (Opcional Avanzado) Si ya se abrió o guardó un archivo,
            guarda los cambios en ese mismo archivo. Si no, actúa como "Guardar Como...".
            Necesitarás una variable para recordar la ruta del archivo actual.
        * Un **separador**.
        * **"Salir"**: Cierra la aplicación (puede usar el diálogo de confirmación).

**Estructura:**
* Es altamente recomendable estructurar esta aplicación usando una clase
    (similar al ejercicio `AppCalculadoraSuma`).

**Pistas:**
* Widget `Text`:
    * Para obtener todo el contenido: `mi_texto.get("1.0", tk.END)` (o `tk.END + "-1c"` para quitar el newline final).
    * Para borrar todo el contenido: `mi_texto.delete("1.0", tk.END)`.
    * Para insertar texto: `mi_texto.insert(tk.END, "nuevo texto")`.
* `tkinter.filedialog`: `askopenfilename()`, `asksaveasfilename()`.
* Manejo de errores (`try-except`) para operaciones de archivo es crucial.
-------------------------------------------------------------------------------
"""
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext  # scrolledtext ya incluye scrollbars


class EditorTextoSimpleApp:
    def __init__(self, master):
        self.master = master
        master.title("Editor de Texto Simple")
        master.geometry("700x500")

        self.ruta_archivo_actual = None  # Para la funcionalidad "Guardar"

        self.crear_widgets_y_menu()

    def crear_widgets_y_menu(self):
        # --- Widget Text con Scrollbars (usando scrolledtext) ---
        self.text_area = scrolledtext.ScrolledText(
            self.master,
            wrap=tk.WORD,  # Ajuste de línea por palabra
            undo=True,  # Habilitar undo/redo básico
            font=("Consolas", 11)
        )
        self.text_area.pack(expand=True, fill="both", padx=5, pady=5)
        self.text_area.focus_set()  # Poner el foco en el área de texto

        # --- Barra de Menú ---
        barra_menu = tk.Menu(self.master)
        self.master.config(menu=barra_menu)

        # --- Menú Archivo ---
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        menu_archivo.add_command(label="Nuevo", command=self.nuevo_archivo)
        menu_archivo.add_command(label="Abrir...", command=self.abrir_archivo)
        menu_archivo.add_command(label="Guardar", command=self.guardar_archivo)
        menu_archivo.add_command(label="Guardar Como...", command=self.guardar_archivo_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.confirmar_salida)

        # --- (Opcional) Menú Editar ---
        menu_editar = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Editar", menu=menu_editar)
        menu_editar.add_command(label="Deshacer", command=self.text_area.edit_undo)
        menu_editar.add_command(label="Rehacer", command=self.text_area.edit_redo)
        # Se podrían añadir Cortar, Copiar, Pegar usando eventos y selección

    def nuevo_archivo(self):
        if messagebox.askokcancel("Nuevo Archivo",
                                  "¿Deseas crear un nuevo archivo? Se perderán los cambios no guardados."):
            self.text_area.delete("1.0", tk.END)
            self.ruta_archivo_actual = None
            self.master.title("Editor de Texto Simple - Sin Título")

    def abrir_archivo(self):
        ruta = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")]
        )
        if ruta:  # Si el usuario seleccionó un archivo
            try:
                with open(ruta, "r", encoding="utf-8") as archivo:
                    contenido = archivo.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, contenido)
                self.ruta_archivo_actual = ruta
                self.master.title(f"Editor de Texto Simple - {ruta}")
                messagebox.showinfo("Abrir Archivo", "Archivo cargado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error al Abrir", f"No se pudo leer el archivo:\n{e}")

    def guardar_archivo_como(self):
        ruta = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de Texto", "*.txt"), ("Todos los Archivos", "*.*")]
        )
        if ruta:  # Si el usuario especificó una ruta para guardar
            try:
                contenido = self.text_area.get("1.0", tk.END + "-1c")  # -1c para no incluir el último newline
                with open(ruta, "w", encoding="utf-8") as archivo:
                    archivo.write(contenido)
                self.ruta_archivo_actual = ruta
                self.master.title(f"Editor de Texto Simple - {ruta}")
                messagebox.showinfo("Guardar Archivo", "Archivo guardado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error al Guardar", f"No se pudo guardar el archivo:\n{e}")
        return ruta  # Retorna la ruta por si guardar_archivo() la necesita

    def guardar_archivo(self):
        if self.ruta_archivo_actual:  # Si ya tenemos una ruta (se abrió o guardó antes)
            try:
                contenido = self.text_area.get("1.0", tk.END + "-1c")
                with open(self.ruta_archivo_actual, "w", encoding="utf-8") as archivo:
                    archivo.write(contenido)
                messagebox.showinfo("Guardar Archivo", "Cambios guardados exitosamente.")
            except Exception as e:
                messagebox.showerror("Error al Guardar", f"No se pudo guardar el archivo:\n{e}")
        else:  # Si no hay ruta actual, actuar como "Guardar Como..."
            self.guardar_archivo_como()

    def confirmar_salida(self):
        # Podríamos verificar si hay cambios sin guardar antes de preguntar
        if messagebox.askyesno(title="Confirmar Salida", message="¿Estás seguro de que quieres salir?"):
            self.master.destroy()


# --- Bloque Principal ---
if __name__ == "__main__":
    print("Iniciando Editor de Texto Simple...")
    ventana_raiz = tk.Tk()
    app_editor = EditorTextoSimpleApp(ventana_raiz)
    ventana_raiz.mainloop()
    print("Editor de Texto cerrado.")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la ventaja de usar `scrolledtext.ScrolledText` en lugar de un
    `tk.Text` y añadir `Scrollbar`s manualmente?
2.  Explica cómo funcionan `filedialog.askopenfilename()` y
    `filedialog.asksaveasfilename()`. ¿Qué retornan?
3.  ¿Por qué es crucial usar bloques `try-except` al leer y escribir archivos?
    Menciona al menos dos tipos de excepciones que podrían ocurrir.
4.  En el método `guardar_archivo`, ¿cómo se diferencia la lógica si el archivo
    ya ha sido guardado previamente (`self.ruta_archivo_actual` existe) versus
    si es la primera vez que se guarda?
5.  ¿Cómo podrías implementar una funcionalidad simple de "Contar Palabras" que
    tome el contenido del `Text` widget, cuente las palabras y muestre el
    resultado (quizás en un `messagebox` o una etiqueta de estado)?
-------------------------------------------------------------------------------
"""