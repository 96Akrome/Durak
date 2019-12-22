#lang scheme

;;(sum lst)
;;Suma todos los elementos de la lista lst, usando la recursión de cola simple.
;;Retorna la suma de todos los elementos de lst.
(define (sum lst)
  (if (empty? lst)
      0
      (+ (car lst) (sum (cdr lst)))
      )
  )

;;(min-fn a b)
;;Compara la cola y de la lista a = (x y) con el valor numérico b.
;;Retorna la cabeza x de la lista a = (x y), en caso de que y es menor a b. En caso contrario, retorna b.
(define (min-fn a b)
  (if (< (cadr a) b)
      (car a) b)
  )

;;(max-fn a b)
;;Compara la cola y de la lista a = (x y) con el valor numérico b.
;;Retorna la cabeza  x de la lista a = (x y), en caso de que y es mayor a b. En caso contrario, retorna b.
(define (max-fn a b)
  (if (> (cadr a) b)
      (car a) b)
  )

(define (maymecola listadelistas)
  (if (empty? listadelistas) (error "Lista de listas ingresada está vacía!")
      (let loop (
                 (x -inf.0)
                 (y +inf.0)
                 (l (map (lambda (listadelistas) (list (car listadelistas) (sum (cdr listadelistas)))) listadelistas))
                 )
        (if (empty? l)
            (list x y)
            (loop (max-fn (car l) x) (min-fn (car l) y) (cdr l))))
      )
  )
