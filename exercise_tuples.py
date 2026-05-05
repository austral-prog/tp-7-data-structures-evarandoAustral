# Ejercicios de tuplas: búsqueda del tesoro pirata


def get_coordinate(registro):
    """
    Retorna la coordenada desde una tupla (tesoro, coordenada).
    """
    return registro[1]


def convert_coordinate(coordenada):
    """
    Convierte una coordenada como "2A" en ("2", "A").
    """
    return (coordenada[0], coordenada[1])


def create_record(registro_azara, registro_rui):
    """
    Combina los registros si las coordenadas coinciden.
    """
    tesoro = registro_azara[0]
    coordenada_azara = registro_azara[1]

    ubicacion = registro_rui[0]
    coordenada_rui = registro_rui[1]
    cuadrante = registro_rui[2]

    if convert_coordinate(coordenada_azara) == coordenada_rui:
        return (tesoro, coordenada_azara, ubicacion, coordenada_rui, cuadrante)

    return "not a match"


def sum_tuple(numeros):
    """
    Suma los elementos de una tupla sin usar sum().
    """
    total = 0

    for numero in numeros:
        total += numero

    return total


def count_occurrences(tupla, elemento):
    """
    Cuenta cuántas veces aparece un elemento sin usar count().
    """
    cantidad = 0

    for valor in tupla:
        if valor == elemento:
            cantidad += 1

    return cantidad


def find_index(tupla, elemento):
    """
    Retorna el índice de la primera aparición sin usar index().
    """
    indice_encontrado = -1
    indice = 0

    while indice < len(tupla) and indice_encontrado == -1:
        if tupla[indice] == elemento:
            indice_encontrado = indice
        indice += 1

    return indice_encontrado


def filter_positives(numeros):
    """
    Retorna una tupla con los números positivos.
    """
    positivos = []

    for numero in numeros:
        if numero > 0:
            positivos.append(numero)

    return tuple(positivos)
