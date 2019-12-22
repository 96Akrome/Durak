#lang scheme

;;(remv W X list).
;;Busca los numeros W y X en la lista list para remover todas las apariciones de estos en dicha lista.
;;Retorna la lista equivalente a list eliminando toda ocurrencia de W y X en esta.
(define remv
  (lambda (W X list)
    (cond
      (( null? list) '() )
      (( eqv? W ( car list)) ( remv W X ( cdr list)))
      (( eqv? X ( car list)) ( remv W X ( cdr list)))
      (else ( cons (car list) ( remv W X ( cdr list)) )))))

;;(member? x lista).
;;Revisa si x existe en la lista ls
;;Retorna #t si x existe en la lista, #f si no.
(define (member? x lista)
     (cond ((null? lista) #f)
           ((equal? x (car lista)) #t)
           (else   (member? x (cdr lista)))))


;;(aux k lista).
;;Revisa si en la lista ingresada hay números que al sumarlos den como resultado el número ingresado k para luego imprimir una lista de tuplas con los pares encontrados
;;Retorna la lista con las tuplas de números que al ser sumados dan el numero k ingresado.
(define (aux k lista)
  (if (empty? lista)
      '()
      (let iterar ((num (car lista)) (lis (cdr lista)) (tupla '()))
        (if (empty? lis)
            tupla
            (if (member? (- k num) lis)
                (if (empty? (remv num (- k num) lis))
                    (append tupla (list (list num (- k num))))
                    (iterar (car (remv num (- k num) lis)) (cdr (remv num (- k num) lis)) (append tupla (list (list num (- k num))))))
                (iterar (car lis) (cdr lis) tupla))))))

(define (armar k lista)
  (if (empty? (aux k lista))
      #f
      (aux k lista)))