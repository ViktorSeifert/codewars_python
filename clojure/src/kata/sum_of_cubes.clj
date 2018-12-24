(ns kata.sum-of-cubes)

(defn- cube-sum [n]
  (* (/ 1 4) (* n n) (* (inc n) (inc n))))

(defn- find-nb-impl [m initial-step]
  (loop [n 1 step initial-step]
    (let [cs (cube-sum n)]
      (cond
        (< step 1) -1
        (= m cs) n
        (> m cs) (recur (+ n 1) step)
        (< m cs) (recur (- n step) (/ step 10))))))

(defn find-nb [m] (find-nb-impl m 100))