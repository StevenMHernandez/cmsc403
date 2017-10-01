#lang racket

(define leapYears (lambda (start end ListSoFar)
                    (let ([nextDate (+ start (modulo (- 4 (modulo start 4)) 4))])
                      ;nextDate
                      ; if ((y%100) != 0 || (y%400) == 0)
                      (if (or (not (= (modulo nextDate 100) 0)) (= (modulo nextDate 400) 0))
                              
                          (if (> nextDate end) ListSoFar
                              (leapYears (+ 1 nextDate) end (cons nextDate ListSoFar))
                              )
                          (leapYears (+ 1 nextDate) end ListSoFar) 
                          )
                      )
                        
                    )
  )


; should all be the same
(leapYears 1776 2017 '())
(leapYears 1775 2017 '())
(leapYears 1775 2016 '())

; should all be the same length
(length (leapYears 1776 2017 '()))
(length (leapYears 1775 2017 '()))
(length (leapYears 1775 2016 '()))
