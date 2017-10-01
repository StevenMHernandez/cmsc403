#lang racket

(define sizeOf(lambda (L total)
                (if (null? L) total
                    (sizeOf (cdr L) (+ 1 total))
                    )
                )
  )

(define sum(lambda (L total)
                (if (null? L) total
                    (sum (cdr L) (+ (car L) total))
                    )
                )
  )

(define average (lambda (L)
                  (/ (sum L 0) (sizeOf L 0))
                  )
  )

(average '(1 5 9)) ; 5

(average '(1 5 8)) ; 14/3