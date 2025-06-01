"""
-------------------------------------------------------------------------------
                        EJERCICIO OPCIONAL 01
                    Clase Rectángulo con Cálculos
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Define una clase `Rectangulo` para representar rectángulos.

1.  La clase debe tener un constructor `__init__(self, base, altura)` que
    inicialice los atributos de instancia `self.base` y `self.altura`.
    Asegúrate de que base y altura sean números positivos; si no, puedes
    asignarles un valor por defecto (ej: 1) o imprimir un aviso.
2.  Implementa un método llamado `calcular_area(self)` que retorne el área
    del rectángulo (base * altura).
3.  Implementa un método llamado `calcular_perimetro(self)` que retorne el
    perímetro del rectángulo (2 * (base + altura)).
4.  Implementa un método llamado `es_cuadrado(self)` que retorne `True` si
    el rectángulo es un cuadrado (base == altura) y `False` en caso contrario.
5.  Implementa un método `mostrar_info(self)` que imprima la base, la altura,
    el área, el perímetro y si es un cuadrado o no.

Crea al menos dos objetos `Rectangulo` con diferentes dimensiones (uno que
sea un cuadrado y otro que no). Para cada objeto, llama al método `mostrar_info()`.
-------------------------------------------------------------------------------
"""

class Rectangulo:
    """Representa un rectángulo y permite calcular su área, perímetro
       e identificar si es un cuadrado."""

    def __init__(self, base, altura):
        """
        Constructor de la clase Rectangulo.

        Args:
            base (float or int): La longitud de la base del rectángulo.
            altura (float or int): La altura del rectángulo.
        """
        if base > 0:
            self.base = base
        else:
            print(f"Advertencia: La base ({base}) no es positiva. Se usará 1 por defecto.")
            self.base = 1

        if altura > 0:
            self.altura = altura
        else:
            print(f"Advertencia: La altura ({altura}) no es positiva. Se usará 1 por defecto.")
            self.altura = 1
        print(f"Rectángulo creado con base {self.base} y altura {self.altura}.")

    def calcular_area(self):
        """Calcula y retorna el área del rectángulo."""
        return self.base * self.altura

    def calcular_perimetro(self):
        """Calcula y retorna el perímetro del rectángulo."""
        return 2 * (self.base + self.altura)

    def es_cuadrado(self):
        """Verifica si el rectángulo es un cuadrado."""
        return self.base == self.altura

    def mostrar_info(self):
        """Muestra toda la información relevante del rectángulo."""
        print("\n--- Información del Rectángulo ---")
        print(f"  Base      : {self.base}")
        print(f"  Altura    : {self.altura}")
        print(f"  Área      : {self.calcular_area()}")
        print(f"  Perímetro : {self.calcular_perimetro()}")
        if self.es_cuadrado():
            print("  Tipo      : Es un CUADRADO.")
        else:
            print("  Tipo      : Es un RECTÁNGULO (no cuadrado).")
        print("----------------------------------")


print("--- Creando y Probando Objetos Rectangulo ---")
# Crear un rectángulo que no es un cuadrado
rect1 = Rectangulo(10, 5)
rect1.mostrar_info()

# Crear un rectángulo que sí es un cuadrado
rect2 = Rectangulo(7, 7)
rect2.mostrar_info()

# Crear un rectángulo con valores inválidos para probar la validación del constructor
rect_invalido = Rectangulo(-5, 0)
rect_invalido.mostrar_info()

# Probar un método individual
area_rect1 = rect1.calcular_area()
print(f"\nEl área de rect1 calculada por separado es: {area_rect1}")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  En el constructor `__init__`, ¿por qué se verifica si `base` y `altura` son
    positivas? ¿Qué otras formas de manejar entradas inválidas podrías implementar?
2.  Los métodos `calcular_area` y `calcular_perimetro` retornan un valor, mientras
    que `mostrar_info` solo imprime. ¿Cuándo es preferible que una función/método
    retorne un valor en lugar de imprimirlo directamente?
3.  ¿Podrías añadir un método `redimensionar(self, nueva_base, nueva_altura)` que
    permita cambiar las dimensiones de un rectángulo existente?
4.  Si tuvieras una lista de objetos `Rectangulo`, ¿cómo podrías iterar sobre
    ella y llamar al método `mostrar_info()` para cada rectángulo en la lista?
-------------------------------------------------------------------------------
"""