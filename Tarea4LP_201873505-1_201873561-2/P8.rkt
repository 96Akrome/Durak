#lang scheme

(define (pairs x)
  (if (or (= 0 (length x))(= 1 (length x)))
      '()
      (cons (list (car x)(cadr x)) (pairs (cdr x)))))


;;  (map (lambda (i j) (list i j)) x  x)))

(define (sum lst)
  (if (empty? lst)
      0
      (+ (car lst) (sum (cdr lst)))
      )
  )

(define (lolsum listadelistas)
  (map (lambda (listadelistas) (sum listadelistas)) listadelistas)
  )

(define (cima lista)
  writeln "Lol"
  )

