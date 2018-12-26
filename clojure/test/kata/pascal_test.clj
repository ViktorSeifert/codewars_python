(ns kata.pascal-test
  (:require 
    [clojure.test :refer :all]
    [kata.pascal :refer :all]))

(deftest
  triangles
  (testing "Testing triangles"
    (is (= (pascal 1) [[1]]))
    (is (= (pascal 4) [[1][1 1][1 2 1][1 3 3 1]]))))