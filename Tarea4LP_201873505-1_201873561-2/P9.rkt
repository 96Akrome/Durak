#lang scheme

;;(cumplen funcion lista)
;;Fitra la lista original, usando la funcion filter y de la funcion pasada.
;;Retorna la lista de elementos tales que, al aplicar la función, retornan #t.
(define (cumplen funcion lista)
  (filter funcion lista)
  )

;;(no_cumplen funcion lista)
;;Fitra la lista original, usando la funcion filter y la negación de la función original.
;;Retorna la lista de elementos tales que, al aplicar la función, retornan #f.
(define (no_cumplen funcion lista)
  (filter (negate funcion) lista)
  )

(define (segm funcion lista)
  (append (cumplen funcion lista) (no_cumplen funcion lista))
  )
  


