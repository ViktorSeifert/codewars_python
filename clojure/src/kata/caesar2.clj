(ns kata.caesar2
  (:require [clojure.string :refer [lower-case]]
            [clojure.set :refer [union]]))

; https://www.codewars.com/kata/second-variation-on-caesar-cipher/train/clojure

(def low (vec (map char (range (int \a) (->> \z int inc)))))

(def up (vec (map char (range (int \A) (->> \Z int inc)))))

(def letters (union (set low) (set up)))

(defn- letter-map [shift]
  (merge 
    (zipmap (concat (take-last shift low) (take (- 26 shift) low)) low)
    (zipmap (concat (take-last shift up) (take (- 26 shift) up)) up)))

(defn- cypher-mapping [shift]
  (let [lm (letter-map shift)]
    (fn [l] (if (contains? letters l) (lm l) l))))

(defn- split-to-n-parts [n s]
  (let [chunk-size (->> (/ (count s) n) Math/ceil int)]
    (loop [result [] rest (seq s)]
      (if (empty? rest)
        result
        (recur (conj result (take chunk-size rest)) (drop chunk-size rest))))))

(defn encode-str [input shift]
  (let [
    encoded-input (->> (map #((cypher-mapping shift) %) input) (apply str))
    prefix (str (->> input first lower-case) (->> encoded-input first lower-case))]
    (->>
      (str prefix encoded-input)
      (split-to-n-parts 5)
      (map #(apply str %)))))

(defn decode [s])
