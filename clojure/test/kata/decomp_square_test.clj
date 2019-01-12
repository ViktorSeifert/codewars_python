(ns kata.decomp-square-test
  (:require [clojure.test :refer :all]
            [kata.decomp-square :refer :all]))

(deftest a-test1
  (testing "Test 1"
    (is (= (decompose 463) [5 30 462]))))
(deftest a-test2
  (testing "Test 2"
    (is (= (decompose 50) [1,3,5,8,49]))))
(deftest a-test3
  (testing "Test 3"
    (is (= (decompose 2) nil))))
(deftest a-test3
  (testing "Test 4"
    (is (= (decompose 9927447) [1 3 17 87 4455 9927446]))))
    