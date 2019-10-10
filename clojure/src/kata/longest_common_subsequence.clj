(ns kata.longest-common-subsequence)
; https://www.codewars.com/kata/593ff8b39e1cc4bae9000070/train/clojure

(defn- lcs-impl [x y result]
    (if (or (empty? x) (empty? y))
        result
        (let [fx (first x)
              fy (first y)
              xs (rest x)
              ys (rest y)]
            (if (= fx fy)
                (recur xs ys (cons fx result))
                (let [lcsX (lcs-impl x ys result)
                      lcsY (lcs-impl xs y result)]
                    (if (> (count lcsX) (count lcsY))
                        lcsX
                        lcsY))))))

(defn lcs
    [^String x ^String y]
    (->>
        (lcs-impl (reverse x) (reverse y) [])
        (apply str)))