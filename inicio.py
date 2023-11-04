import os
from pathlib import Path

# Ruta base donde se encuentran las recetas
mi_ruta = Path("C:/Users/jimym/Documents/Udemy/Recetas")

# Función para contar la cantidad de recetas en la ruta
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

# Función para mostrar el menú principal
def menu_principal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('*' * 50)
        print('*' * 5 + " Bienvenido al administrador de recetas " + '*' * 5)
        print('*' * 50)
        print('\n')
        print(f"Las recetas se encuentran en {mi_ruta}")
        print(f"Total recetas: {contar_recetas(mi_ruta)}")

        print("Elige una opción:")
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoría nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa
        [7] - Volver al inicio''')

        eleccion_menu = input(">> ")

        if eleccion_menu == "1":
            leer_receta()
            volver_inicio()
        elif eleccion_menu == "2":
            crear_receta()
            volver_inicio()
        elif eleccion_menu == "3":
            crear_categoria()
            volver_inicio()
        elif eleccion_menu == "4":
            eliminar_receta()
            volver_inicio()
        elif eleccion_menu == "5":
            eliminar_categoria()
            volver_inicio()
        elif eleccion_menu == "6":
            break
        elif eleccion_menu == "7":
            continue

# Función para mostrar la lista de categorías
def mostrar_categorias():
    print("Categorías:")
    for carpeta in mi_ruta.iterdir():
        if carpeta.is_dir():
            print(carpeta.name)

# Función para elegir una categoría
def elegir_categoria():
    while True:
        mostrar_categorias()
        categoria = input("Elije una categoría: ")
        ruta_categoria = mi_ruta / categoria

        if ruta_categoria.is_dir():
            return ruta_categoria
        else:
            print("Categoría no válida. Inténtalo de nuevo.")

# Función para mostrar la lista de recetas en una categoría
def mostrar_recetas(ruta_categoria):
    print("Recetas en la categoría:")
    for receta in ruta_categoria.glob('*.txt'):
        print(receta.stem)

# Función para elegir una receta
def elegir_receta(ruta_categoria):
    while True:
        mostrar_recetas(ruta_categoria)
        receta = input("Elije una receta: ")
        ruta_receta = ruta_categoria / (receta + ".txt")

        if ruta_receta.is_file():
            return ruta_receta
        else:
            print("Receta no válida. Inténtalo de nuevo.")

# Función para leer el contenido de una receta
def leer_receta():
    ruta_categoria = elegir_categoria()
    ruta_receta = elegir_receta(ruta_categoria)

    with open(ruta_receta, 'r', encoding='utf-8') as file:
        contenido = file.read()
        print(contenido)

# Función para crear una nueva receta
def crear_receta():
    ruta_categoria = elegir_categoria()
    nombre_receta = input("Escribe el nombre de tu receta: ") + ".txt"
    ruta_receta = ruta_categoria / nombre_receta

    if ruta_receta.is_file():
        print("La receta ya existe.")
    else:
        contenido_receta = input("Escribe tu nueva receta (presiona Ctrl+Z o Ctrl+D para finalizar):\n")
        with open(ruta_receta, 'w', encoding='utf-8') as file:
            file.write(contenido_receta)
        print(f"Tu receta {nombre_receta} ha sido creada.")

# Función para crear una nueva categoría
def crear_categoria():
    nombre_categoria = input("Escribe el nombre de la nueva categoría: ")
    ruta_categoria = mi_ruta / nombre_categoria

    if ruta_categoria.is_dir():
        print("La categoría ya existe.")
    else:
        ruta_categoria.mkdir()
        print(f"Tu nueva categoría {nombre_categoria} ha sido creada.")

# Función para eliminar una receta
def eliminar_receta():
    ruta_categoria = elegir_categoria()
    ruta_receta = elegir_receta(ruta_categoria)
    ruta_receta.unlink()
    print(f"La receta {ruta_receta.name} ha sido eliminada.")

# Función para eliminar una categoría
def eliminar_categoria():
    ruta_categoria = elegir_categoria()
    ruta_categoria.rmdir()
    print(f"La categoría {ruta_categoria.name} ha sido eliminada.")

# Función para volver al menú principal
def volver_inicio():
    input("Presiona Enter para volver al inicio...")

if __name__ == "__main__":
    menu_principal()
import os
from pathlib import Path

# Ruta base donde se encuentran las recetas
mi_ruta = Path("C:/Users/jimym/Documents/Udemy/Recetas")

# Función para contar la cantidad de recetas en la ruta
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

# Función para mostrar el menú principal
def menu_principal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('*' * 50)
        print('*' * 5 + " Bienvenido al administrador de recetas " + '*' * 5)
        print('*' * 50)
        print('\n')
        print(f"Las recetas se encuentran en {mi_ruta}")
        print(f"Total recetas: {contar_recetas(mi_ruta)}")

        print("Elige una opción:")
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoría nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa
        [7] - Volver al inicio''')

        eleccion_menu = input(">> ")

        if eleccion_menu == "1":
            leer_receta()
            volver_inicio()
        elif eleccion_menu == "2":
            crear_receta()
            volver_inicio()
        elif eleccion_menu == "3":
            crear_categoria()
            volver_inicio()
        elif eleccion_menu == "4":
            eliminar_receta()
            volver_inicio()
        elif eleccion_menu == "5":
            eliminar_categoria()
            volver_inicio()
        elif eleccion_menu == "6":
            break
        elif eleccion_menu == "7":
            continue

# Función para mostrar la lista de categorías
def mostrar_categorias():
    print("Categorías:")
    for carpeta in mi_ruta.iterdir():
        if carpeta.is_dir():
            print(carpeta.name)

# Función para elegir una categoría
def elegir_categoria():
    while True:
        mostrar_categorias()
        categoria = input("Elije una categoría: ")
        ruta_categoria = mi_ruta / categoria

        if ruta_categoria.is_dir():
            return ruta_categoria
        else:
            print("Categoría no válida. Inténtalo de nuevo.")

# Función para mostrar la lista de recetas en una categoría
def mostrar_recetas(ruta_categoria):
    print("Recetas en la categoría:")
    for receta in ruta_categoria.glob('*.txt'):
        print(receta.stem)

# Función para elegir una receta
def elegir_receta(ruta_categoria):
    while True:
        mostrar_recetas(ruta_categoria)
        receta = input("Elije una receta: ")
        ruta_receta = ruta_categoria / (receta + ".txt")

        if ruta_receta.is_file():
            return ruta_receta
        else:
            print("Receta no válida. Inténtalo de nuevo.")

# Función para leer el contenido de una receta
def leer_receta():
    ruta_categoria = elegir_categoria()
    ruta_receta = elegir_receta(ruta_categoria)

    with open(ruta_receta, 'r', encoding='utf-8') as file:
        contenido = file.read()
        print(contenido)

# Función para crear una nueva receta
def crear_receta():
    ruta_categoria = elegir_categoria()
    nombre_receta = input("Escribe el nombre de tu receta: ") + ".txt"
    ruta_receta = ruta_categoria / nombre_receta

    if ruta_receta.is_file():
        print("La receta ya existe.")
    else:
        contenido_receta = input("Escribe tu nueva receta (presiona Ctrl+Z o Ctrl+D para finalizar):\n")
        with open(ruta_receta, 'w', encoding='utf-8') as file:
            file.write(contenido_receta)
        print(f"Tu receta {nombre_receta} ha sido creada.")

# Función para crear una nueva categoría
def crear_categoria():
    nombre_categoria = input("Escribe el nombre de la nueva categoría: ")
    ruta_categoria = mi_ruta / nombre_categoria

    if ruta_categoria.is_dir():
        print("La categoría ya existe.")
    else:
        ruta_categoria.mkdir()
        print(f"Tu nueva categoría {nombre_categoria} ha sido creada.")

# Función para eliminar una receta
def eliminar_receta():
    ruta_categoria = elegir_categoria()
    ruta_receta = elegir_receta(ruta_categoria)
    ruta_receta.unlink()
    print(f"La receta {ruta_receta.name} ha sido eliminada.")

# Función para eliminar una categoría
def eliminar_categoria():
    ruta_categoria = elegir_categoria()
    ruta_categoria.rmdir()
    print(f"La categoría {ruta_categoria.name} ha sido eliminada.")

# Función para volver al menú principal
def volver_inicio():
    input("Presiona Enter para volver al inicio...")

if __name__ == "__main__":
    menu_principal()
