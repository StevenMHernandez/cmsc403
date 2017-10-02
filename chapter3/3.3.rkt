#lang racket

(define increase-salary (lambda (percentage Salaries SalariesSoFar)
                          (if (null? Salaries)
                              SalariesSoFar
                              (increase-salary percentage (cdr Salaries)
                                               (append SalariesSoFar
                                                       (list (* (+ 1 percentage) (car Salaries))))
                                               )
                              )
                          )
  )

(increase-salary 0.03 '(100 200 1000) '()) ; '(103 206 1030)
