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