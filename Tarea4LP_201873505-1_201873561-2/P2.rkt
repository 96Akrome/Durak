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


(define (maxmin lst)
  (let loop ( (x -inf.0) (y +inf.0)  (lst (map (lambda (lst)(list (car lst) (sum (cdr lst)))) lst)))
    (if (empty? lst)
        (list x y)
        (loop (max (car lst) x) (min (car lst) y) (car lst))))
  )
