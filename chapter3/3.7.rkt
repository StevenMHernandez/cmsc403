#lang racket

(define getSquareRoots (lambda (L ListSoFar)
                          (if (null? L) ListSoFar
                              (if (> 0 (car L))
                                  (getSquareRoots (cdr L) ListSoFar)
                                  (getSquareRoots (cdr L) (append ListSoFar (list (sqrt (car L)))))
                                  )
                              )
                          )
  )

(getSquareRoots '(-99 9 4 0 -1 1 12) '()) ; should return '(3 2 0 1 sqrt(12))
