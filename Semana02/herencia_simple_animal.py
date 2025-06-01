"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                         Herencia Simple con Animales
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio introduce el concepto de herencia, donde una clase (subclase)
puede heredar atributos y métodos de otra clase (superclase).

1.  Define una clase base (superclase) llamada `Animal`:
    a.  En su constructor `__init__(self, nombre, edad)`, inicializa los
        atributos de instancia `self.nombre` y `self.edad`.
    b.  Define un método `comer(self)` que imprima: "[nombre] está comiendo."
    c.  Define un método `hacer_sonido(self)` que imprima: "[nombre] hace un sonido genérico."

2.  Define una clase `Perro` que HEREDE de `Animal`:
    a.  Su constructor `__init__(self, nombre, edad, raza)` debe inicializar
        `nombre`, `edad` (usando el constructor de la superclase `Animal` con `super()`)
        y un atributo específico de `Perro`, `self.raza`.
    b.  SOBREESCRIBE el método `hacer_sonido(self)` para que imprima:
        "[nombre] (un perro) hace: ¡Guau Guau!"
    c.  Define un método específico para `Perro` llamado `jugar(self)` que imprima:
        "[nombre] está jugando con la pelota."

3.  Define una clase `Gato` que HEREDE de `Animal`:
    a.  Su constructor `__init__(self, nombre, edad, color_pelaje)` debe inicializar
        `nombre`, `edad` (usando `super()`) y `self.color_pelaje`.
    b.  SOBREESCRIBE el método `hacer_sonido(self)` para que imprima:
        "[nombre] (un gato) hace: ¡Miau!"
    c.  Define un método específico para `Gato` llamado `acicalarse(self)` que imprima:
        "[nombre] se está acicalando."

4.  Crea un objeto de la clase `Perro` y otro de la clase `Gato`.
5.  Llama a los métodos `comer()`, `hacer_sonido()` y su método específico
    (`jugar()` o `acicalarse()`) para cada objeto.
-------------------------------------------------------------------------------
"""

# 1. Definir la clase base Animal
class Animal:
    """Clase base para representar un animal."""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Animal creado: {self.nombre}, {self.edad} años.")

    def comer(self):
        """Hace que el animal coma."""
        print(f"{self.nombre} está comiendo.")

    def hacer_sonido(self):
        """Hace que el animal emita un sonido genérico."""
        print(f"{self.nombre} hace un sonido genérico.")

# 2. Definir la subclase Perro que hereda de Animal
class Perro(Animal):
    """Representa un perro, que es un tipo de Animal."""
    def __init__(self, nombre, edad, raza):
        # a. Llamar al constructor de la superclase Animal
        super().__init__(nombre, edad)
        self.raza = raza # Atributo específico de Perro
        print(f"  -> Específicamente, un Perro de raza {self.raza}.")

    # b. Sobrescribir el método hacer_sonido
    def hacer_sonido(self):
        print(f"{self.nombre} (un perro) hace: ¡Guau Guau!")

    # c. Método específico de Perro
    def jugar(self):
        print(f"{self.nombre} está jugando con la pelota.")

# 3. Definir la subclase Gato que hereda de Animal
class Gato(Animal):
    """Representa un gato, que es un tipo de Animal."""
    def __init__(self, nombre, edad, color_pelaje):
        # a. Llamar al constructor de la superclase Animal
        super().__init__(nombre, edad)
        self.color_pelaje = color_pelaje # Atributo específico de Gato
        print(f"  -> Específicamente, un Gato con pelaje color {self.color_pelaje}.")

    # b. Sobrescribir el método hacer_sonido
    def hacer_sonido(self):
        print(f"{self.nombre} (un gato) hace: ¡Miau!")

    # c. Método específico de Gato
    def acicalarse(self):
        print(f"{self.nombre} se está acicalando.")

print("\n--- Creando y Usando Objetos Perro y Gato ---")
# 4. Crear objetos de Perro y Gato
mi_perro = Perro("Bobby", 5, "Golden Retriever")
mi_gato = Gato("Luna", 2, "Blanco")

# 5. Llamar a los métodos
print("\n--- Acciones de Bobby (Perro) ---")
mi_perro.comer()          # Método heredado de Animal
mi_perro.hacer_sonido()   # Método sobrescrito en Perro
mi_perro.jugar()          # Método específico de Perro

print("\n--- Acciones de Luna (Gato) ---")
mi_gato.comer()           # Método heredado de Animal
mi_gato.hacer_sonido()    # Método sobrescrito en Gato
mi_gato.acicalarse()      # Método específico de Gato

# También podemos crear un objeto Animal directamente
animal_generico = Animal("Criatura", 10)
animal_generico.hacer_sonido()


"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Qué es la "herencia" en POO y cuál es su principal beneficio?
2.  ¿Qué es una "superclase" (o clase base) y una "subclase" (o clase derivada)?
    Identifícalas en este ejercicio.
3.  ¿Para qué se utiliza la función `super()` dentro del constructor de una subclase?
    ¿Qué pasaría si no la llamaras y la superclase tuviera lógica importante en su `__init__`?
4.  ¿Qué significa "sobrescribir" (override) un método? Da un ejemplo de este ejercicio.
5.  Si la clase `Animal` tuviera un atributo `especie = "Desconocida"` definido
    directamente en el cuerpo de la clase (no en `__init__`), ¿podrían los objetos
    `Perro` y `Gato` acceder a ese atributo? (Esto se refiere a atributos de clase).
-------------------------------------------------------------------------------
"""