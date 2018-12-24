(ns kata.two-to-one
    (:require [clojure.set :as set]))
  
  (defn longest [s1 s2]
    (apply str (sort (set/union (set s1) (set s2)))))