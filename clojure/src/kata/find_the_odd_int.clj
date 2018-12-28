(ns kata.find-the-odd-int)

(defn find-odd [xs]
  (->> 
    (group-by 
      (fn [x] (count (filter (fn [y] (= x y)) xs))) 
      xs)
    (filter #(odd? (first %)))
    (first)
    (second)
    (first)))