(ns kata.sum-of-cubes)

(defn- pow [x y] (reduce * (repeat y x)))

(defn- cube-sum [n]
  (->>
    (range 1 (+ n 1))
    (map #(pow % 3))
    (reduce +)))

(defn- find-nb-down [m n]
  (loop [n n]
    (let [cs (cube-sum n)]
      (cond
        (= m cs) n
        (< m cs) (recur (- n 1))
        :else -1))))

(defn find-nb [m]
  (loop [n 1]
    (let [cs (cube-sum n)]
      (cond
        (= m cs) n
        (> m cs) (recur (* n 2))
        :else (trampoline find-nb-down m n)))))
