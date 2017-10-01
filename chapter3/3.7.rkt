#lang racket

(define getSquareRootsR (lambda (L ListSoFar)
                          (if (null? L) ListSoFar
                              (if (> 0 (car L))
                                  (getSquareRootsR (cdr L) ListSoFar)
                                  (getSquareRootsR (cdr L) (cons (sqrt (car L)) ListSoFar))
                                  )
                              )
                          )
  )

(define getSquareRoots (lambda (L)
                         ; if we don't reverse we would have a backwards list
                         (reverse (getSquareRootsR L '())) 
                         )
  )

(getSquareRoots '(-99 9 4 0 -1 1 12)) ; should return '(3 2 0 1 sqrt(12))