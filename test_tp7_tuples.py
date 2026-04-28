import unittest
import exercise_tuples as ex


class TestGetCoordinate(unittest.TestCase):

    def test_coordenada_simple(self):
        """Extraer coordenada de una tupla básica"""
        result = ex.get_coordinate(('Scrimshawed Whale Tooth', '2A'))
        self.assertEqual('2A', result)

    def test_coordenada_con_letra_f(self):
        """Extraer coordenada con columna F"""
        result = ex.get_coordinate(('Pirate Flag', '7F'))
        self.assertEqual('7F', result)

    def test_coordenada_con_numero_alto(self):
        """Extraer coordenada con un número alto"""
        result = ex.get_coordinate(('Model Ship in Large Bottle', '8A'))
        self.assertEqual('8A', result)

    def test_coordenada_1c(self):
        """Extraer coordenada 1C"""
        result = ex.get_coordinate(('Robot Parrot', '1C'))
        self.assertEqual('1C', result)

    def test_coordenada_distinta(self):
        """Extraer coordenada 4E"""
        result = ex.get_coordinate(('Silver Seahorse', '4E'))
        self.assertEqual('4E', result)


class TestConvertCoordinate(unittest.TestCase):

    def test_coordenada_2a(self):
        """Convertir coordenada 2A"""
        result = ex.convert_coordinate('2A')
        self.assertEqual(('2', 'A'), result)

    def test_coordenada_7f(self):
        """Convertir coordenada 7F"""
        result = ex.convert_coordinate('7F')
        self.assertEqual(('7', 'F'), result)

    def test_coordenada_1c(self):
        """Convertir coordenada 1C"""
        result = ex.convert_coordinate('1C')
        self.assertEqual(('1', 'C'), result)

    def test_coordenada_8a(self):
        """Convertir coordenada 8A"""
        result = ex.convert_coordinate('8A')
        self.assertEqual(('8', 'A'), result)

    def test_retorna_tupla(self):
        """El resultado debe ser una tupla, no una lista"""
        result = ex.convert_coordinate('4E')
        self.assertIsInstance(result, tuple)


class TestCreateRecord(unittest.TestCase):

    def test_coincidencia_simple(self):
        """Coordenadas coinciden: 5B"""
        azara = ('Angry Monkey Figurine', '5B')
        rui = ('Stormy Breakwater', ('5', 'B'), 'Purple')
        result = ex.create_record(azara, rui)
        expected = ('Angry Monkey Figurine', '5B', 'Stormy Breakwater', ('5', 'B'), 'Purple')
        self.assertEqual(expected, result)

    def test_coincidencia_8c(self):
        """Coordenadas coinciden: 8C"""
        azara = ('Carved Wooden Elephant', '8C')
        rui = ('Foggy Seacave', ('8', 'C'), 'Purple')
        result = ex.create_record(azara, rui)
        expected = ('Carved Wooden Elephant', '8C', 'Foggy Seacave', ('8', 'C'), 'Purple')
        self.assertEqual(expected, result)

    def test_coincidencia_1f(self):
        """Coordenadas coinciden: 1F"""
        azara = ('Amethyst Octopus', '1F')
        rui = ('Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')
        result = ex.create_record(azara, rui)
        expected = ('Amethyst Octopus', '1F', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')
        self.assertEqual(expected, result)

    def test_no_coincide_diferente_numero(self):
        """Las coordenadas no coinciden en el número"""
        azara = ('Amethyst Octopus', '1F')
        rui = ('Seaside Cottages', ('1', 'C'), 'Blue')
        result = ex.create_record(azara, rui)
        self.assertEqual('not a match', result)

    def test_no_coincide_diferente_letra(self):
        """Las coordenadas no coinciden en la letra"""
        azara = ('Angry Monkey Figurine', '5B')
        rui = ('Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')
        result = ex.create_record(azara, rui)
        self.assertEqual('not a match', result)

    def test_no_coincide_completamente(self):
        """Coordenadas totalmente distintas"""
        azara = ('Brass Spyglass', '4B')
        rui = ('Spiky Rocks', ('3', 'D'), 'Yellow')
        result = ex.create_record(azara, rui)
        self.assertEqual('not a match', result)


class TestSumTuple(unittest.TestCase):

    def test_suma_positivos(self):
        """Suma de enteros positivos"""
        self.assertEqual(15, ex.sum_tuple((1, 2, 3, 4, 5)))

    def test_tupla_vacia(self):
        """Tupla vacía retorna 0"""
        self.assertEqual(0, ex.sum_tuple(()))

    def test_un_solo_elemento(self):
        """Un solo elemento retorna ese valor"""
        self.assertEqual(7, ex.sum_tuple((7,)))

    def test_suma_con_negativos(self):
        """Mezcla de positivos y negativos"""
        self.assertEqual(-5, ex.sum_tuple((10, -15, 5, -5)))

    def test_suma_con_flotantes(self):
        """Suma de flotantes"""
        self.assertAlmostEqual(6.0, ex.sum_tuple((1.5, 2.5, 2.0)))


class TestCountOccurrences(unittest.TestCase):

    def test_contar_enteros(self):
        """Contar un entero repetido"""
        self.assertEqual(3, ex.count_occurrences((1, 2, 2, 3, 2), 2))

    def test_elemento_no_presente(self):
        """Elemento inexistente retorna 0"""
        self.assertEqual(0, ex.count_occurrences(('a', 'b', 'a'), 'c'))

    def test_tupla_vacia(self):
        """Tupla vacía retorna 0"""
        self.assertEqual(0, ex.count_occurrences((), 'x'))

    def test_todos_iguales(self):
        """Todos los elementos son iguales"""
        self.assertEqual(4, ex.count_occurrences(('x', 'x', 'x', 'x'), 'x'))

    def test_contar_string_en_tupla(self):
        """Contar strings en una tupla"""
        self.assertEqual(3, ex.count_occurrences(('rojo', 'azul', 'rojo', 'verde', 'rojo'), 'rojo'))


class TestFindIndex(unittest.TestCase):

    def test_primera_aparicion(self):
        """Retorna el índice de la primera aparición"""
        self.assertEqual(1, ex.find_index(('a', 'b', 'c', 'b'), 'b'))

    def test_elemento_no_encontrado(self):
        """Elemento inexistente retorna -1"""
        self.assertEqual(-1, ex.find_index((1, 2, 3), 9))

    def test_tupla_vacia(self):
        """Tupla vacía retorna -1"""
        self.assertEqual(-1, ex.find_index((), 'x'))

    def test_elemento_en_posicion_cero(self):
        """Elemento en la primera posición"""
        self.assertEqual(0, ex.find_index(('x', 'y', 'z'), 'x'))

    def test_elemento_en_ultima_posicion(self):
        """Elemento en la última posición"""
        self.assertEqual(3, ex.find_index((10, 20, 30, 40), 40))


class TestFilterPositives(unittest.TestCase):

    def test_filtro_mixto(self):
        """Mezcla de positivos, negativos y cero"""
        self.assertEqual((1, 5, 7), ex.filter_positives((-3, 1, 0, 5, -2, 7)))

    def test_todos_negativos(self):
        """Todos negativos retorna tupla vacía"""
        self.assertEqual((), ex.filter_positives((-1, -2, -3)))

    def test_todos_positivos(self):
        """Todos positivos retorna la tupla completa"""
        self.assertEqual((1, 2, 3), ex.filter_positives((1, 2, 3)))

    def test_tupla_vacia(self):
        """Tupla vacía retorna tupla vacía"""
        self.assertEqual((), ex.filter_positives(()))

    def test_cero_no_es_positivo(self):
        """El 0 no se considera positivo"""
        self.assertEqual((), ex.filter_positives((0, 0, 0)))

    def test_retorna_tupla(self):
        """El resultado debe ser una tupla"""
        result = ex.filter_positives((1, -1, 2))
        self.assertIsInstance(result, tuple)


if __name__ == '__main__':
    unittest.main()
