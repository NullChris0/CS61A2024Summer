test = {'name': 'd',
 'points': 0.1,
 'suites': [{'cases': [{'code': '>>> tomato = Item("tomato", 4, "vegetable")\n'
                                '\n'
                                '>>> kale = Item("kale", 1, "vegetable")\n'
                                '\n'
                                '>>> apple = Item("apple", 2, "fruit")\n'
                                '\n'
                                '>>> chicken = Item("chicken", 3, "meat")\n'
                                '\n'
                                '>>> oreos = Item("oreos", 6, "junk_food")\n'
                                '\n'
                                '>>> stuff = GroceryList([tomato, kale, apple, '
                                'chicken, oreos])\n'
                                '\n'
                                '>>> [i for i in stuff.generate_list(1, '
                                '["vegetable"])]\n'
                                '[kale]\n'
                                '\n'
                                '>>> [i for i in stuff.generate_list(1, '
                                '["fruit"])]\n'
                                '[]\n'
                                '\n'
                                '>>> [i for i in stuff.generate_list(10, '
                                '["vegetable", "fruit", "junk_food"])]\n'
                                '[tomato, kale, apple]\n'
                                '\n'
                                '>>> [i for i in stuff.generate_list(50, '
                                '["vegetable", "fruit", "junk_food", '
                                '"meat"])]\n'
                                '[tomato, kale, apple, chicken, oreos]\n'}],
             'scored': True,
             'setup': '>>> from q5 import *',
             'type': 'doctest'}]}