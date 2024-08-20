test = {'name': 'b',
 'points': 0.1,
 'suites': [{'cases': [{'code': '>>> t3 = Tree(10, [Tree(20, [Tree("hello", '
                                '[Tree("hello", [Tree("hello")])])]), Tree(30, '
                                '[Tree(50, [Tree("hello", '
                                '[Tree("hello")])])]), Tree(40, [Tree(70, '
                                '[Tree("hello", [Tree("hello")])])])])\n'
                                '\n'
                                '>>> print(t3)\n'
                                '10\n'
                                '    20\n'
                                '        hello\n'
                                '            hello\n'
                                '                hello\n'
                                '    30\n'
                                '        50\n'
                                '            hello\n'
                                '                hello\n'
                                '    40\n'
                                '        70\n'
                                '            hello\n'
                                '                hello\n'
                                '\n'
                                '>>> shortest_no_hello(t3)\n'
                                '[10, 20]\n'}],
             'scored': True,
             'setup': '>>> from q3 import *',
             'type': 'doctest'}]}