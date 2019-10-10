(ns kata.longest-common-subsequence-test
    (:require 
      [clojure.test :refer :all]
      [kata.longest-common-subsequence :refer :all]))
      
  (deftest sample-tests
    (are [expected result] (= expected result)
      "" (lcs "" "")
      "" (lcs "abc" "")
      "" (lcs "" "abc")
      "" (lcs "a" "b")
      "a" (lcs "a" "a")
      "ac" (lcs "abc" "ac")
      "abc" (lcs "abcdef" "abc")
      "acf" (lcs "abcdef" "acf")
      "nottest" (lcs "anothertest" "notatest")
      "12356" (lcs "132535365" "123456789")
      "final" (lcs "nothardlythefinaltest" "zzzfinallyzzz")
      "acdefghijklmnoq" (lcs "abcdefghijklmnopq" "apcdefghijklmnobq")))