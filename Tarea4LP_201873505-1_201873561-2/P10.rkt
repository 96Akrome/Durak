#lang scheme

(define (serie funcion entero)
  (if (< entero 0) (error "Entero ingresado es negativo!")
      (if (= entero 0)
          0
          (+ (funcion entero) (serie funcion (- entero 1)))
          )
      )
  )