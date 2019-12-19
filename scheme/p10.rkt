#lang scheme

(define (serie funcion entero)
  (let sum ((i entero) (n 0))
    (if (= i 0)
        n
        (sum (- i 1) (+ n (funcion i))))))

"
(serie (lambda (x) (* x x)) 3)
"