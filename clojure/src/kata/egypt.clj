(ns kata.egypt)

; https://www.codewars.com/kata/54f8693ea58bce689100065f/train/clojure

(defn- decompose-impl [n decomp]
  (if (zero? n)
    (filter pos? decomp)
    (let [next-fraction (->> n (/) (Math/ceil) bigint (/))]
      (recur (- n next-fraction) (conj decomp next-fraction)))))

(defn decompose [r]
  (let [r (rationalize (read-string r))
        whole-part (int r)]
    (if (zero? r)
      [] 
      (->> (decompose-impl (- r whole-part) [whole-part]) (map str)))))