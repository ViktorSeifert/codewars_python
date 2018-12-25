(ns kata.sum-of-cubes)

; https://www.codewars.com/kata/build-a-pile-of-cubes/train/clojure
; Taken from https://rosettacode.org/wiki/Nth_root#Clojure
(defn- abs [x]
  " Absolute value"
  (if (< x 0) (- x) x))
 
(defn- power [x n]
  " x to power n, where n = 0, 1, 2, ... "
  (apply * (repeat n x)))
 
(defn- calc-delta [A x n]
  " nth rooth algorithm delta calculation "
  (/ (- (/ A (power x (- n 1))) x) n))
 
(defn- nth-root
  " nth root of algorithm: A = numer, n = root"
  ([A n] (nth-root A n 0.5 1.0))
  ([A n guess-prev guess-current]
   (if (< (abs (- guess-prev guess-current)) 1e-6)
     guess-current
     (recur A n guess-current (+ guess-current (calc-delta A guess-current n))))))

; ----------------------------------------------------------------

(defn- cube-sum [n]
  (* (/ 1 4) (* n n) (* (inc n) (inc n))))

(defn- root-part [m]
  (nth-root (+ 1 (* 8 (nth-root m 2))) 2))

(defn- inverse-cube-sum [m]
  (let [rp (root-part m)]
    (/ (+ -1 rp) 2)))

; Usually it would be enough to check
; if the inverse-cube-sum is an integer.
; But somewhere in the code there's a
; slight rounding error (probably in nth-root).
; So for an input of 10252519345963644753026N
; the solution would answer 450010N.
; But the cube-sum of 450010N is
; 10252519345963644753025N -> it's off by one ;-)
; So we compare with the cube-sum.
(defn find-nb [m]
  (let [im (inverse-cube-sum m)
        iim (cube-sum (bigdec im))]
    (if (== m iim) (bigint im) -1)))