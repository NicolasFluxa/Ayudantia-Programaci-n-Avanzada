"""
-------------------------------------------------------------------------------
                              EJERCICIO 02
             Uso Completo de `try-except-else-finally` con Archivos
-------------------------------------------------------------------------------
## ENUNCIADO:
## ----------
Este ejercicio demuestra el uso de todas las cláusulas de manejo de excepciones
(`try`, `except`, `else`, `finally`) al trabajar con archivos.

1.  Define una función `leer_y_mostrar_archivo(nombre_archivo)`:
    a.  Dentro de un bloque `try`:
        i.  Intenta abrir el archivo especificado en modo lectura (`'r'`).
            (Usa `with open(...) as archivo:` para asegurar que se cierre).
        ii. Lee todo el contenido del archivo.
        iii.Imprime el contenido leído.
    b.  Añade un bloque `except FileNotFoundError`:
        i.  Si el archivo no existe, imprime un mensaje como
            "Error: El archivo '[nombre_archivo]' no fue encontrado."
    c.  Añade un bloque `except IOError`:
        i.  Si ocurre otro error de entrada/salida (ej: permisos), imprime
            "Error: No se pudo leer el archivo '[nombre_archivo]'."
    d.  Añade un bloque `except Exception as e` general:
        i.  Para capturar cualquier otra excepción no prevista e imprimir
            un mensaje genérico junto con el error `e`.
    e.  Añade un bloque `else`:
        i.  Este bloque se ejecutará SOLO si no ocurrieron excepciones en el `try`.
        ii. Imprime un mensaje como "Lectura del archivo '[nombre_archivo]' completada exitosamente."
    f.  Añade un bloque `finally`:
        i.  Este bloque se ejecutará SIEMPRE, haya o no excepciones.
        ii. Imprime un mensaje como "Operación con el archivo '[nombre_archivo]' finalizada."

2.  En el código principal (fuera de la función):
    a.  Crea un archivo de prueba llamado "datos_prueba.txt" y escribe algunas
        líneas de texto en él.
    b.  Llama a `leer_y_mostrar_archivo("datos_prueba.txt")`.
    c.  Llama a `leer_y_mostrar_archivo("archivo_inexistente.txt")`.
    d.  (Opcional) Intenta simular otro error de I/O si puedes (ej: un archivo
        sin permisos de lectura, aunque esto es más dependiente del sistema operativo).
-------------------------------------------------------------------------------
"""

def leer_y_mostrar_archivo(nombre_archivo):
    """
    Intenta leer y mostrar el contenido de un archivo, manejando excepciones.
    """
    print(f"\n--- Intentando procesar el archivo: {nombre_archivo} ---")
    try:
        # a.i, a.ii (Usar 'with' asegura que el archivo se cierre automáticamente)
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo: # encoding es buena práctica
            print(f"Archivo '{nombre_archivo}' abierto correctamente.")
            contenido = archivo.read()
            # a.iii
            print("\nContenido del archivo:")
            print(contenido)

    # b. Manejar archivo no encontrado
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")

    # c. Manejar otros errores de I/O
    except IOError:
        print(f"Error de E/S: No se pudo leer el archivo '{nombre_archivo}' (quizás problemas de permisos o está corrupto).")

    # d. Manejar cualquier otra excepción
    except Exception as e:
        print(f"Ocurrió un error inesperado al procesar '{nombre_archivo}': {e}")

    # e. Bloque else: se ejecuta si no hubo excepciones en el try
    else:
        print(f"\nLectura del archivo '{nombre_archivo}' completada exitosamente.")

    # f. Bloque finally: se ejecuta siempre
    finally:
        print(f"Operación de intento de lectura con el archivo '{nombre_archivo}' finalizada.")
        print("-------------------------------------------------")


# --- Código Principal ---
if __name__ == "__main__":
    # 2a. Crear un archivo de prueba
    nombre_archivo_prueba = "datos_prueba.txt"
    try:
        with open(nombre_archivo_prueba, 'w', encoding='utf-8') as f:
            f.write("Línea 1: Hola desde el archivo de prueba.\n")
            f.write("Línea 2: Este es un ejemplo de manejo de archivos.\n")
            f.write("Línea 3: Python es versátil.\n")
        print(f"Archivo '{nombre_archivo_prueba}' creado para la demostración.")
    except IOError:
        print(f"No se pudo crear el archivo de prueba '{nombre_archivo_prueba}'. Las pruebas pueden fallar.")

    # 2b. Llamar con un archivo que existe
    leer_y_mostrar_archivo(nombre_archivo_prueba)

    # 2c. Llamar con un archivo que no existe
    leer_y_mostrar_archivo("archivo_inexistente.txt")

    # (Opcional) Simular otro error. Esto es más complejo de simular de forma controlada y portable.
    # Por ejemplo, si creas un directorio con el mismo nombre que un archivo que intentas abrir.
    # O cambiar permisos de un archivo (requiere privilegios y es dependiente del SO).
    # Dejaremos esta parte como un ejercicio teórico o de experimentación para el estudiante.

"""
-------------------------------------------------------------------------------
## PREGUNTAS DE COMPRENSIÓN:
## --------------------------
1.  ¿En qué situaciones se ejecuta el código dentro del bloque `else` en una
    estructura `try-except-else-finally`?
2.  ¿Cuál es la garantía principal que ofrece el bloque `finally`? ¿Por qué es útil,
    especialmente al trabajar con recursos externos como archivos o conexiones de red?
3.  La construcción `with open(...) as archivo:` se utiliza para trabajar con archivos.
    ¿Qué ventaja principal ofrece `with` en este contexto? (Pista: se relaciona con `finally`).
4.  Si dentro del bloque `try` ocurre una excepción que NO es `FileNotFoundError` ni
    `IOError` (y tienes el `except Exception as e:`), ¿se ejecutarían los bloques
    `else` y `finally`? Explica el flujo.
5.  ¿Podrías tener múltiples bloques `except` para diferentes tipos de errores
    después de un solo `try`? ¿Por qué es esto útil?
-------------------------------------------------------------------------------
"""