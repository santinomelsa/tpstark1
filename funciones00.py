def nombres_superheroes(lista):
    return [heroe["nombre"] for heroe in lista]

def nombre_altura_superheroes(lista):
    return [(heroe["nombre"], heroe["altura"]) for heroe in lista]

def personaje_mas_alto(lista):
    heroe_mas_alto = lista[0]
    for heroe in lista:
        if float(heroe["altura"]) > float(heroe_mas_alto["altura"]):
            heroe_mas_alto = heroe
    return float(heroe_mas_alto["altura"]), heroe_mas_alto["nombre"]

def personaje_mas_bajo(lista):
    heroe_mas_bajo = lista[0]
    for heroe in lista:
        if float(heroe["altura"]) < float(heroe_mas_bajo["altura"]):
            heroe_mas_bajo = heroe
    return float(heroe_mas_bajo["altura"]), heroe_mas_bajo["nombre"]

def promedio_altura(lista):
    total_altura = sum(float(heroe["altura"]) for heroe in lista)
    cantidad_heroes = len(lista)
    return total_altura / cantidad_heroes

def personaje_mas_pesado(lista):
    heroe_mas_pesado = lista[0]
    for heroe in lista:
        if float(heroe["peso"]) > float(heroe_mas_pesado["peso"]):
            heroe_mas_pesado = heroe
    return float(heroe_mas_pesado["peso"]), heroe_mas_pesado["nombre"]

def personaje_menos_pesado(lista):
    heroe_menos_pesado = lista[0]
    for heroe in lista:
        if float(heroe["peso"]) < float(heroe_menos_pesado["peso"]):
            heroe_menos_pesado = heroe
    return float(heroe_menos_pesado["peso"]), heroe_menos_pesado["nombre"]
