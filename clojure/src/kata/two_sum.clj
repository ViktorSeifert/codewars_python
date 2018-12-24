(ns kata.two-sum)

(defn- all-index-combos [vector-length]
  (for [x (range vector-length) y (range vector-length) :when (not= x y)] [x y]))

(defn twosum [numbers target]
  (let [index-tuples (all-index-combos (count numbers))]
    (->>
      (for [[i j] index-tuples :when (= target (+ (get numbers i) (get numbers j)))] [i j])
      (first))))