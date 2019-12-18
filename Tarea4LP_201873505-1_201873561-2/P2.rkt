#lang scheme

(define empty '())


(define (sum lst)
  (if (empty? lst)
      0
      (+ (car lst) (sum (cdr lst)))
      )
  )

(define (min-fn a b) (if (< a b) a b))
(define (max-fn a b) (if (> a b) a b))


(define (maxmin lst)
  (let loop ( (x -inf.0) (y +inf.0)  (lst (map (lambda (lst)(list (car lst) (sum (cdr lst)))) lst)))
    (if (empty? lst)
        (list x y)
        (loop (max-fn (cadar lst) x) (min-fn (cadar lst) y) (cdr lst))))
  )
