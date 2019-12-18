#lang scheme

(define empty '()
  )

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

(define (maxlst lst)
  (cond
    ( empty? lst writeln "Lista vacia, no tiene maximo")
    ((= (length lst) 1)(car lst))
    (else max((car lst)(maxlst (cdr lst)))
          )
    )
  )

(define (minlst lst)
  (cond
    (empty? lst writeln "Lista vacia, no tiene minimo.")
    ((= (length lst) 1)(car lst))
    (else (min((car lst))(minlst (cdr lst)))
          )
    )
  )