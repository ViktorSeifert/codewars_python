(ns kata.is-sorted-and-how)

(defn sorted-and-how? [sq]
  (let [lt-or-gt
    (->>
      sq
      (partition 2 1)
      (map #(cond
              (< (first %) (second %)) :lt
              (> (first %) (second %)) :gt
              ; Special treatment of eq
              ; because the kata tests
              ; see [9 9 10] as not being sorted.
              :else :eq)))]
    (cond
      (every? #(= :lt %) lt-or-gt) "yes, ascending"
      (every? #(= :gt %) lt-or-gt) "yes, descending"
      :else "no")))
