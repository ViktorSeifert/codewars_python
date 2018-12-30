(ns kata.piglatin-test
  (:require [clojure.test :refer :all]
            [kata.piglatin :refer :all]))

(deftest pig-latin-example-test1
  (is (= (pig-it "Pig latin is cool") "igPay atinlay siay oolcay")))
  
(deftest pig-latin-example-test2
  (is (= (pig-it "This is my string") "hisTay siay ymay tringsay")))
