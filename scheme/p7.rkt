#lang scheme

(define fpi
  (lambda (funcion umbral i)
    (if (<= (abs (- (funcion i) i)) umbral) 
        0
        (+ 1 (fpi funcion umbral (funcion i))))))