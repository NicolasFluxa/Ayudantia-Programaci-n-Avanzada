"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
        Abstracción y Clases "Conceptualmente Abstractas" - Instrumentos
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
La abstracción se trata de ocultar la complejidad y mostrar solo las
características esenciales. A menudo, esto se logra con clases base que definen
una interfaz común que las subclases deben implementar. Python no tiene
clases abstractas "formales" como otros lenguajes sin usar el módulo `abc`,
pero podemos simular el concepto.

1.  Define una clase base "conceptualmente abstracta" llamada `InstrumentoMusical`.
    a.  En su `__init__(self, nombre, marca)` debe inicializar `self.nombre` y `self.marca`.
    b.  Debe tener un método `afinar(self)` que imprima
        "`Afinando el [nombre] [marca] de forma genérica.`"
    c.  Debe tener un método `tocar_nota(self, nota)` que, en la clase base,
        levante un error `NotImplementedError` con el mensaje:
        "Este método debe ser implementado por las subclases."
        Esto indica que las subclases CONCRETAS deben proporcionar su propia
        implementación de cómo tocar una nota.

2.  Crea una subclase `Guitarra` que herede de `InstrumentoMusical`.
    a.  Su `__init__(self, marca, numero_cuerdas=6)` debe llamar al `super().__init__`
        pasando "Guitarra" como nombre y la marca, y luego inicializar `self.numero_cuerdas`.
    b.  Sobrescribe el método `afinar(self)` para imprimir
        "`Afinando las [numero_cuerdas] cuerdas de la Guitarra [marca].`"
    c.  Implementa el método `tocar_nota(self, nota)` para que imprima
        "`Guitarra [marca] toca la nota [nota] con un rasgueo.`"

3.  Crea una subclase `Teclado` que herede de `InstrumentoMusical`.
    a.  Su `__init__(self, marca, numero_teclas=61)` debe llamar al `super().__init__`
        pasando "Teclado" como nombre y la marca, y luego inicializar `self.numero_teclas`.
    b.  Sobrescribe el método `afinar(self)` para imprimir
        "`El Teclado [marca] es electrónico, no requiere afinación manual.`"
    c.  Implementa el método `tocar_nota(self, nota)` para que imprima
        "`Teclado [marca] presiona la tecla para la nota [nota].`"

4.  Crea instancias de `Guitarra` y `Teclado`.
5.  Llama a los métodos `afinar()` y `tocar_nota("Do")` para cada instancia.
6.  Intenta crear una instancia de `InstrumentoMusical` directamente y llama a
    su método `tocar_nota("Sol")`. ¿Qué sucede? ¿Por qué?
-------------------------------------------------------------------------------
"""

# 1. Clase base "conceptualmente abstracta"
class InstrumentoMusical:
    """Clase base para instrumentos musicales."""
    def __init__(self, nombre, marca):
        self.nombre = nombre
        self.marca = marca
        print(f"Instrumento creado: {self.nombre} ({self.marca})")

    def afinar(self):
        """Método base para afinar el instrumento."""
        print(f"Afinando el {self.nombre} {self.marca} de forma genérica.")

    def tocar_nota(self, nota):
        """
        Método "abstracto" para tocar una nota.
        Las subclases deben implementar esto.
        """
        raise NotImplementedError("Este método (tocar_nota) debe ser implementado por las subclases.")

# 2. Subclase Guitarra
class Guitarra(InstrumentoMusical):
    """Representa una guitarra."""
    def __init__(self, marca, numero_cuerdas=6):
        super().__init__("Guitarra", marca)
        self.numero_cuerdas = numero_cuerdas
        print(f"  -> Tiene {self.numero_cuerdas} cuerdas.")

    def afinar(self):
        """Afina la guitarra."""
        print(f"Afinando las {self.numero_cuerdas} cuerdas de la Guitarra {self.marca}.")

    def tocar_nota(self, nota):
        """Toca una nota en la guitarra."""
        print(f"Guitarra {self.marca} toca la nota '{nota}' con un rasgueo.")

# 3. Subclase Teclado
class Teclado(InstrumentoMusical):
    """Representa un teclado electrónico."""
    def __init__(self, marca, numero_teclas=61):
        super().__init__("Teclado", marca)
        self.numero_teclas = numero_teclas
        print(f"  -> Tiene {self.numero_teclas} teclas.")

    def afinar(self):
        """Indica que el teclado no requiere afinación manual."""
        print(f"El Teclado {self.marca} es electrónico, no requiere afinación manual.")

    def tocar_nota(self, nota):
        """Toca una nota en el teclado."""
        print(f"Teclado {self.marca} presiona la tecla para la nota '{nota}'.")


print("\n--- Probando Instrumentos Musicales ---")
# 4. Crear instancias
mi_guitarra = Guitarra("Fender", 6)
mi_teclado = Teclado("Yamaha", 76)

# 5. Llamar a métodos
print("\nAcciones de la Guitarra:")
mi_guitarra.afinar()
mi_guitarra.tocar_nota("Sol")

print("\nAcciones del Teclado:")
mi_teclado.afinar()
mi_teclado.tocar_nota("Fa#")

# 6. Intentar usar la clase base directamente
print("\nIntentando usar InstrumentoMusical directamente:")
instrumento_generico = InstrumentoMusical("Genérico", "MarcaX")
instrumento_generico.afinar()
try:
    instrumento_generico.tocar_nota("La")
except NotImplementedError as e:
    print(f"Error al llamar tocar_nota() en instrumento_generico: {e}")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Qué es la "abstracción" en POO? ¿Cómo ayuda a manejar la complejidad?
2.  En `InstrumentoMusical`, ¿qué significa `raise NotImplementedError` en el
    método `tocar_nota`? ¿Cuál es su propósito?
3.  ¿Por qué se considera a `InstrumentoMusical` una clase "conceptualmente abstracta"
    en este ejemplo, aunque Python no lo fuerce explícitamente sin el módulo `abc`?
4.  Si una subclase como `Guitarra` no implementara el método `tocar_nota`, ¿qué
    sucedería al intentar llamar a `mi_guitarra.tocar_nota("Re")`?
5.  ¿Cómo el uso de una clase base como `InstrumentoMusical` (con métodos definidos
    o "abstractos") facilita el polimorfismo en funciones que trabajan con
    diferentes tipos de instrumentos?
-------------------------------------------------------------------------------
"""