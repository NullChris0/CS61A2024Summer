test = {'name': 'b',
 'points': 0.1,
 'suites': [{'cases': [{'code': 'scm> (define zeros (cons-stream 0 zeros))\n'
                                'zeros\n'
                                '\n'
                                'scm> (define ones (cons-stream 1 ones))\n'
                                'ones\n'
                                '\n'
                                'scm> (take 10 (studio-switch zeros ones))\n'
                                '(0 0 0 0 0 0 0 0 0 0)\n'
                                '\n'
                                'scm> (take 10 (studio-switch ones zeros))\n'
                                '(1 1 1 1 1 1 1 1 1 1)\n'}],
             'scored': True,
             'setup': 'scm> (load-all ".")',
             'type': 'scheme'},
            {'cases': [{'code': 'scm> (define a (cons-stream 0 (cons-stream '
                                "'guitar (cons-stream 1 (cons-stream 'guitar "
                                '(cons-stream 2 a))))))\n'
                                'a\n'
                                '\n'
                                "scm> (define b (cons-stream 'x (cons-stream "
                                "'guitar (cons-stream 'y (cons-stream 'guitar "
                                '(cons-stream 2 a))))))\n'
                                'b\n'
                                '\n'
                                'scm> (take 10 a)\n'
                                '(0 guitar 1 guitar 2 0 guitar 1 guitar 2)\n'
                                '\n'
                                'scm> (take 10 b)\n'
                                '(x guitar y guitar 2 0 guitar 1 guitar 2)\n'
                                '\n'
                                'scm> (take 10 (studio-switch a b))\n'
                                '(0 x 1 y 2 0 2 0 1 1)\n'
                                '\n'
                                'scm> (take 10 (studio-switch b b))\n'
                                '(x x y y 2 0 2 0 1 1)\n'}],
             'scored': True,
             'setup': 'scm> (load-all ".")',
             'type': 'scheme'}]}