#lang scheme

(define (serie funcion entero)
  (if (= entero 0)
      0
      (+ (funcion entero) (serie funcion (- entero 1)))
      )
  )