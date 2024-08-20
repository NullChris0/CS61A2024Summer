(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values)
  (list keys values))

(define (get-keys-kwlist1 kwlist) (car kwlist))

(define (get-values-kwlist1 kwlist) (cadr kwlist))

(define (make-kwlist2 keys values)
  (define (reverse s r)
    (if (null? s)
        r
        (reverse (cdr s) (cons (car s) r))))
  (define (reverse-make k v r)
    (if (and (null? k) (null? v))
        r
        (reverse-make (cdr k)
                      (cdr v)
                      (cons (list (car k) (car v)) r))))
  (reverse (reverse-make keys values '()) '()))

(define (get-keys-kwlist2 kwlist)
  (map car kwlist))

(define (get-values-kwlist2 kwlist)
  (map cadr kwlist))

(define (add-to-kwlist kwlist key value)
  (make-kwlist
   (append (get-keys-kwlist kwlist) (list key))
   (append (get-values-kwlist kwlist) (list value))))

(define (get-first-from-kwlist kwlist key)
  (if (null? (get-keys-kwlist kwlist))
      nil
      (let ((values (get-values-kwlist kwlist))
            (keys (get-keys-kwlist kwlist)))
        (cond 
          ((equal? (car keys) key)
           (car values))
          (else
           (get-first-from-kwlist
            (make-kwlist (cdr keys) (cdr values))
            key))))))
