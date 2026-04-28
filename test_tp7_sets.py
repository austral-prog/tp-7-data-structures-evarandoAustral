import unittest
import exercise_sets as ex


class TestCleanIngredients(unittest.TestCase):

    def test_sin_duplicados(self):
        """Receta sin ingredientes duplicados"""
        result = ex.clean_ingredients(
            'Shakshuka',
            ['tomatoes', 'olive oil', 'cumin', 'harissa']
        )
        nombre, ingredientes = result
        self.assertEqual('Shakshuka', nombre)
        self.assertEqual({'tomatoes', 'olive oil', 'cumin', 'harissa'}, ingredientes)

    def test_con_duplicados(self):
        """Receta con varios ingredientes repetidos"""
        result = ex.clean_ingredients(
            'Waakye',
            ['baking soda', 'sorghum stems', 'coconut oil', 'black-eyed peas',
             'water', 'salt', 'white rice', 'baking soda', 'baking soda',
             'sorghum stems', 'sorghum stems', 'sorghum stems', 'coconut oil']
        )
        nombre, ingredientes = result
        self.assertEqual('Waakye', nombre)
        expected = {'baking soda', 'sorghum stems', 'coconut oil',
                    'black-eyed peas', 'water', 'salt', 'white rice'}
        self.assertEqual(expected, ingredientes)

    def test_retorna_tupla(self):
        """Debe retornar una tupla con (nombre, set)"""
        result = ex.clean_ingredients('Test', ['a', 'b', 'a'])
        self.assertIsInstance(result, tuple)
        self.assertEqual(2, len(result))
        self.assertIsInstance(result[1], set)

    def test_set_elimina_duplicados(self):
        """El set final debe tener los ingredientes únicos"""
        ingredientes = ['tomato', 'tomato', 'tomato', 'onion', 'onion']
        result = ex.clean_ingredients('Sauce', ingredientes)
        self.assertEqual({'tomato', 'onion'}, result[1])

    def test_lista_vacia(self):
        """Receta sin ingredientes"""
        result = ex.clean_ingredients('Agua', [])
        self.assertEqual(('Agua', set()), result)


class TestCheckDrinks(unittest.TestCase):

    def test_mocktail_simple(self):
        """Bebida sin alcohol es un Mocktail"""
        result = ex.check_drinks(
            'Honeydew Cucumber',
            ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber']
        )
        self.assertEqual('Honeydew Cucumber Mocktail', result)

    def test_cocktail_con_scotch(self):
        """Bebida con scotch es un Cocktail"""
        result = ex.check_drinks(
            'Shirley Tonic',
            ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda']
        )
        self.assertEqual('Shirley Tonic Cocktail', result)

    def test_cocktail_con_vodka(self):
        """Bebida con vodka es un Cocktail"""
        result = ex.check_drinks(
            'Moscow Mule',
            ['vodka', 'ginger beer', 'lime juice']
        )
        self.assertEqual('Moscow Mule Cocktail', result)

    def test_cocktail_con_gin(self):
        """Bebida con gin es un Cocktail"""
        result = ex.check_drinks(
            'Gin Tonic',
            ['gin', 'tonic water', 'lemon']
        )
        self.assertEqual('Gin Tonic Cocktail', result)

    def test_mocktail_jugo(self):
        """Jugo de frutas es un Mocktail"""
        result = ex.check_drinks(
            'Fruit Punch',
            ['orange juice', 'pineapple juice', 'grenadine', 'soda']
        )
        self.assertEqual('Fruit Punch Mocktail', result)

    def test_cocktail_con_rum(self):
        """Bebida con rum es un Cocktail"""
        result = ex.check_drinks(
            'Mojito',
            ['mint leaves', 'lime', 'sugar', 'rum', 'club soda']
        )
        self.assertEqual('Mojito Cocktail', result)


class TestUniqueChars(unittest.TestCase):

    def test_hello(self):
        """Caracteres únicos de 'hello'"""
        result = ex.unique_chars("hello")
        self.assertEqual({'h', 'e', 'l', 'o'}, result)

    def test_string_vacio(self):
        """String vacío retorna set vacío"""
        result = ex.unique_chars("")
        self.assertEqual(set(), result)

    def test_todos_distintos(self):
        """Todos los caracteres son distintos"""
        result = ex.unique_chars("abcdef")
        self.assertEqual({'a', 'b', 'c', 'd', 'e', 'f'}, result)

    def test_todos_iguales(self):
        """Todos los caracteres son iguales"""
        result = ex.unique_chars("aaaa")
        self.assertEqual({'a'}, result)

    def test_con_espacios(self):
        """Incluye espacios como caracteres válidos"""
        result = ex.unique_chars("ab ba")
        self.assertEqual({'a', 'b', ' '}, result)


class TestSumSet(unittest.TestCase):

    def test_suma_simple(self):
        """Suma de un set de enteros"""
        self.assertEqual(10, ex.sum_set({1, 2, 3, 4}))

    def test_set_vacio(self):
        """Set vacío retorna 0"""
        self.assertEqual(0, ex.sum_set(set()))

    def test_un_solo_elemento(self):
        """Set con un solo elemento"""
        self.assertEqual(42, ex.sum_set({42}))

    def test_set_con_negativos(self):
        """Set con números negativos"""
        self.assertEqual(0, ex.sum_set({-5, 5, -3, 3}))

    def test_set_con_flotantes(self):
        """Set con flotantes"""
        self.assertAlmostEqual(4.5, ex.sum_set({1.5, 3.0}))


class TestCommonElements(unittest.TestCase):

    def test_interseccion_parcial(self):
        """Intersección con elementos en común"""
        self.assertEqual({2, 3}, ex.common_elements({1, 2, 3}, {2, 3, 4}))

    def test_sin_elementos_en_comun(self):
        """Sin elementos en común retorna set vacío"""
        self.assertEqual(set(), ex.common_elements({1, 2}, {3, 4}))

    def test_ambos_vacios(self):
        """Ambos sets vacíos"""
        self.assertEqual(set(), ex.common_elements(set(), set()))

    def test_un_set_vacio(self):
        """Un set vacío y otro con elementos"""
        self.assertEqual(set(), ex.common_elements(set(), {1, 2, 3}))

    def test_sets_iguales(self):
        """Sets idénticos retornan todos los elementos"""
        self.assertEqual({1, 2, 3}, ex.common_elements({1, 2, 3}, {1, 2, 3}))

    def test_retorna_set(self):
        """El resultado debe ser un set"""
        result = ex.common_elements({1, 2}, {2, 3})
        self.assertIsInstance(result, set)


if __name__ == '__main__':
    unittest.main()
