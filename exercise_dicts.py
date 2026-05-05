# Ejercicios de diccionarios: sistema de inventario


def create_inventory(items):
    """
    Crea un diccionario "inventario" a partir de una lista de items.
    Cada clave es el nombre de un item y su valor es la cantidad de veces
    que aparece en la lista.
    """
    inventario = {}

    for item in items:
        if item in inventario:
            inventario[item] += 1
        else:
            inventario[item] = 1

    return inventario


def add_items(inventario, items):
    """
    Agrega una lista de items a un inventario existente.
    """
    for item in items:
        if item in inventario:
            inventario[item] += 1
        else:
            inventario[item] = 1

    return inventario


def decrement_items(inventario, items):
    """
    Resta 1 a la cantidad del inventario por cada item.
    Las cantidades no pueden quedar negativas.
    """
    for item in items:
        if item in inventario and inventario[item] > 0:
            inventario[item] -= 1

    return inventario


def remove_item(inventario, item):
    """
    Elimina un item del inventario si existe.
    """
    if item in inventario:
        del inventario[item]

    return inventario


def list_inventory(inventario):
    """
    Retorna una lista de tuplas (item, cantidad) solo con cantidad > 0.
    """
    lista = []

    for item in inventario:
        if inventario[item] > 0:
            lista.append((item, inventario[item]))

    return lista


def find_max_value(diccionario):
    """
    Retorna la clave con el valor más alto.
    Si el diccionario está vacío, retorna "".
    """
    if diccionario == {}:
        return ""

    primera_clave = True
    clave_maxima = ""
    valor_maximo = 0

    for clave in diccionario:
        if primera_clave:
            clave_maxima = clave
            valor_maximo = diccionario[clave]
            primera_clave = False
        elif diccionario[clave] > valor_maximo:
            clave_maxima = clave
            valor_maximo = diccionario[clave]

    return clave_maxima


def reverse_dict(diccionario):
    """
    Invierte un diccionario. Si varias claves tienen el mismo valor,
    concatena las claves en orden de aparición.
    """
    invertido = {}

    for clave in diccionario:
        valor = diccionario[clave]

        if valor in invertido:
            invertido[valor] += clave
        else:
            invertido[valor] = clave

    return invertido


def word_frequency(palabras):
    """
    Cuenta la frecuencia de cada palabra.
    También soporta string vacío retornando {}.
    """
    frecuencias = {}

    if palabras == "":
        return frecuencias

    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias


def find_biggest_expense(gastos):
    """
    Retorna la categoría con mayor promedio de gastos.
    """
    if gastos == {}:
        return ""

    primera_categoria = True
    categoria_mayor = ""
    promedio_mayor = 0

    for categoria in gastos:
        total = 0

        for gasto in gastos[categoria]:
            total += gasto

        if len(gastos[categoria]) == 0:
            promedio = 0
        else:
            promedio = total / len(gastos[categoria])

        if primera_categoria:
            categoria_mayor = categoria
            promedio_mayor = promedio
            primera_categoria = False
        elif promedio > promedio_mayor:
            categoria_mayor = categoria
            promedio_mayor = promedio

    return categoria_mayor


def sum_expenses(gastos):
    """
    Retorna un diccionario con la suma total de gastos por categoría.
    """
    totales = {}

    for categoria in gastos:
        total = 0

        for gasto in gastos[categoria]:
            total += gasto

        totales[categoria] = total

    return totales


def sum_expenses_by_type(gastos):
    """
    Retorna un diccionario con la suma de gastos agrupada por tipo.
    """
    totales = {}

    for categoria in gastos:
        for gasto in gastos[categoria]:
            tipo = gasto[0]
            monto = gasto[1]

            if tipo in totales:
                totales[tipo] += monto
            else:
                totales[tipo] = monto

    return totales
