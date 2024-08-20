(define (over-or-under num1 num2)
  (cond 
    ((< num1 num2) -1)
    ((= num1 num2) 0)
    (else          1)))

(define (make-adder num) (lambda (x) (+ x num)))

(define (composed f g) (lambda (x) (f (g x))))

; repeat 1 time = f (repeat 0 time) = x
; repeat 2 times = f (repeat 1 time) = f (x)
; repeat 3 times = f (repeat 2 times) = f (f (x))
; notice that repeat returns procedure, so call ((repeat f (- n 1)) x) as recursion
(define (repeat f n)
  (lambda (x)
    (if (= n 0)
        x
        (f ((repeat f (- n 1)) x)))))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (if (zero? b)
      a
      (gcd b (modulo a b))))

(define (duplicate lst)
  (if (null? lst)
      nil
      (cons (car lst)
            (cons (car lst) (duplicate (cdr lst))))))

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (deep-map fn s)
  (map (lambda (x)
         (if (list? x)
             (deep-map fn x)
             (fn x)))
       s))
