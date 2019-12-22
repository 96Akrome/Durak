#lang scheme

(define (fpi funcion umbral i)
  (let iterar ((abs (lambda (x)(if (> x 0) x (* x -1)))) (num i) (iteraciones 0))
    (if (<= (abs (- (funcion num) num)) umbral)
        iteraciones
        (iterar (lambda (x)(if (> x 0) x (* x -1))) (funcion num) (+ iteraciones 1)))))





