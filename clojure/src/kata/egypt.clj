(ns kata.egypt)

; https://www.codewars.com/kata/54f8693ea58bce689100065f/train/clojure

(defn- decompose-impl [n denom decomp]
  (if (= n (reduce + decomp))
    (filter pos? decomp)
    (let [expanded-decomp (conj decomp (/ 1 denom))
          current-sum (reduce + expanded-decomp)]
      (if (<= current-sum n)
        (recur n (inc denom) expanded-decomp)
        (recur n (inc denom) decomp)))))

(defn decompose [r]
  (let [r (read-string r)
        whole-part (int r)]
    (if (zero? r)
      [] 
      (->> (decompose-impl r 2 [whole-part]) (map str)))))