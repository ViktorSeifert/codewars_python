(ns kata.decomp-square)

; https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/clojure

(defn- n-bits [n]
  (->
    (bit-shift-left 1 n)
    (- 1)))

(defn decompose [n]
  ())