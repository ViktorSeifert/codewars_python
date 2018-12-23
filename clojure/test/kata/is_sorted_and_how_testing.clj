(ns kata.is-sorted-and-how-testing
  (require [clojure.test :refer :all])
  (use [kata.is-sorted-and-how :rename {sorted-and-how? solution}]))

(deftest sample-tests
  (are [inp exp] (= exp (solution inp))
       [1 2] "yes, ascending"
       [15 7 3 -8] "yes, descending"
       [4 2 30] "no"
       [9 9 41 65 75 78 129 184 195] "no"))
