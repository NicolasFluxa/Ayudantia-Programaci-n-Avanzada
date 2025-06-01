"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
           Propiedades: Getters, Setters y Deleters con Decoradores
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Python ofrece una forma más "pythónica" de manejar el acceso y la modificación
de atributos utilizando decoradores `@property`, `@<nombre_attr>.setter`, y
`@<nombre_attr>.deleter`.

1.  Define una clase `Circulo`.
2.  En su constructor `__init__(self, radio)`:
    a.  Inicializa un atributo "privado" `self._radio`. (Usamos un solo guion
        bajo como convención para indicar que es de uso interno, aunque
        no hay privacidad estricta sin `__`).
    b.  Llama al setter de `radio` para asignar el valor inicial, de modo que
        la validación se aplique desde el inicio (ej: `self.radio = radio_inicial`).
3.  Usa el decorador `@property` para definir un método `radio(self)` que actúe
    como el "getter" para `_radio`. Simplemente debe retornar `self._radio`.
4.  Usa el decorador `@radio.setter` para definir un método `radio(self, valor)`
    que actúe como el "setter" para `_radio`.
    a.  Este método debe validar que `valor` sea positivo.
    b.  Si es positivo, asigna `valor` a `self._radio`.
    c.  Si no es positivo, lanza un `ValueError` con un mensaje apropiado.
5.  Usa el decorador `@radio.deleter` para definir un método `radio(self)` que
    "elimine" el radio (puedes poner `self._radio` a `None` o 0 y mostrar un mensaje).
6.  Define una propiedad calculada `area` usando `@property`. Este método debe
    calcular y retornar el área del círculo (π * radio^2) usando el valor de `self.radio`
    (que a su vez usará el getter de radio). No debe tener un setter.
7.  Crea instancias de `Circulo`. Demuestra:
    a.  Acceder al radio como si fuera un atributo: `mi_circulo.radio`.
    b.  Modificar el radio como si fuera un atributo: `mi_circulo.radio = nuevo_valor`.
        Prueba con valores válidos e inválidos para ver la validación del setter.
    c.  Acceder a la propiedad calculada `area`: `mi_circulo.area`.
    d.  Intentar asignar un valor a `area` (ej: `mi_circulo.area = 100`). ¿Qué sucede?
    e.  (Opcional) Demostrar el uso del `deleter`: `del mi_circulo.radio`.
-------------------------------------------------------------------------------
"""
import math

class Circulo:
    """Representa un círculo con radio y área calculada usando propiedades."""

    def __init__(self, radio_inicial):
        # self._radio = radio_inicial # Asignación directa (sin validación inicial)
        self.radio = radio_inicial # Llama al setter, aplicando validación desde el inicio

    @property
    def radio(self):
        """Getter para el atributo radio."""
        # print("Accediendo al radio (getter)...")
        return self._radio

    @radio.setter
    def radio(self, valor):
        """Setter para el atributo radio con validación."""
        # print(f"Intentando asignar radio = {valor} (setter)...")
        if valor <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self._radio = float(valor)
        print(f"Radio asignado a: {self._radio}")

    @radio.deleter
    def radio(self):
        """Deleter para el atributo radio."""
        print(f"Eliminando el radio del círculo (radio actual: {self._radio})...")
        del self._radio # O self._radio = None, o self._radio = 0
        print("El atributo _radio ha sido eliminado o reseteado.")

    @property
    def area(self):
        """Propiedad calculada para el área del círculo. Es de solo lectura."""
        # print("Calculando el área (getter de área)...")
        try:
            return math.pi * (self._radio ** 2)
        except AttributeError: # Si _radio fue eliminado por el deleter
            print("No se puede calcular el área porque el radio ha sido eliminado.")
            return None


print("--- Trabajando con la clase Circulo y Propiedades ---")
# 7a. Crear instancia y acceder al radio
try:
    c1 = Circulo(5)
    print(f"Radio inicial de c1: {c1.radio}") # Llama al getter de radio
except ValueError as e:
    print(f"Error al crear c1: {e}")

print("\n--- Modificando el radio (setter) ---")
# 7b. Modificar el radio
try:
    if 'c1' in locals(): # Verificar si c1 se creó exitosamente
        c1.radio = 7.5 # Llama al setter de radio
        print(f"Nuevo radio de c1: {c1.radio}")

        print("\nIntentando asignar un radio inválido (-3):")
        c1.radio = -3 # Esto debería lanzar un ValueError
except ValueError as e:
    print(f"Error al asignar radio: {e}")

print("\n--- Accediendo a la propiedad calculada area ---")
# 7c. Acceder al área
if 'c1' in locals() and hasattr(c1, '_radio'): # Verificar si c1 y su _radio existen
    print(f"Área de c1 (radio={c1.radio}): {c1.area:.2f}") # Llama al getter de area

    c1.radio = 1 # Cambiamos radio, el área se recalculará
    print(f"Área de c1 (radio={c1.radio}): {c1.area:.2f}")

print("\n--- Intentando asignar a la propiedad area (esto dará error) ---")
# 7d. Intentar asignar a 'area'
try:
    if 'c1' in locals():
        c1.area = 100 # AttributeError: can't set attribute 'area'
except AttributeError as e:
    print(f"Error al intentar asignar a c1.area: {e}")

print("\n--- Probando el deleter (opcional) ---")
# 7e. Usar el deleter
try:
    if 'c1' in locals() and hasattr(c1, '_radio'):
        del c1.radio # Llama al deleter de radio
        print(f"Intentando acceder al radio después de eliminarlo: {c1.radio if hasattr(c1, '_radio') else 'No existe'}")
        print(f"Intentando acceder al área después de eliminar el radio: {c1.area}")
except AttributeError as e: # Si _radio fue realmente eliminado con del self._radio
    print(f"Error esperado al acceder a radio/area después de 'del c1.radio': {e}")
except Exception as e:
    print(f"Otro error: {e}")


print("\n--- Creando círculo con radio inicial inválido ---")
try:
    c_error = Circulo(-10)
except ValueError as e:
    print(f"Error al crear c_error: {e}")

print("--------------------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es la ventaja de usar `@property` y `@<nombre_attr>.setter` en lugar
    de métodos getter y setter explícitos con nombres como `get_radio()` y `set_radio()`?
2.  ¿Cómo se define una propiedad de "solo lectura" (como `area` en este caso)?
    ¿Qué pasaría si intentaras definir un `@area.setter`?
3.  Explica el flujo de ejecución cuando se hace `mi_circulo.radio = 10`. ¿Qué
    métodos (propiedades) se invocan?
4.  ¿Para qué sirve el decorador `@<nombre_attr>.deleter`? ¿Es común su uso?
5.  ¿Por qué es una buena práctica llamar al setter (`self.radio = radio_inicial`)
    dentro del `__init__` en lugar de asignar directamente a `self._radio` si
    el setter ya incluye lógica de validación?
-------------------------------------------------------------------------------
"""