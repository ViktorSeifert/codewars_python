(ns kata.piglatin
  (:require
    [clojure.string :as str]
    [clojure.set :refer :all]))

(defn- all-letters [from to]
  (let [start (int from) end (inc (int to))]
    (set (map char (range start end)))))

(def word-chars (union (all-letters \a \z) (all-letters \A \Z)))

(defn pig-it [s]
  (let [tokens (str/split s #" ")]
    (->>
      tokens
      (map #(if (every? word-chars %) (str (apply str (rest %)) (first %) "ay") %))
      (str/join " "))))