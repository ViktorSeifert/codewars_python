(ns kata.band-name-generator
    (:require [clojure.string :as s]))

(defn generate-band-name [noun]
  (let [first-letter (.substring noun 0 1)
        but-first (.substring noun 1)
        cap-noun (s/capitalize noun)]
    (if (s/ends-with? noun first-letter)
        (str cap-noun but-first)
        (str "The " cap-noun))))