#lang scheme

"
-Idea: sea k = 5, lista = (1 2 3 4 5 6 7)
revisar el primer elemento: 1
conseguir el numero de interes: 5 - 1 = 4
revisar si el numero de interes esta en la lista: 4 en posicion 3
agregar par (1 4)
remover elementos 1 y 4 de la lista
repetir
"

;; Devuelve la lista equivalente a list eliminando toda ocurrencia de W y X
(define remv
  (lambda (W X list)
    (cond
      (( null? list) '() )
      (( eqv? W ( car list)) ( remv W X ( cdr list)))
      (( eqv? X ( car list)) ( remv W X ( cdr list)))
      (else ( cons (car list) ( remv W X ( cdr list)) )))))

;; Revisa si x existe en la lista list
(define (member? x ls)
     (cond ((null? ls) #f)
           ((equal? x (car ls)) #t)
           (else   (member? x (cdr ls)))))

;; Entrega la lista con las tuplas de numero que al ser sumados dan el numero k ingresado
(define (aux k lista)
  (if (empty? lista)
      '()
      (let iterar ((num (car lista)) (lis (cdr lista)) (tupla '()))
        (if (empty? lis)
            tupla
            (if (member? (- k num) lis)
                (if (empty? (remv num (- k num) lis))
                    (append tupla (list (list num (- k num))))
                    (iterar (car (remv num (- k num) lis)) (cdr (remv num (- k num) lis)) (append tupla (list (list num (- k num)))))
                    )
                (iterar (car lis) (cdr lis) tupla))))))

(define (armar k lista)
  (if (empty? (aux k lista))
      #f
      (aux k lista)))



"
(armar 12 '(1 2 3 8 23 8 14 4 9))
((8 4) (3 9))

"