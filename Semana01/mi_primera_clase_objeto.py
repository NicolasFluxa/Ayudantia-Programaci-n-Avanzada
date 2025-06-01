"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                       Mi Primera Clase y Objeto
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio introduce los conceptos más básicos de clases y objetos.
Crearemos una clase simple para representar un tipo de objeto.

1.  Define una clase llamada `MascotaSimple`.
2.  Dentro de la clase, por ahora, no definiremos métodos complejos ni un
    constructor `__init__`. Solo usaremos la palabra clave `pass` para indicar
    que el cuerpo de la clase está vacío intencionalmente.
3.  Fuera de la definición de la clase, crea (instancia) dos objetos a partir
    de la clase `MascotaSimple`:
    * Un objeto llamado `mascota1`.
    * Un objeto llamado `mascota2`.
4.  Añade atributos de instancia a `mascota1` DESPUÉS de su creación:
    * `mascota1.nombre = "Fido"`
    * `mascota1.tipo = "Perro"`
5.  Añade atributos de instancia a `mascota2` DESPUÉS de su creación:
    * `mascota2.nombre = "Mishi"`
    * `mascota2.tipo = "Gato"`
6.  Imprime el nombre y el tipo de `mascota1`.
7.  Imprime el nombre y el tipo de `mascota2`.
8.  Imprime el tipo de la variable `mascota1` y el tipo de `mascota2` usando la
    función `type()`. ¿Qué observas?
-------------------------------------------------------------------------------
"""

# 1. Definir una clase simple
class MascotaSimple:
    """Una clase muy simple para representar una mascota."""
    pass # 'pass' es una instrucción nula, se usa cuando se requiere sintácticamente una instrucción pero no se quiere ejecutar ningún código.

print("--- Creando y Configurando Objetos de MascotaSimple ---")

# 3. Crear (instanciar) dos objetos de la clase MascotaSimple
mascota1 = MascotaSimple()
mascota2 = MascotaSimple()

# 4. Añadir atributos a mascota1 después de su creación
mascota1.nombre = "Fido"
mascota1.tipo = "Perro"

# 5. Añadir atributos a mascota2 después de su creación
mascota2.nombre = "Mishi"
mascota2.tipo = "Gato"
# mascota2.edad = 2 # Podríamos añadir más atributos dinámicamente

# 6. Imprimir los atributos de mascota1
print(f"\nInformación de Mascota 1:")
print(f"  Nombre: {mascota1.nombre}")
print(f"  Tipo  : {mascota1.tipo}")

# 7. Imprimir los atributos de mascota2
print(f"\nInformación de Mascota 2:")
print(f"  Nombre: {mascota2.nombre}")
print(f"  Tipo  : {mascota2.tipo}")
# print(f"  Edad  : {mascota2.edad}") # Si se añadió el atributo edad

# 8. Imprimir el tipo de los objetos
print("\n--- Tipos de los Objetos ---")
print(f"El tipo de la variable 'mascota1' es: {type(mascota1)}")
print(f"El tipo de la variable 'mascota2' es: {type(mascota2)}")

# Observación: Ambos objetos son instancias de la clase MascotaSimple.
# Su tipo es <class '__main__.MascotaSimple'> (o similar, dependiendo del entorno).

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Qué es una "clase" en Programación Orientada a Objetos? ¿Qué es un "objeto"?
    Usa una analogía (ej: molde de galletas y galletas).
2.  En este ejercicio, los atributos (`nombre`, `tipo`) se añadieron a los objetos
    *después* de crearlos. ¿Cuál podría ser una desventaja de este enfoque?
    (Pista: ¿qué pasa si olvidas añadir un atributo a un objeto?).
3.  ¿Qué hace la palabra clave `pass` dentro de la definición de una clase?
    ¿Cuándo podrías necesitar usarla?
4.  Si crearas un tercer objeto `mascota3 = MascotaSimple()`, ¿tendría
    automáticamente los atributos `nombre` o `tipo`? ¿Por qué?
-------------------------------------------------------------------------------
"""