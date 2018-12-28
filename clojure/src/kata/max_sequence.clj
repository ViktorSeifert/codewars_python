(ns kata.max-sequence)

; https://www.codewars.com/kata/53db96041f1a7d32dc0004d2

(defn max-sequence [xs]
  (let [xs (vec xs) length-of-xs (count xs)]
    (if (every? #(< % 0) xs)
      0
      (->>
        (for [start (range 0 length-of-xs)
              end (range (inc start) (inc length-of-xs))]
          (subvec xs start end))
        (map #(reduce + %))
        (reduce max)))))