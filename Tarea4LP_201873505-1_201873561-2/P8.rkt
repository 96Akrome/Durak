#lang scheme
;;(pairs x)
;;Recibe una lista, denotada como x, y agrupa el elemento i y i+1 en una lista interna.
;;Retorna lista de pares de números consecutivos. Ej: (1 2 3 4) -> (1 2)(2 3)(3 4).
(define (pairs x)
  (if (or
       (= 0 (length x))
       (= 1 (length x)))
      '()
      (cons (list (car x) (cadr x)) (pairs (cdr x)))
      )
  )

;;(sum lst)
;;Suma todos los elementos de la lista lst, usando la recursión de cola simple.
;;Retorna la suma de todos los elementos de lst.
(define (sum lst)
  (if (empty? lst)
      0
      (+ (car lst) (sum (cdr lst)))
      )
  )

;;(lolsum listadelistas)
;;Recibe una lista de listas y aplica función map, sobre cada lista interna, con funcion de suma como parámetro.
;;Retorna una lista de sumas de las listas internas de la lista original.
(define (lolsum listadelistas)
  (map (lambda (listadelistas) (sum listadelistas)) listadelistas)
  )


(define (cima lista)
  (cond
    ((= 1 (length lista)) (car lista))
    ((= 0 (length lista)) (error "Lista vacia!"))
    (else (cima (lolsum (pairs lista))))
    )
  )

