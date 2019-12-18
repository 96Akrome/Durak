#lang scheme

(define empty '()
  )

(define (sumar_lista lst)
  (if (empty? lst)
      0
      (+ (car lst) (sum (cdr lst)))
      )
  )

;aplica la suma a cada colita de cada lista, retorna una lista de estas sumas
(every (lambda (cdr(lst)) (sumar_lista)) lst)

(define (maymecola listadelistas)
  (let 
  )