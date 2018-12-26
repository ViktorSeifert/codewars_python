; https://www.codewars.com/kata/pascals-triangle-number-2/train/clojure
(ns kata.pascal)

(defn- next-pasal-step [previous-step]
  (concat
    [1]
    (map 
      #(reduce + %)
      (partition 2 1 previous-step))
    [1]))

(defn pascal 
  ([n] (pascal n []))
  ([n acc]
    (if (= n 0) 
      acc
      (let [steps-so-far (count acc)]
        (condp = steps-so-far
          0 (recur (dec n) [[1N]])
          1 (recur (dec n) (conj acc [1N 1N]))
          (recur (dec n) (conj acc (next-pasal-step (last acc)))))))))