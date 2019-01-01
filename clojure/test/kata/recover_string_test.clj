(ns kata.recover-string-test
  (:require [clojure.test :refer :all]
            [kata.recover-string :refer (recover-secret)]))

(deftest solve
  (is (= (recover-secret ["tup" "whi" "tsu" "ats" "hap" "tis" "whs"]) "whatisup")))
