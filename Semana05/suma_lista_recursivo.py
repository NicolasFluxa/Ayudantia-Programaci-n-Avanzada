"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
                       Suma de Elementos de una Lista Recursiva
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Escribe una función recursiva llamada `suma_lista_recursiva(lista)` que
calcule la suma de todos los números en una lista.

La función debe:
1.  Manejar el caso de que la lista contenga elementos no numéricos (opcional,
    podrías asumir que solo contiene números o intentar manejarlo).
2.  Identificar el caso base: Si la lista está vacía, la suma es 0.
3.  Identificar el caso recursivo: Si la lista no está vacía, la suma es
    el primer elemento de la lista más la suma recursiva del resto de la lista
    (todos los elementos excepto el primero).
4.  Probar la función con diferentes listas, incluyendo una lista vacía y
    una lista con un solo elemento.
-------------------------------------------------------------------------------
"""


def suma_lista_recursiva(lista):
    """
    Calcula la suma de los elementos de una lista de números de forma recursiva.

    Args:
        lista (list): Una lista de números.

    Returns:
        int or float: La suma de los elementos de la lista.
                      Retorna 0 si la lista está vacía.
    Raises:
        TypeError: Si la lista contiene elementos no numéricos.
    """
    # 2. Caso base
    if not lista:  # Si la lista está vacía
        return 0
    else:
        # 3. Caso recursivo
        primer_elemento = lista[0]

        # Validación opcional de tipo
        if not isinstance(primer_elemento, (int, float)):
            raise TypeError("La lista solo debe contener números para la suma.")

        # print(f"Sumando {primer_elemento} + suma_lista_recursiva({lista[1:]})") # Para depuración
        return primer_elemento + suma_lista_recursiva(lista[1:])  # lista[1:] es una nueva lista sin el primer elemento


# 4. Pruebas de la función
print("--- Sumando Listas Recursivamente ---")
listas_prueba = [
    [1, 2, 3, 4, 5],  # Suma = 15
    [10, 20, 30],  # Suma = 60
    [7],  # Suma = 7
    [],  # Suma = 0
    [-1, -2, 3, 0, 5]  # Suma = 5
]

for lst in listas_prueba:
    try:
        resultado = suma_lista_recursiva(lst)
        print(f"La suma de la lista {lst} es: {resultado}")
    except TypeError as e:
        print(f"Error al sumar la lista {lst}: {e}")

# Prueba con lista con elementos no numéricos
lista_con_error = [1, 2, "a", 4]
print(f"\nIntentando sumar la lista {lista_con_error}:")
try:
    suma_lista_recursiva(lista_con_error)
except TypeError as e:
    print(f"Error: {e}")

print("-----------------------------------")

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿Cuál es el caso base en la función `suma_lista_recursiva`?
2.  ¿Cómo se "reduce" el problema en cada llamada recursiva? (Observa `lista[1:]`).
    ¿Qué es el "slicing" de listas en Python?
3.  Si llamas a `suma_lista_recursiva([10, 20, 30])`, describe las llamadas
    recursivas y cómo se retorna el valor final.
4.  ¿Qué pasaría si el caso recursivo no modificara la lista (ej: si siempre
    pasara la `lista` original en la llamada recursiva)?
5.  La recursividad en listas a menudo implica crear sub-listas (slices), lo cual
    puede tener un costo en memoria y rendimiento para listas muy grandes.
    ¿Cómo podrías abordar la suma de una lista de forma iterativa (con un bucle)?
-------------------------------------------------------------------------------
"""