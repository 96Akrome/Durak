#lang scheme

;;  (map (lambda (i j) (list i j)) x  x)))

(define (pvp x y)
  (map (lambda (i j) (list i j)) x y)
  )


(define (vs lista)
  (let loop ((attack (car lista)) (l1 (cadr lista))(l2 (caddr lista)))
    writeln "lol"
    )
  )
