"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                     Polimorfismo con Herencia (Figuras)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
El polimorfismo permite que objetos de diferentes clases respondan al mismo
método de formas específicas para cada clase. Usaremos una jerarquía de figuras
geométricas para demostrarlo.

1.  Define una clase base `FiguraGeometrica`:
    a.  Constructor `__init__(self, nombre_figura)` que inicialice `self.nombre_figura`.
    b.  Método `calcular_area(self)` que, por ahora, imprima
        "`El área de [nombre_figura] no está definida.`" o simplemente retorne 0.
    c.  Método `describir(self)` que imprima "Soy una figura geométrica."

2.  Define una clase `Rectangulo` que herede de `FiguraGeometrica`:
    a.  Constructor `__init__(self, base, altura)`: Llama al constructor de `FiguraGeometrica`
        pasando "Rectángulo" como nombre y luego inicializa `self.base` y `self.altura`.
    b.  Sobrescribe `calcular_area(self)` para que retorne el área del rectángulo.
    c.  Sobrescribe `describir(self)` para que imprima
        "Soy un Rectángulo de base [base] y altura [altura]."

3.  Define una clase `Circulo` que herede de `FiguraGeometrica`:
    a.  Constructor `__init__(self, radio)`: Llama al constructor de `FiguraGeometrica`
        pasando "Círculo" como nombre y luego inicializa `self.radio`.
        (Puedes usar `import math` para tener `math.pi`).
    b.  Sobrescribe `calcular_area(self)` para que retorne el área del círculo (π * radio^2).
    c.  Sobrescribe `describir(self)` para que imprima "Soy un Círculo de radio [radio]."

4.  Crea una función `mostrar_detalles_figura(figura)` que reciba un objeto `figura`
    (que se espera sea una instancia de `FiguraGeometrica` o sus subclases).
    Esta función debe llamar a `figura.describir()` y luego imprimir el resultado de
    `figura.calcular_area()`.

5.  Crea una lista que contenga al menos una instancia de `Rectangulo` y una de `Circulo`.
6.  Itera sobre la lista y, para cada figura en ella, llama a la función
    `mostrar_detalles_figura()`. Observa cómo se ejecuta el método correcto
    (de `Rectangulo` o `Circulo`) para `calcular_area` y `describir`.
-------------------------------------------------------------------------------
"""
import math # Para usar math.pi en la clase Circulo

# 1. Clase base FiguraGeometrica
class FiguraGeometrica:
    """Clase base para figuras geométricas."""
    def __init__(self, nombre_figura):
        self.nombre_figura = nombre_figura

    def calcular_area(self):
        """Método base para calcular el área. Las subclases deben implementarlo."""
        print(f"El área de {self.nombre_figura} no está definida en la clase base.")
        return 0

    def describir(self):
        """Método base para describir la figura."""
        print(f"Soy una figura geométrica llamada {self.nombre_figura}.")

# 2. Clase Rectangulo que hereda de FiguraGeometrica
class Rectangulo(FiguraGeometrica):
    """Representa un rectángulo."""
    def __init__(self, base, altura):
        super().__init__("Rectángulo") # Llama al constructor de la superclase
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura

    def describir(self):
        """Describe el rectángulo."""
        # super().describir() # Opcional: llamar al método de la superclase
        print(f"Soy un {self.nombre_figura} de base {self.base} y altura {self.altura}.")

# 3. Clase Circulo que hereda de FiguraGeometrica
class Circulo(FiguraGeometrica):
    """Representa un círculo."""
    def __init__(self, radio):
        super().__init__("Círculo") # Llama al constructor de la superclase
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo."""
        return math.pi * (self.radio ** 2)

    def describir(self):
        """Describe el círculo."""
        # super().describir() # Opcional
        print(f"Soy un {self.nombre_figura} de radio {self.radio}.")

# 4. Función para mostrar detalles de una figura
def mostrar_detalles_figura(figura):
    """Muestra la descripción y el área de una figura geométrica."""
    print("\n--- Detalles de la Figura ---")
    figura.describir() # Polimorfismo en acción
    area = figura.calcular_area() # Polimorfismo en acción
    print(f"Su área es: {area:.2f}")
    print("-----------------------------")

print("--- Demostración de Polimorfismo con Figuras ---")
# 5. Crear una lista de figuras
rect1 = Rectangulo(10, 5)
circ1 = Circulo(7)
rect2 = Rectangulo(3, 4)
fig_generica = FiguraGeometrica("Figura Desconocida")

lista_de_figuras = [rect1, circ1, rect2, fig_generica]

# 6. Iterar y mostrar detalles
for figura_actual in lista_de_figuras:
    mostrar_detalles_figura(figura_actual)

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Qué es el "polimorfismo" en POO? ¿Cómo se manifiesta en la función
    `mostrar_detalles_figura` cuando se le pasan objetos `Rectangulo` y `Circulo`?
2.  ¿Por qué la función `mostrar_detalles_figura` puede funcionar correctamente
    con diferentes tipos de figuras sin necesidad de saber explícitamente
    si el objeto es un `Rectangulo` o un `Circulo`?
3.  En la clase `FiguraGeometrica`, el método `calcular_area` imprime un mensaje
    o retorna 0. ¿Qué pasaría si una subclase olvidara sobrescribir este método
    y se llamara `calcular_area()` en un objeto de esa subclase?
4.  ¿Qué es un "contrato" o "interfaz" en el contexto de la POO y cómo se relaciona
    con el polimorfismo y la herencia (aunque Python no tenga interfaces explícitas
    como otros lenguajes)?
-------------------------------------------------------------------------------
"""