"""
-------------------------------------------------------------------------------
                              EJERCICIO 01
                          Factorial Recursivo
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
El factorial de un número entero no negativo `n`, denotado como `n!`, es el
producto de todos los enteros positivos menores o iguales a `n`.
Por ejemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120.
Por definición, 0! = 1 y 1! = 1.

Escribe una función recursiva llamada `factorial_recursivo(n)` que calcule
el factorial de un número `n`.

La función debe:
1.  Validar que `n` sea un entero no negativo. Si es negativo, debe lanzar
    un `ValueError`. Si no es entero, también (o manejarlo adecuadamente).
2.  Identificar el caso base: si `n` es 0 o 1, el factorial es 1.
3.  Identificar el caso recursivo: si `n > 1`, el factorial es `n` multiplicado
    por el factorial de `n-1`.
4.  Probar la función con varios números (ej: 0, 1, 5, 7) y también con un
    número negativo para ver la validación.
-------------------------------------------------------------------------------
"""

def factorial_recursivo(n):
    """
    Calcula el factorial de un número n de forma recursiva.

    Args:
        n (int): Un número entero no negativo.

    Returns:
        int: El factorial de n.

    Raises:
        ValueError: Si n es negativo o no es un entero.
    """
    # 1. Validar la entrada
    if not isinstance(n, int):
        raise ValueError("El factorial solo está definido para números enteros.")
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")

    # 2. Caso base
    if n == 0 or n == 1:
        return 1
    # 3. Caso recursivo
    else:
        # print(f"Calculando {n} * factorial_recursivo({n-1})") # Para depuración y ver las llamadas
        return n * factorial_recursivo(n - 1)

# 4. Pruebas de la función
print("--- Calculando Factoriales Recursivamente ---")
numeros_prueba = [0, 1, 5, 7, 3]

for num in numeros_prueba:
    try:
        resultado = factorial_recursivo(num)
        print(f"El factorial de {num} ({num}!) es: {resultado}")
    except ValueError as e:
        print(f"Error al calcular factorial de {num}: {e}")

# Prueba con un número negativo
print("\nIntentando calcular factorial de un número negativo (-3):")
try:
    factorial_recursivo(-3)
except ValueError as e:
    print(f"Error: {e}")

# Prueba con un no entero
print("\nIntentando calcular factorial de un no entero (3.5):")
try:
    factorial_recursivo(3.5)
except ValueError as e:
    print(f"Error: {e}")

print("-------------------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Qué es un "caso base" en una función recursiva? ¿Por qué es crucial tenerlo?
    ¿Cuál es el caso base en `factorial_recursivo`?
2.  ¿Qué es un "caso recursivo" (o paso recursivo)? ¿Cómo se define en esta función?
3.  Si llamaras a `factorial_recursivo(3)`, traza mentalmente (o en papel) las
    llamadas recursivas que se harían hasta llegar al caso base y cómo se
    construye el resultado final.
4.  ¿Qué sucedería si el caso base estuviera incorrecto o ausente (por ejemplo,
    si el caso base fuera `n == -1`)?
5.  La recursividad a veces puede ser menos eficiente que una solución iterativa
    (con bucles) debido a la sobrecarga de llamadas a funciones. ¿Podrías
    escribir una versión iterativa de la función factorial?
-------------------------------------------------------------------------------
"""