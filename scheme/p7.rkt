#lang scheme

(define fpi
  (lambda (funcion umbral i)
    (if (or (equal? (real->decimal-string (abs(- i (funcion i))) 14) (real->decimal-string umbral 14)) (< (abs(- i (funcion i))) umbral))
        0
        (+ 1 (fpi funcion umbral (funcion i))))))