# TP7 - Trabajo Práctico 7

## Temas evaluados

Estructuras de datos en Python: **tuplas**, **sets (conjuntos)** y **diccionarios**. Operaciones, métodos y patrones comunes para cada una.

## Cómo ejecutar los tests

Para verificar todos los ejercicios en el directorio actual:

```bash
python3 -m unittest discover
```

Para verificar un ejercicio en particular:

```bash
python3 -m unittest test_tp7_tuples
```

O ejecutar directamente:

```bash
python3 test_tp7_tuples.py
```

---

## Parte 1 — Tuplas

Azara y Rui son compañeros de equipo en una búsqueda del tesoro pirata.
Uno tiene una lista de tesoros con coordenadas, el otro una lista de ubicaciones con coordenadas.

**Lista de Azara:**

| Tesoro                      | Coordenada |
| --------------------------- | ---------- |
| Amethyst Octopus            | 1F         |
| Angry Monkey Figurine       | 5B         |
| Antique Glass Fishnet Float | 3D         |
| Brass Spyglass              | 4B         |
| Carved Wooden Elephant      | 8C         |

**Lista de Rui:**

| Ubicación                             | Coordenada  | Cuadrante |
| ------------------------------------- | ----------- | --------- |
| Seaside Cottages                      | ("1", "C")  | Blue      |
| Aqua Lagoon (Island of Mystery)       | ("1", "F")  | Yellow    |
| Abandoned Lighthouse                  | ("4", "B")  | Blue      |
| Stormy Breakwater                     | ("5", "B")  | Purple    |
| Foggy Seacave                         | ("8", "C")  | Purple    |

Las coordenadas de Azara y Rui están con formatos distintos. Ayudá a organizarlas.

Todos los ejercicios de esta parte se resuelven en el mismo archivo: `exercise_tuples.py`.

**Archivo de test:** `test_tp7_tuples.py`

---

### Ejercicio 1 — `get_coordinate`

**Conceptos:** acceso a elementos de una tupla por índice.

**Consigna:** Implementar `get_coordinate(registro)` que recibe una tupla `(tesoro, coordenada)` y devuelve solo la coordenada.

**Ejemplo:** Para `('Scrimshawed Whale Tooth', '2A')` la salida esperada es:

```
'2A'
```

---

### Ejercicio 2 — `convert_coordinate`

**Conceptos:** creación de tuplas, acceso a caracteres de un string.

**Consigna:** Implementar `convert_coordinate(coordenada)` que recibe una coordenada en formato `"2A"` y devuelve una tupla `("2", "A")` con sus componentes.

**Ejemplo:** Para `"2A"` la salida esperada es:

```
('2', 'A')
```

Para `"7F"` la salida esperada es:

```
('7', 'F')
```

---

### Ejercicio 3 — `create_record`

**Conceptos:** combinación de tuplas, reutilización de funciones, comparación.

**Consigna:** Implementar `create_record(registro_azara, registro_rui)` que combine ambos registros si las coordenadas coinciden.

- `registro_azara`: tupla `(tesoro, coordenada)` → ej: `('Brass Spyglass', '4B')`
- `registro_rui`: tupla `(ubicacion, coordenada, cuadrante)` → ej: `('Abandoned Lighthouse', ('4', 'B'), 'Blue')`

Si las coordenadas coinciden, retornar `(tesoro, coordenada_azara, ubicacion, coordenada_rui, cuadrante)`.
Si NO coinciden, retornar el string `"not a match"`.

**Ejemplo:**

```python
create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
# → ('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')

create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'Blue'))
# → 'not a match'
```

**Tip:** podés reutilizar `get_coordinate` y `convert_coordinate` para normalizar las coordenadas antes de compararlas.

---

### Ejercicio 4 — `sum_tuple`

**Conceptos:** iteración con `for` sobre una tupla, acumulador.

**Consigna:** Implementar `sum_tuple(numeros)` que recorra la tupla con un `for` (o `while`) y retorne la suma total. Si la tupla está vacía, retornar 0.

**No se permite usar `sum()`.**

**Ejemplo:**

```python
sum_tuple((1, 2, 3, 4, 5))  # → 15
sum_tuple(())               # → 0
sum_tuple((10, -15, 5, -5)) # → -5
```

---

### Ejercicio 5 — `count_occurrences`

**Conceptos:** recorrido con `for`, contador, comparación.

**Consigna:** Implementar `count_occurrences(tupla, elemento)` que recorra la tupla y cuente cuántas veces aparece `elemento`.

**No se permite usar el método `.count()`.**

**Ejemplo:**

```python
count_occurrences((1, 2, 2, 3, 2), 2)            # → 3
count_occurrences(('a', 'b', 'a'), 'c')          # → 0
count_occurrences((), 'x')                       # → 0
```

---

### Ejercicio 6 — `find_index`

**Conceptos:** iteración y retorno temprano.

**Consigna:** Implementar `find_index(tupla, elemento)` que retorne el índice de la **primera** aparición del elemento. Si no se encuentra, retornar `-1`.

**No se permite usar el método `.index()`.**

**Ejemplo:**

```python
find_index(('a', 'b', 'c', 'b'), 'b')  # → 1
find_index((1, 2, 3), 9)               # → -1
find_index((), 'x')                    # → -1
```

---

### Ejercicio 7 — `filter_positives`

**Conceptos:** iteración, construcción de una nueva tupla, filtrado.

**Consigna:** Implementar `filter_positives(numeros)` que recorra la tupla y retorne una **nueva tupla** con solo los números positivos (> 0). El 0 NO es positivo.

**Ejemplo:**

```python
filter_positives((-3, 1, 0, 5, -2, 7))  # → (1, 5, 7)
filter_positives((-1, -2, -3))          # → ()
filter_positives((0, 0, 0))             # → ()
```

---

## Parte 2 — Sets (Conjuntos)

Ejercicios sobre sets: aplicaciones reales (catering) y operaciones recorriendo la estructura con `for` / `while`.

Todos los ejercicios de esta parte se resuelven en el mismo archivo: `exercise_sets.py`.

**Archivo de test:** `test_tp7_sets.py`

---

### Ejercicio 8 — `clean_ingredients`

**Conceptos:** conversión de lista a `set`, eliminación de duplicados.

**Consigna:** Las recetas fueron agregadas desde varias fuentes y tienen ingredientes duplicados. Implementar `clean_ingredients(nombre_plato, ingredientes)` que retorne una tupla `(nombre_plato, set_de_ingredientes)` sin duplicados.

**Ejemplo:**

```python
clean_ingredients('Punjabi-Style Chole',
                  ['onions', 'tomatoes', 'ginger paste', 'ginger paste',
                   'chickpeas', 'chickpeas'])
# → ('Punjabi-Style Chole',
#    {'onions', 'tomatoes', 'ginger paste', 'chickpeas'})
```

---

### Ejercicio 9 — `check_drinks`

**Conceptos:** operador `in` con sets, iteración, retorno temprano.

**Consigna:** El evento incluye cócteles y mocktails. Implementar `check_drinks(nombre_bebida, ingredientes)` que devuelva:

- `"<nombre> Cocktail"` si algún ingrediente está en el set `ALCOHOLS` (definido al inicio del archivo).
- `"<nombre> Mocktail"` si ningún ingrediente es alcohólico.

**Ejemplo:**

```python
check_drinks('Honeydew Cucumber',
             ['honeydew', 'coconut water', 'mint leaves', 'lime juice'])
# → 'Honeydew Cucumber Mocktail'

check_drinks('Shirley Tonic',
             ['cinnamon stick', 'scotch', 'whole cloves', 'ginger'])
# → 'Shirley Tonic Cocktail'
```

---

### Ejercicio 10 — `unique_chars`

**Conceptos:** construcción de un set desde un string.

**Consigna:** Implementar `unique_chars(texto)` que reciba un string y devuelva un `set` con los caracteres únicos.

**Ejemplo:**

```python
unique_chars("hello")
# → {'h', 'e', 'l', 'o'}

unique_chars("")
# → set()
```

---

### Ejercicio 11 — `sum_set`

**Conceptos:** iteración con `for` sobre un set, acumulador.

**Consigna:** Implementar `sum_set(numeros)` que recorra el set y retorne la suma de sus elementos. Si el set está vacío, retornar 0.

**No se permite usar `sum()`.**

**Ejemplo:**

```python
sum_set({1, 2, 3, 4})   # → 10
sum_set(set())          # → 0
sum_set({-5, 5, -3, 3}) # → 0
```

---

### Ejercicio 12 — `common_elements`

**Conceptos:** iteración sobre set, pertenencia con `in`, construcción de un set nuevo.

**Consigna:** Implementar `common_elements(set_a, set_b)` que retorne un nuevo set con los elementos que aparecen en **ambos** sets.

**No se permite usar `&` ni `.intersection()`.** La idea es recorrer uno de los sets y verificar con `in` si el elemento está también en el otro.

**Ejemplo:**

```python
common_elements({1, 2, 3}, {2, 3, 4})  # → {2, 3}
common_elements({1, 2}, {3, 4})        # → set()
common_elements({1, 2, 3}, {1, 2, 3})  # → {1, 2, 3}
```

---

## Parte 3 — Diccionarios

Esta parte tiene dos bloques. El primero trabaja sobre un sistema de inventario (crear, agregar, descontar, eliminar, listar ítems). El segundo introduce operaciones más generales sobre diccionarios: búsqueda del máximo, inversión, frecuencia de palabras y análisis de gastos.

Todos los ejercicios se resuelven en el mismo archivo: `exercise_dicts.py`.

**Archivo de test:** `test_tp7_dicts.py`

---

### Ejercicio 13 — `create_inventory`

**Conceptos:** creación de diccionarios, conteo de ocurrencias.

**Consigna:** Implementar `create_inventory(items)` que reciba una lista y devuelva un `dict` con cada item y la cantidad de veces que aparece.

**Ejemplo:**

```python
create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
# → {"coal": 1, "wood": 2, "diamond": 3}
```

---

### Ejercicio 14 — `add_items`

**Conceptos:** acceso y modificación de diccionarios, operador `in`.

**Consigna:** Implementar `add_items(inventario, items)` que agregue cada elemento de la lista al inventario. Si el item ya existe, incrementar su cantidad en 1; si no, agregarlo con cantidad 1.

**Ejemplo:**

```python
add_items({"coal": 1}, ["wood", "iron", "coal", "wood"])
# → {"coal": 2, "wood": 2, "iron": 1}
```

---

### Ejercicio 15 — `decrement_items`

**Conceptos:** modificación de diccionarios, validaciones de rango.

**Consigna:** Implementar `decrement_items(inventario, items)` que reste 1 por cada aparición del item en la lista. **Las cantidades no pueden ser negativas**: si un item aparece más veces que su stock, debe quedar en 0 y las solicitudes extra se ignoran.

**Ejemplo:**

```python
decrement_items({"coal": 3, "diamond": 1, "iron": 5},
                ["diamond", "coal", "iron", "iron"])
# → {"coal": 2, "diamond": 0, "iron": 3}

decrement_items({"coal": 2, "wood": 1, "diamond": 2},
                ["coal", "coal", "wood", "wood", "diamond"])
# → {"coal": 0, "wood": 0, "diamond": 1}
```

---

### Ejercicio 16 — `remove_item`

**Conceptos:** eliminación con `del` o `pop`, validación con `in`.

**Consigna:** Implementar `remove_item(inventario, item)` que elimine por completo el item del inventario. Si el item no existe, retornar el inventario sin cambios.

**Ejemplo:**

```python
remove_item({"coal": 2, "wood": 1, "diamond": 2}, "coal")
# → {"wood": 1, "diamond": 2}

remove_item({"coal": 2, "wood": 1, "diamond": 2}, "gold")
# → {"coal": 2, "wood": 1, "diamond": 2}
```

---

### Ejercicio 17 — `list_inventory`

**Conceptos:** método `.items()`, list comprehension, filtrado.

**Consigna:** Implementar `list_inventory(inventario)` que retorne una lista de tuplas `(item, cantidad)` con los items disponibles. **Solo incluir los items con cantidad mayor a 0.**

**Ejemplo:**

```python
list_inventory({"coal": 7, "wood": 11, "diamond": 2, "iron": 7, "silver": 0})
# → [('coal', 7), ('wood', 11), ('diamond', 2), ('iron', 7)]
```

---

### Ejercicio 18 — `find_max_value`

**Conceptos:** iteración con `.items()`, comparación de valores, caso borde para dict vacío.

**Consigna:** Implementar `find_max_value(diccionario)` que reciba un diccionario de nombres (claves) y puntajes (valores), y devuelva el nombre asociado al puntaje más alto. Si el diccionario está vacío, retornar `""`.

**Ejemplo:**

```python
find_max_value({'John': 85, 'Emma': 92, 'Sophia': 78})
# → 'Emma'

find_max_value({})
# → ''
```

---

### Ejercicio 19 — `reverse_dict`

**Conceptos:** inversión de diccionarios, acumulación de claves duplicadas.

**Consigna:** Implementar `reverse_dict(diccionario)` que invierta el diccionario usando los valores como claves. Si varias claves comparten el mismo valor, sus nombres se concatenan (en orden de aparición) como una sola cadena.

**Ejemplo:**

```python
reverse_dict({'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 2})
# → {1: 'a', 2: 'be', 3: 'cd'}

reverse_dict({})
# → {}
```

---

### Ejercicio 20 — `word_frequency`

**Conceptos:** conteo de ocurrencias con diccionario, operador `in`.

**Consigna:** Implementar `word_frequency(palabras)` que reciba una lista de palabras y retorne un `dict` con la frecuencia de cada una. Debe soportar también el caso de recibir un string vacío, retornando `{}`.

**Ejemplo:**

```python
word_frequency(["apple", "banana", "apple", "orange", "banana", "apple"])
# → {'apple': 3, 'banana': 2, 'orange': 1}

word_frequency("")
# → {}
```

---

### Ejercicio 21 — `find_biggest_expense`

**Conceptos:** promedio de listas, iteración sobre `.items()`, comparación.

**Consigna:** Implementar `find_biggest_expense(gastos)` que reciba un diccionario donde cada clave es una categoría y su valor una lista de gastos. Retornar la categoría cuyo **promedio** sea más alto. Si el diccionario está vacío, retornar `""`.

**Ejemplo:**

```python
find_biggest_expense({'Food': [60, 80, 100],
                      'Transport': [10, 1, 2],
                      'Games': [10, 20, 30]})
# → 'Food'
```

---

### Ejercicio 22 — `sum_expenses`

**Conceptos:** construcción de diccionarios con `sum`, dict comprehension.

**Consigna:** Implementar `sum_expenses(gastos)` que reciba el mismo formato de entrada que el ejercicio anterior y retorne un nuevo diccionario con la **suma total** de los gastos por categoría.

**Ejemplo:**

```python
sum_expenses({'Food': [60, 80, 100],
              'Transport': [10, 1, 2],
              'Games': [10, 20, 30]})
# → {'Food': 240, 'Transport': 13, 'Games': 60}
```

---

### Ejercicio 23 — `sum_expenses_by_type`

**Conceptos:** iteración anidada, agrupamiento por clave, uso de `.get()`.

**Consigna:** Implementar `sum_expenses_by_type(gastos)` que reciba un diccionario donde cada categoría tiene una lista de tuplas `(tipo, monto)`. Retornar un nuevo diccionario con la suma de los montos agrupados por **tipo** (ignorando la categoría).

**Ejemplo:**

```python
sum_expenses_by_type({
    'Food': [("A", 60), ("B", 100), ("A", 20)],
    'Transport': [("A", 10), ("B", 50), ("C", 5)],
    'Games': [("A", 6), ("B", 24), ("C", 99)]
})
# → {'A': 96, 'B': 174, 'C': 104}
```
