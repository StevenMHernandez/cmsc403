#lang racket

(define combineLists (lambda (A B)
                       (if (null? B) A
                           (combineLists (cons (car B) A) (cdr B))
                           )
                       )
  )

(define listContains (lambda (L x)
                       (if (null? L) #f
                           (if (equal? x (car L)) #t
                               (listContains (cdr L) x)
                               )
                           )
                       )
  )

(define removeDuplicates (lambda (L ListSoFar)
                           (if (null? L) ListSoFar
                               (if (listContains ListSoFar (car L))
                                   (removeDuplicates (cdr L) ListSoFar)
                                   (removeDuplicates (cdr L) (cons (car L) ListSoFar))
                                   )
                               )
                           )
  )

(define unionUnique (lambda (A B) (removeDuplicates (combineLists A B) '())))

; could have been as simple as (remove-duplicates (append A B)), both functions being built-in to racket.
  

(unionUnique '(2 3 1 2 3 3 4) '(3 2 3 5 3)) ; should only contain (1 2 3 4 5)

(unionUnique '(1 1 1 1 1) '(0 0 0 0 2 0)) ; should only contain(0 1 2)

(unionUnique '() '(3 2 1)) ; should only contain (1 2 3)

(unionUnique '() '()) ; should be '()

(unionUnique '(null) '()) ; should only contain(null)

(unionUnique (list '(1 2 3)) (list "d" '(1 2 2) '(1 2 3))) ; should only contain("d" '(1 2 2) '(1 2 3))
