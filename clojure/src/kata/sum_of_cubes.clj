(ns kata.sum-of-cubes)

(defn- pow [x y] (reduce * (repeat y x)))

(defn- naturals [] (iterate inc 1))

(defn- cube-sum [n]
  (->>
    (range 1 (+ n 1))
    (map #(pow % 3))
    (reduce +)))

(defn find-nb [m]
  (let [cubes (for [n (naturals) :let [cs (cube-sum n)] :while (<= cs m)] [n cs])
        last-cube (last cubes)]
      (if (= m (second last-cube)) (first last-cube) -1)))
    