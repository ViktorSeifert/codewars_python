(ns kata.band-name-generator-test
    (:require [clojure.test :refer [deftest is are testing]]
              [kata.band-name-generator :refer [generate-band-name]]))
              
  (deftest sample
    (testing "sample-tests"
      (are [input expected] (= (generate-band-name input) expected)
        "knife" "The Knife"
        "tart" "Tartart"
        "sandles" "Sandlesandles"
        "bed" "The Bed")))
  