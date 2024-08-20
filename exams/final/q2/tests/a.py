test = {'name': 'a',
 'points': 0.1,
 'suites': [{'cases': [{'code': 'scm> (ladder-locator 10)\n'
                                '(1 0)\n'
                                '\n'
                                'scm> (ladder-locator 10001)\n'
                                '(1 0 0 0 1)\n'
                                '\n'
                                'scm> (ladder-locator 8080)\n'
                                '((8) 0 (8) 0)\n'
                                '\n'
                                'scm> (ladder-locator 123456780)\n'
                                '(1 2 3 4 5 6 7 (8) 0)\n'}],
             'scored': True,
             'setup': 'scm> (load-all ".")',
             'type': 'scheme'}]}