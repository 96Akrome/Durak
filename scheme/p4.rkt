#lang scheme

;; Permite acceder al elemento en la posicion n de la lista
(define (list-ref lst n)
 (if (<= n 0)
     (car lst)
     (list-ref (cdr lst) (- n 1))))

;; Revisa las filas
(define (fila n matriz)
         
      (let tope ((i 0) (j 0) (fila (car matriz)) (matrix matriz))
        (if (eqv? i (- n 1))
            #t
            (if (< (car fila) (car (cdr fila)))
                (tope (+ i 1) j (cdr fila) matrix)
                (if (eqv? j (- n 1))
                    #f
                    (tope 0 (+ j 1) (car (cdr matrix)) (cdr matrix)))))))

;; es de cola
(define (transponer matriz)
  (let iter ((matriz matriz) (result '()))
    (if (null? (car matriz))
        result
        (iter (map cdr matriz) (append result (list (map car matriz)))))))

;; Obtiene el numero alojado en el indice ii de la matriz
(define (numeroIndice indice matriz)
  (let reducir ((i 1) (matrix matriz))
    (if (< i indice)
        (reducir (+ i 1) (transponer (cdr (transponer (cdr matrix)))))
        (car (car matrix)))))

;; revisa la diagonal desde arriba hacia abajo y de izq a derecha
(define (diagonal n matriz)
  (let tope ((i 2) (num1 (car (car matriz))) (num2 (car (cdr (car (cdr matriz)))) ) )
    (if (eqv? i n)
        (if (< num1 num2)
            #t
            #f)
        (if (< num1 num2)
                (tope (+ i 1) num2 (numeroIndice (+ i 1) matriz) )
                #f))))



(define (orden n matriz)
  (cond ((fila n matriz) #t)
        ((fila n (transponer matriz)) #t)
        ((diagonal n matriz) #t)
        (else   #f)))



"
(orden 3 '( (1 4  3)
            (2 2 12)
            (1 5 15) ) )
#t
(orden 3 '( (3 9 8)
            (6 5 4)
            (2 1 7) ) )
#t


"