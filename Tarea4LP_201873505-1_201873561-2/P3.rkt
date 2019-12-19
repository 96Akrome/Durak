#lang scheme

(define (pvp x y a)
  (cond
    ((eqv? a 'A)(and x y))
    ((eqv? a 'O)(or x y))
    ((eqv? a 'X)(xor-fn x y))
    (else (error "Operador logico invalido! Se aceptan solo A,O,X"))
    )
  )

(define (xor-fn a b)
  (not (equal? a b))
  )


(define (max-fn a b)
  (cond
    ((> a b) 1 2)
    (else #f))
  )


(define (vs lista)
  (let loop ((resultado 0)(attack (car lista)) (l1 (cadr lista))(l2 (caddr lista))(paridad 0)(n1 0)(n2 0))
   (cond
     ((and (even? paridad) (pvp (car l1) (car l2) attack) (+ n1 1)) writeln "estoy en par")
     ((and (not(even? paridad))(pvp (car l1) (car l2) attack) (+ n2 1)) writeln "estoy en impar"))
    (loop (max-fn n1 n2) attack (cdr l1) (cdr l2) (+ paridad 1) n1 n2)
    )
  )
