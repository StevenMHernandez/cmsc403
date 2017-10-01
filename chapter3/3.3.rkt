#lang racket
(define increase-salary-r (lambda (percentage Salaries SalariesSoFar)
                            (if (null? Salaries)
                                SalariesSoFar
                                (increase-salary-r percentage (cdr Salaries) (cons
                                                                              (* (+ 1 percentage)
                                                                                 (car Salaries)
                                                                                 )
                                                                              SalariesSoFar)
                                                   ))
                            )
  )

(define increase-salary (lambda (percentage Salaries)
                          (increase-salary-r percentage Salaries '())
                          ))

(increase-salary 0.03 '(100 200 1000)) ; '(103 206 1030)