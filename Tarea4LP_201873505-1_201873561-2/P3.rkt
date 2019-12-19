#lang scheme

(define (pvp x y a)
  (cond
    ((eqv? a "A")(and x y))
    ((eqv? a "O")(or x y))
    ((eqv? a "X")(xor-fn x y))
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
  (let loop ((attack (car lista)) (l1 (cadr lista))(l2 (caddr lista))(paridad 0)(n1 0)(n2 0))
   (cond
     ((even? paridad)(
                     (begin
                       (cond
                          ((pvp ((car l1) (car l2) attack))(+ n1 1))
                          (+ n1 0))
                         )
                     ))
     
     (not (even? paridad)(
                          cond(
                               ((pvp l1 l2 attack)(+ n2 1))
                               (+ n2 0))
                              )
          )
     )
    (loop max-fn(n1 n2)(+ paridad 1)(l1 (cdr l1))(l2 (cdr l2))))
  )
