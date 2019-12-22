#lang scheme

;;(error orden Matriz).
;;Revisa los casos en que la matriz y el orden ingresados genere algun error.
;;Retorna #t si se detecto algun error, #f si no.
(define (error orden Matriz)
  (if (eqv? (length Matriz) 0)
      #t
      (if (eqv? (length Matriz) orden)
          (let iter ((matriz Matriz) (num 1))
            (if (eqv? num orden)
                (if (eqv? (length (car matriz)) orden)
                    #f
                    #t)
                (if (eqv? (length (car matriz)) orden)
                    (iter (cdr matriz) (+ num 1))
                    #t)))
          #t)))
             
;;(fila n matriz).
;;Revisa todas las filas de una matriz para ver si en alguna de ellas esta ordenada de menor a mayor.
;;Retorna #t si alguna fila esta ordenada de menor a mayor, #f si no.
(define (fila n matriz)
      (let tope ((i 0) (j 0) (fila (car matriz)) (matrix matriz))
        (if (eqv? i (- n 1))
            #t
            (if (< (car fila) (car (cdr fila)))
                (tope (+ i 1) j (cdr fila) matrix)
                (if (eqv? j (- n 1))
                    #f
                    (tope 0 (+ j 1) (car (cdr matrix)) (cdr matrix)))))))
               
;;(transponer matriz).
;;Toma la matriz ingresada y la transpone cambiando filas por columnas.
;;Retorna la matriz transpuesta de la matriz ingresada.
(define (transponer matriz)
  (let iter ((matriz matriz) (result '()))
    (if (null? (car matriz))
        result
        (iter (map cdr matriz) (append result (list (map car matriz)))))))

;;(numeroIndice indice matriz).
;;Recorre los numeros en la diagonal de la matriz eliminando n filas y columnas para acceder a estos, donde n = indice. 
;;Retorna el numero alojado en la casilla [indice][indice] de la matriz ingresada, con indice >= 1.
(define (numeroIndice indice matriz)
  (let reducir ((i 1) (matrix matriz))
    (if (< i indice)
        (reducir (+ i 1) (transponer (cdr (transponer (cdr matrix)))))
        (car (car matrix)))))

;;(diagonal n matriz).
;;Revisa los numeros de la diagonal de la matriz para ver si estan ordenados de menor a mayor (de izquierda a derecha y de arriba hacia abajo segun el enunciado). 
;;Retorna #t si la diagonal esta ordenada de menor a mayor, #f si no.
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
  (if (error n matriz)
      "La matriz ingresada no es válida"
      (cond ((fila n matriz) #t)
            ((fila n (transponer matriz)) #t)
            ((diagonal n matriz) #t)
            (else   #f))))


