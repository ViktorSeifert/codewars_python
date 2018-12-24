(ns kata.two-to-one-test
    (:require [clojure.test :refer :all]
              [kata.two-to-one :refer :all]))
  (require '[clojure.string :as str])

  (deftest sample
    (testing "sample-tests"
      (are [input1 input2 expected] (= (longest input1 input2) expected)
        "aretheyhere" "yestheyarehere" , "aehrsty"
        "loopingisfunbutdangerous" "lessdangerousthancoding" , "abcdefghilnoprstu"
        "inmanylanguages" "theresapairoffunctions" , "acefghilmnoprstuy"
        )))