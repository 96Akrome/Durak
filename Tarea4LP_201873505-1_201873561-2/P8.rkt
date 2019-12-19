#lang scheme
;;(pairs x)
;;Recibe una lista, denotada como x, y agrupa el elemento i y i+1 en una lista interna.
;;Retorna lista de pares de numeros consecutivos. Ej: (1 2 3 4)-> (1 2)(2 3)(3 4).
(define (pairs x)
  (if (or (= 0 (length x))(= 1 (length x)))
      '()
      (cons (list (car x)(cadr x)) (pairs (cdr x)))))

;; (empty)
;; Define empty como la lista vacia '()
;; Retorna la lista vacia
(define empty '())

;;(sum lst)
;; Suma todos los elementos de la lista lst, usando la recursion de cola simple.
;;Retorna la suma de todos los elementos de lst.
(define (sum lst)
  (if (empty? lst)
      0
      (+ (car lst) (sum (cdr lst)))
      )
  )

;;(lolsum listadelistas)
;;Recibe una lista de listas y aplica funcion map, sobre cada lista interna, con funcion de suma como parametro.
;;Retorna una lista de sumas de las listas internas de la lista original.
(define (lolsum listadelistas)
  (map (lambda (listadelistas) (sum listadelistas)) listadelistas)
  )


(define (cima lista)
  (if (= 1 (length lista))
      (car lista)
      (cima (lolsum (pairs lista))))
  )

