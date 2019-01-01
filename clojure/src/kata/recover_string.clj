(ns kata.recover-string
  (:require [clojure.set :refer [difference union]]))

(defn- graph-edges-from-triplet [triplet]
  (let 
    [alpha (nth triplet 0) beta (nth triplet 1) gamma (nth triplet 2)]
    #{[alpha beta] [alpha gamma] [beta gamma]}))

(defn- top-sort [graph]
  (loop [g graph result []]
    (if (= (count g) 1) (concat (first g) result)
      (let [
        heads (set (map first g))
        tails (set (map second g))
        no-successor-node (first (difference tails heads))]
        (recur (remove #(= (second %) no-successor-node) g) (cons no-successor-node result))))))

(defn recover-secret [triplets]
  (->>
    triplets
    (map #(graph-edges-from-triplet %))
    (apply union)
    (top-sort)
    (apply str)))