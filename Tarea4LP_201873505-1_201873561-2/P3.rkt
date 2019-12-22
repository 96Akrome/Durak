#lang scheme

;;(pvp x y a)
;;Recibe dos numeros binarios y un tipo de ataque. Segun el ultimo se aplica la operacion binaria a los dos numeros recibidos.
;;Retorna el valor de retorno de la operacion binaria. 1 si es Verdadero y 0 si es Falso. En caso de ataque incorrecto, se desplega un error.
(define (pvp x y a)
  (cond
    ((eqv? a 'A)(and x y))
    ((eqv? a 'O)(or x y))
    ((eqv? a 'X)(xor-fn x y))
    (else (error "Operador logico invalido! Se aceptan solo A,O,X"))
    )
  )

;;(xor-fn x y)
;;Aplica la definicion de operacion logica xor a dos numeros binarios.
;;Retorna 1 si el xor da como resultado Verdadero, en otro caso retorna 0.
(define (xor-fn x y)
  (if ((negate eqv?)x y) 1 0)
  )


;;(max-fn a b)
;;Recibe dos parametros numericos, y decide de los dos es mayor o si se produjo el empate.
;;Si a > b, se retorna 1, y b > a, 2. En caso de empate, #f.
(define (max-fn a b)
  (cond
    ((> a b) 1)
    ((> b a) 2)
    (else #f))
  )

;;(comparar paridad l1 l2 attack)
;;Recibe el numero-contador paridad, dos listas y el tipo de ataque.
;;Retorna la lista (1 0) si la primera lista gano y la paridad era par, (0 1) si la segunda y paridad era impar. En otro caso se retorna (0 0).
(define (comparar paridad l1 l2 attack)
  (cond
   ((eqv? 0 (pvp (car l1) (car l2) attack))
    (list 0 0))
   ((and (even? paridad) (pvp (car l1)(car l2) attack))
    (list 1 0))
   ((and (not (even? paridad)) (pvp (car l1) (car l2) attack))
    (list 0 1)))
  )
  

(define (vs lista)
  (if (or (empty? lista)(empty? (cadr lista))(empty? (caddr lista))(not (eqv? (length (cadr lista)) (length (caddr lista)))))
      (error "Datos ingresados inválidos! Alguna de las listas no cumple las condiciones de largo o este vacia.")
      (let loop ((attack (car lista)) (l1 (cadr lista))(l2 (caddr lista))(paridad 1)(n1 0)(n2 0))
        (if (empty? l1)
            (max-fn n1 n2)
            (let ( (n1 (+ n1 (car (comparar paridad l1 l2 attack)))) (n2 (+ n2 (cadr (comparar paridad l1 l2 attack)))))
              (loop attack (cdr l1) (cdr l2) (+ paridad 1) n1 n2))
            )
        )
      )
  )


