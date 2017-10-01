#lang racket
(define runForEach (lambda (myFunc L)
               (if (null? L)
                   '()
                   (if (null? (cdr L))
                       (car L)
                       (runForEach myFunc (cons
                                     (myFunc (car L) (car (cdr L)))
                                     (cdr (cdr L))
                                     ))
                       )
                   )
               ))

(runForEach + '(1 2 3 3)) ; 9

(runForEach + '(3 5 7 9)) ; 24