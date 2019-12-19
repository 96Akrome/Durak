#lang scheme

(define (pvp x y a)
  (cond
    ((eqv? a 'A)(and x y))
    ((eqv? a 'O)(or x y))
    ((eqv? a 'X)(xor-fn x y))
    (else (error "Operador logico invalido! Se aceptan solo A,O,X"))
    )
  )

(define (xor-fn x y)
  (if (boolean=? x y) 0 1)
  )


(define (max-fn a b)
  (cond
    ((> a b) 1 2)
    (else #f))
  )

(define (comparar paridad l1 l2 attack)
  (cond
   ((eqv? 0 (pvp (car l1) (car l2) attack)) (list 0 0))
   ((and (even? paridad) (pvp (car l1)(car l2) attack)) (list 1 0))
   ((and (not (even? paridad)) (pvp (car l1) (car l2) attack)) (list 0 1)))
  )
  

(define (vs lista)
  (let loop ((attack (car lista)) (l1 (cadr lista))(l2 (caddr lista))(paridad 0)(n1 0)(n2 0))
    (if (and (empty? l1)(empty? l2)) (max-fn n1 n2)
        (begin 
         (+ n1 (car (comparar paridad l1 l2 attack)))
         (+ n2 (cadr (comparar paridad l1 l2 attack)))) 
        )
    (loop attack (cdr l1) (cdr l2) (+ paridad 1) n1 n2)))



  ;; (cond
    ;; ((and (even? paridad)(pvp (car l1) (car l2) attack) (+ n1 1)) writeln "estoy en par")
     ;;((and (not(even? paridad))(pvp (car l1) (car l2) attack) (+ n2 1)) writeln "estoy en impar"))
    ;;(loop attack (cdr l1) (cdr l2) (+ paridad 1) n1 n2)))
