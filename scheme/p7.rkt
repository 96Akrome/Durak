#lang scheme

(define fpi
  (lambda (funcion umbral i)
    (if (or (eqv? (abs (- (funcion i) i)) umbral) (< (abs (- (funcion i) i)) umbral))
        0         
        (+ 1 (fpi funcion umbral (funcion i))))))