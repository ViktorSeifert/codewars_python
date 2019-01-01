(ns kata.egypt)

; https://www.codewars.com/kata/54f8693ea58bce689100065f/train/clojure

(defn- decompose-impl [n denom decomp]
  (if (zero? n)
    (filter pos? decomp)
    (let [fraction (/ denom)]
      ; (<= fraction n) should work, but it seems slower that what is below
      (if (not (neg? (- n fraction)))
        (recur (- n fraction) (inc denom) (conj decomp fraction))
        (recur n (inc denom) decomp)))))

(defn decompose [r]
  (let [r (read-string r)
        whole-part (int r)]
    (if (zero? r)
      [] 
      (->> (decompose-impl (- r whole-part) 2 [whole-part]) (map str)))))