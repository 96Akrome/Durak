#lang scheme

(define fpi
  (lambda (funcion umbral i)
    (if (eqv? (abs (- (funcion i) i)) umbral)
        0        
        (if (< (abs (- (funcion i) i)) umbral) 
            0
            (+ 1 (fpi funcion umbral (funcion i)))))))