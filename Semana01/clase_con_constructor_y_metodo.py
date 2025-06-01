"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                 Clase con Constructor (`__init__`) y Métodos
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Ahora mejoraremos nuestra representación de una mascota utilizando un
constructor para inicializar sus atributos y métodos para definir su comportamiento.

1.  Define una clase llamada `Mascota`.
2.  Dentro de la clase, define el método constructor `__init__(self, nombre, tipo, edad)`:
    a.  Este método debe aceptar `nombre`, `tipo` (ej: "Perro", "Gato") y `edad`
        como parámetros (además de `self`).
    b.  Dentro del constructor, asigna estos parámetros a atributos de instancia:
        `self.nombre`, `self.tipo`, `self.edad`.
3.  Define un método de instancia llamado `presentarse(self)`:
    a.  Este método debe imprimir una cadena que presente a la mascota, usando
        sus atributos. Por ejemplo: "¡Hola! Soy [nombre], un [tipo] de [edad] año(s)."
4.  Define otro método de instancia llamado `hacer_sonido(self, sonido)`:
    a.  Este método debe aceptar un parámetro `sonido` (string).
    b.  Debe imprimir una cadena como: "[nombre] hace: ¡[sonido]!"
5.  Crea dos objetos de la clase `Mascota`, proporcionando los valores para
    nombre, tipo y edad en el momento de la creación.
    * `perro1 = Mascota("Rocky", "Labrador", 3)`
    * `gato1 = Mascota("Pelusa", "Siamés", 5)`
6.  Llama al método `presentarse()` para cada uno de tus objetos mascota.
7.  Llama al método `hacer_sonido()` para cada mascota, pasándole un sonido
    apropiado (ej: "Guau", "Miau").
-------------------------------------------------------------------------------
"""

# 1. Definir la clase Mascota
class Mascota:
    """
    Representa una mascota con nombre, tipo y edad,
    y algunos comportamientos básicos.
    """

    # 2. Método constructor __init__
    def __init__(self, nombre, tipo, edad):
        """
        Constructor de la clase Mascota.
        Inicializa los atributos de la mascota.

        Args:
            nombre (str): El nombre de la mascota.
            tipo (str): El tipo o raza de la mascota (ej: "Perro", "Gato").
            edad (int): La edad de la mascota en años.
        """
        self.nombre = nombre # Atributo de instancia
        self.tipo = tipo     # Atributo de instancia
        self.edad = edad     # Atributo de instancia
        print(f"¡Se ha creado una nueva mascota: {self.nombre}!")

    # 3. Método de instancia presentarse
    def presentarse(self):
        """Hace que la mascota se presente."""
        print(f"¡Hola! Soy {self.nombre}, un {self.tipo} de {self.edad} año(s).")

    # 4. Método de instancia hacer_sonido
    def hacer_sonido(self, sonido):
        """Hace que la mascota emita un sonido específico."""
        print(f"{self.nombre} hace: ¡{sonido}!")

print("--- Creando Mascotas con Constructor y Usando Métodos ---")
# 5. Crear objetos (instancias) de la clase Mascota
perro1 = Mascota("Rocky", "Labrador", 3)
gato1 = Mascota("Pelusa", "Siamés", 5)
pajaro1 = Mascota("Piolín", "Canario", 1)

print("\n--- Presentaciones ---")
# 6. Llamar al método presentarse()
perro1.presentarse()
gato1.presentarse()
pajaro1.presentarse()

print("\n--- Haciendo Sonidos ---")
# 7. Llamar al método hacer_sonido()
perro1.hacer_sonido("Guau Guau")
gato1.hacer_sonido("Miau")
pajaro1.hacer_sonido("Pío Pío")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Qué es el método `__init__` en una clase de Python? ¿Cuándo se ejecuta
    automáticamente?
2.  ¿Qué representa el parámetro `self` en los métodos de una clase? ¿Es
    obligatorio usar la palabra "self" o podría ser otro nombre?
3.  ¿Cuál es la diferencia entre un atributo de instancia (como `self.nombre`)
    y una variable local definida dentro de un método?
4.  Si defines un método como `mi_metodo()` (sin `self` como primer parámetro)
    dentro de una clase e intentas llamarlo desde un objeto (`mi_objeto.mi_metodo()`),
    ¿qué error esperarías? ¿Por qué?
5.  Añade un nuevo método a la clase `Mascota` llamado `cumplir_anios(self)` que
    incremente la edad de la mascota en 1 y muestre un mensaje. Pruébalo.
-------------------------------------------------------------------------------
"""