(ns array-diff)
(defn array-diff [a b]
  (let [filtering-set (set b)
        filtering-function #(not (filtering-set %))]
    (filter filtering-function a)))