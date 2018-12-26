(ns kata.rainfall
  (:require [clojure.string :as str]))

(defn- extract-data-from-single-line [data-line]
  (let [[city-name city-data-string] (str/split data-line #":")]
    {(str/trim city-name)
      (->>
        (re-seq #"\d+(\.\d+)?" city-data-string)
        (map #(first %))  
        (map #(read-string %))
        (vec))}))

(defn- extract-data [data-as-string]
  (let [data-lines (str/split-lines data-as-string)]
    (apply merge
      (for [data-line data-lines]
        (extract-data-from-single-line data-line)))))

(defn mean [twn strng] 
  (let [town-data (get (extract-data strng) twn)]
    (if (nil? town-data)
      -1
      (/ (reduce + town-data) (count town-data)))))

(defn variance [twn strng] 
  (let [
      town-data (get (extract-data strng) twn)
      town-mean (mean twn strng)
      num-data-points (count town-data)]
    (if (nil? town-data)
      -1
      (->> town-data
        (map #(- % town-mean))
        (map #(* % %))
        (map #(/ % num-data-points))
        (reduce +)))))
