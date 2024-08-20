test = {'name': 'a',
 'points': 0.1,
 'suites': [{'cases': [{'code': "scm> (cabinet-filter '(1 2 3) (lambda (x) (= "
                                'x 2)))\n'
                                '(1 3)\n'
                                '\n'
                                "scm> (cabinet-filter '(1 2 3) (lambda (x) "
                                '(list? x)))\n'
                                '(1 2 3)\n'
                                '\n'
                                "scm> (cabinet-filter '(1 (2 3)) (lambda (x) "
                                '(list? x)))\n'
                                '(1)\n'
                                '\n'
                                "scm> (cabinet-filter '((1) (2 3)) (lambda (x) "
                                '(list? x)))\n'
                                '()\n'
                                '\n'
                                "scm> (cabinet-filter '((1) (2 3)) (lambda (x) "
                                '(and (list? x) (equal? (car x) 2))))\n'
                                '((1))\n'}],
             'scored': True,
             'setup': 'scm> (load-all ".")',
             'type': 'scheme'}]}