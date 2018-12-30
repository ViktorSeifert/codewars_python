(ns kata.stat
  (:import
    java.time.Duration))

; https://www.codewars.com/kata/55b3425df71c1201a800009c/train/clojure

(def time-tuple-regex #"(\d?\d)\|(\d?\d)\|(\d?\d)")

(defn- parse-time-tuples [results-string]
  (map #(rest %) (re-seq time-tuple-regex results-string)))

(defn- to-duration-format [parsed-time-tuple]
  (str "PT" (nth parsed-time-tuple 0) "H" (nth parsed-time-tuple 1) "M" (nth parsed-time-tuple 2) "S"))

(defn- extract-durations [results-string]
  (->>
    (parse-time-tuples results-string)
    (map #(to-duration-format %))
    (map #(Duration/parse %))))

(defn- extract-range [durations]
  (let [
    sorted-durations (sort durations)
    smallest (first sorted-durations)
    largest (last sorted-durations)]
  (.minus largest smallest)))

(defn- extract-average [durations]
  (let [
    num-durations (count durations)
    durations-sum (reduce #(.plus %1 %2) durations)]
    (.dividedBy durations-sum num-durations)))

(defn- calculate-median-indices [seq-length]
  (let [m (/ (dec seq-length) 2)]
    (if (integer? m) #{m} #{(int (Math/floor m)) (int (Math/ceil m))})))

(defn- extract-median [durations]
  (let [
    sorted-durations (sort durations)
    median-indices (calculate-median-indices (count durations))]
    (extract-average (keep-indexed #(when (median-indices %1) %2) sorted-durations))))

(def number-with-2-leading-zeroes "%02d")

(defn- to-output-format [duration]
  (let [
    hours (.toHours duration)
    minutes (-> duration (.minusHours hours) (.toMinutes))
    seconds (-> duration (.minusHours hours) (.minusMinutes minutes) (.getSeconds))]
    (str
      (format number-with-2-leading-zeroes hours)
      "|" (format number-with-2-leading-zeroes minutes)
      "|" (format number-with-2-leading-zeroes seconds))))

(defn stat [results-string]
  (if (empty? results-string) ""
    (let [durations (extract-durations results-string)]
      (str
        "Range: "
        (-> durations (extract-range) (to-output-format))
        " Average: "
        (-> durations (extract-average) (to-output-format))
        " Median: "
        (-> durations (extract-median) (to-output-format))))))