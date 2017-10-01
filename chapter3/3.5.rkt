#lang racket
(define performOnAllR (lambda (myFunc L total)
                        (if (null? L) total
                            (performOnAllR myFunc (cdr L) (myFunc total (car L)))
                            )))

(define performOnAll (lambda (myFunc L)
                       (if (null? L) 0
                           (if (null? (cdr L)) (car L)
                               (performOnAllR myFunc (cdr (cdr L)) (myFunc (car L) (car (cdr L))))
                               )
                           )
                       )
  )

(performOnAll + '(1 2 3 3)) ; 9
(performOnAll * '(1 2 3 3)) ; 18
(performOnAll + '(1 2 3 0)) ; 6
(performOnAll * '(1 2 3 0)) ; 0
(performOnAll - '(18 1 2 3 3)) ; 9
(performOnAll / '(64 2 2 2)) ; 8