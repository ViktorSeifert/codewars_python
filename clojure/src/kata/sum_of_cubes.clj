(ns kata.sum-of-cubes)

(defn- pow [x y] (reduce * (repeat y x)))

(defn- cube-sum [n]
  (try
    (->>
      (range 1 (+ n 1))
      (map #(pow % 3))
      (reduce +))
    (catch ArithmeticException ex -1)))

(defn- find-nb-impl [m initial-step]
  (loop [n 1 step initial-step]
    (let [cs (cube-sum n)]
      (cond
        (< step 1) -1
        (= m cs) n
        (> m cs) (recur (+ n step) step)
        (< m cs) (recur (- n step) (/ step 10))))))

(defn find-nb [m] (find-nb-impl m 10000))