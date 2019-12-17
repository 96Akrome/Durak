#lang scheme

;;(right tree)
;;Aplica car(cdr(cdr(tree))) al arbol pasado.
;;Retorna el valor de car(cdr(cdr(tree))), es decir, subarbol derecho.
(define (right tree)
  (caddr (tree))
  )

;;(left tree)
;;Aplica car(cdr(tree)) al arbol pasado.
;;Retorna el valor de car(cdr(tree)), es decir, subarbol izquierdo.
(define (left tree)
  (cadr (tree))
  )


(define empty '() )


(define (gemelos arbol1 arbol2)
  (cond
    ((and (empty? arbol1) (empty? arbol2) ) #t)
    ((or (empty? arbol1) (empty? arbol2)) #f)
    (else
     (and (gemelos (right arbol1) (right arbol2)) (gemelos (left arbol1) (left arbol2))))
    )
  )

      
