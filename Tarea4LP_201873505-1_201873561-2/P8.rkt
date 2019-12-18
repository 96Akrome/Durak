#lang scheme

(define (pairs x)
  (if (or (= 0 (length x))(= 1 (length x)))
      '()
      (cons (list (car x)(cadr x)) (pairs (cdr x)))))





;;  (map (lambda (i j) (list i j)) x  x)))




