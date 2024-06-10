from os import system
from data_stark import lista_personajes
from funciones00 import *

def pausar():
    system("pause")

def limpiar_terminal():
    system("cls")

def menu_superheroes() -> str:
   
    limpiar_terminal()
    print("        Menu de opciones")
    print("A- Mostrar el nombre de todos los superheroes.")
    print("B- Mostrar el nombre y altura de todos los superheroes.")
    print("C- Mostrar la altura mayor")
    print("D- Mostrar la altura menor")
    print("E- Mostrar la altura promedio de todos los heroes")
    print("F- Mostrar Nombre del heroe con la mayor altura.")
    print("G- Mostrar Nombre del heroe con la menor altura.")
    print("H- Mostrar Heroe mas pesado.")
    print("I- Mostrar Heroe mas liviano.")
    print("J- Salir")

    return obtener_opcion("Ingrese una opcion: ").lower()

def confirmar_salida(mensaje: str) -> bool:
    respuesta = input(mensaje).lower()
    return respuesta == "si"

def es_texto(entrada) -> bool:
    return isinstance(entrada,str)

def obtener_opcion(mensaje):
    lista_opciones=["a","b","c","d","e","f","j","h","i","j"]

    while True:
        entrada=input(mensaje)
        if entrada in lista_opciones:

            return entrada
        else:
            print("Entrada invalida. Por favor, ingrese una opcion valida.")

flag_mas_alto= False
flag_mas_bajo= False

altura_maxima, nombre_altura_maxima= personaje_mas_alto(lista_personajes)
altura_minima, nombre_altura_minima= personaje_mas_bajo(lista_personajes)

mayor_peso, nombre_mas_pesado= personaje_mas_pesado(lista_personajes)
menor_peso, nombre_menos_pesado= personaje_menos_pesado(lista_personajes)

while True:
    match menu_superheroes():
        case "a":
            print(nombres_superheroes(lista_personajes))

        case "b":
            print(nombre_altura_superheroes(lista_personajes))

        case "c":
            print(f"La mayor altura es: {altura_maxima}")
            flag_mas_alto=True

        case "d":
            print(f"La altura minima es: {altura_minima}")
            flag_mas_bajo=True

        case "e":
            print(f"El promedio de alturas de todos los heroes es: {promedio_altura(lista_personajes)}")

        case "f":
            print(f"Nombre del heroe con la mayor altura: {nombre_altura_maxima}")

        case "g":
            print(f"Nombre del heroe con la menor altura: {nombre_altura_minima}")

        case "h":
            print(f"Nombre del heroe mas pesado: {nombre_mas_pesado}")

        case "i":
            print(f"Nombre del heroe mas liviano: {nombre_menos_pesado}")

        case "j":
            if confirmar_salida("¿Desea salir? (si/no): "):
                break

        case _:
            print("Opción no válida. Por favor, intente nuevamente.")

    pausar()    
