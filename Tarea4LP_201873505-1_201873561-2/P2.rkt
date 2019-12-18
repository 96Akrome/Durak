#lang scheme

(define empty '())

(define (sum lst)
  (if (empty? lst)
      0
      (+ (car lst) (sum (cdr lst)))
      )
  )


(define (mapear_suma lst)
  (map (lambda (lst) (sum lst)) lst)
  )
;(mapear_suma '((0 0 9) (1 1 1 1 1)))
;(9 5)

;para hacer : pasar la lista por maxlst y minlst, quiza fusionar las 2 funciones, retornar tupla maxsuma, minsuma, buscar su pos en lista actual, retornar cabezas.

(define (maxlst lst)
  (cond
    ( (= (length lst) 0) writeln "Lista vacia, no tiene maximo")
    ((= (length lst) 1)(first lst))
    (else (max (car lst) (maxlst (cdr lst)))
          )
    )
  )

(define (minlst lst)
  (cond
    ((= (length lst) 0) writeln "Lista vacia, no tiene maximo")
    ((= (length lst) 1)(first lst))
    (else (min (car lst) (minlst (cdr lst)))
          )
    )
  )