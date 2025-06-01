"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                    Polimorfismo con Duck Typing (Protocolos)
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
En Python, el polimorfismo no siempre requiere herencia. Si un objeto "camina
como un pato y grazna como un pato, entonces es un pato" (Duck Typing).
Esto significa que si un objeto implementa los métodos necesarios (un protocolo),
puede ser tratado polimórficamente.

1.  Define tres clases diferentes que NO tengan una relación de herencia común:
    `Pato`, `Persona`, `RobotParlante`.
2.  Cada una de estas clases debe implementar un método llamado `comunicarse()`:
    a.  El `Pato` debe imprimir "¡Cuac cuac!".
    b.  La `Persona` (con un `nombre` en su `__init__`) debe imprimir
        "[nombre] dice: ¡Hola!".
    c.  El `RobotParlante` (con un `id_robot` en su `__init__`) debe imprimir
        "Robot [id_robot]: Saludos, humano."
3.  Define una función llamada `iniciar_conversacion(ser_comunicante)`:
    a.  Esta función debe recibir un objeto `ser_comunicante`.
    b.  Dentro de la función, simplemente llama al método `ser_comunicante.comunicarse()`.
4.  Crea instancias de `Pato`, `Persona` y `RobotParlante`.
5.  Llama a la función `iniciar_conversacion()` pasándole cada una de estas instancias.
    Observa que la función funciona con todos ellos porque todos "saben" comunicarse.
6.  (Opcional) Crea otra clase, `Perro`, con un método `ladrar()` pero SIN el
    método `comunicarse()`. Intenta pasar un objeto `Perro` a
    `iniciar_conversacion()`. ¿Qué sucede?
-------------------------------------------------------------------------------
"""

# 1. Definir clases sin herencia común
class Pato:
    def __init__(self, nombre="Lucas"):
        self.nombre = nombre

    def comunicarse(self): # Implementa el "protocolo" de comunicarse
        print(f"{self.nombre} (Pato) dice: ¡Cuac cuac!")

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def comunicarse(self): # Implementa el "protocolo" de comunicarse
        print(f"{self.nombre} (Persona) dice: ¡Hola!")

class RobotParlante:
    def __init__(self, id_robot):
        self.id_robot = id_robot

    def comunicarse(self): # Implementa el "protocolo" de comunicarse
        print(f"Robot {self.id_robot}: Saludos, humano.")

# 6. (Opcional) Clase Perro sin el método comunicarse()
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print(f"{self.nombre} (Perro) dice: ¡Guau!")

# 3. Definir la función que espera el protocolo "comunicarse"
def iniciar_conversacion(ser_comunicante):
    """
    Intenta hacer que un objeto se comunique.
    Espera que el objeto tenga un método 'comunicarse()'.
    """
    print("\n--- Intentando iniciar conversación ---")
    try:
        # Intenta llamar al método que forma parte del "protocolo" esperado
        ser_comunicante.comunicarse()
    except AttributeError:
        print(f"Error: El objeto de tipo '{type(ser_comunicante).__name__}' no sabe cómo 'comunicarse()'.")
    print("-------------------------------------")


print("--- Demostración de Duck Typing ---")
# 4. Crear instancias
pato_donald = Pato("Donald")
persona_ana = Persona("Ana")
robot_r2d2 = RobotParlante("R2-D2")
perro_bobby = Perro("Bobby") # Para la parte opcional

# 5. Llamar a iniciar_conversacion() con objetos que cumplen el protocolo
iniciar_conversacion(pato_donald)
iniciar_conversacion(persona_ana)
iniciar_conversacion(robot_r2d2)

# 6. (Opcional) Intentar con un objeto que NO cumple el protocolo
iniciar_conversacion(perro_bobby)

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Qué es "Duck Typing"? ¿Por qué se llama así?
2.  En este ejemplo, ¿las clases `Pato`, `Persona` y `RobotParlante` heredan
    de una superclase común que defina `comunicarse()`? ¿Es necesario para que
    `iniciar_conversacion()` funcione con ellas?
3.  ¿Qué es un "protocolo" en el contexto de Duck Typing en Python?
4.  ¿Qué tipo de error ocurre si intentas pasar un objeto a `iniciar_conversacion`
    que no tiene un método `comunicarse()`? ¿Cómo se manejó en el ejemplo?
5.  ¿Podrías definir otra clase, por ejemplo `Extraterrestre`, que también tenga un
    método `comunicarse()` y pasarla a `iniciar_conversacion`? ¿Funcionaría?
-------------------------------------------------------------------------------
"""