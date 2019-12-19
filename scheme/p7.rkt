#lang scheme

;;(abs n)
;;Revisa si el número n ingresado es positivo o no.
;;Retorna el valor absoluto del número n ingresado.
(define (abs n)
  (if (> n 0)
      n
      (* n -1)))

(define (fpi funcion umbral i)
  (let iterar ((num i) (iteraciones 0))
    (if (<= (abs (- (funcion num) num)) umbral)
        iteraciones
        (iterar (funcion num) (+ iteraciones 1)))))

"
(fpi (lambda (x) (cos x)) 0.02 1)
8
"