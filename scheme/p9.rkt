#lang scheme

(define (segm funcion lista)
  (append (filter funcion lista) (filter (negate funcion) lista))
)



"
(segm (lambda (x) (< x 4)) '(7 4 3 8 2))
"
