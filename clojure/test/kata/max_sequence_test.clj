(ns kata.max-sequence-test
  (:require [clojure.test :refer :all]
            [kata.max-sequence :refer :all]))

(deftest simple
  (are [actual expected] (= actual expected)
    (max-sequence [-2, 1, -3, 4, -1, 2, 1, -5, 4]) 6
    (max-sequence [-2 -3 -1]) 0
    (max-sequence [1 2 3]) 6))
