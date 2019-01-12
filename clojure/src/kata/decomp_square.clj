(ns kata.decomp-square)

; https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/clojure

(defn- n-bits [n]
  (->
    (bit-shift-left 1 n)
    (- 1)))

(defn- sub-select [selection numbers]
  (keep-indexed #(if (bit-test selection %1) %2) numbers))

(defn- valid? [decomposition]
  (and (not (nil? decomposition)) (= decomposition (distinct decomposition))))

(defn- decompose-impl [n r]
  (let [r2 (* r r) remaining (- n r2)]
    (cond
      (= r 0) nil
      ; Prevent [1 1] entering the result
      (= remaining 2) nil
      (= remaining 0) [r]
      (< remaining 0) nil
      :else
        (let [decomp-rem (decompose-impl remaining (int (Math/sqrt remaining)))]
          (if
            (valid? decomp-rem) (cons r decomp-rem) (decompose-impl n (- r 1)))))))

(defn decompose [n]
  (let [result (decompose-impl (* n n) (- n 1))]
    (if (valid? result) (sort result) nil)))