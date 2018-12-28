(ns kata.sudoku)

; Did I Finish my Sudoku?
; https://www.codewars.com/kata/53db96041f1a7d32dc0004d2/solutions/clojure
(defn- rows [sudoku-board]
  (for [x (range 0 9)] (sudoku-board x)))

(defn- number-at-pos [sudoku-board row-index column-index]
  (-> sudoku-board (nth row-index) (nth column-index)))

(defn- column [sudoku-board column-index]
  (for [x (range 0 9)] (number-at-pos sudoku-board x column-index)))

(defn- columns [sudoku-board]
  (for [x (range 0 9)] (column sudoku-board x)))

(def square-size 3)

(defn- square-index-ranges [square-index]
  (let
    [column-start-index (-> square-index (rem square-size) (* square-size))
     column-end-index (+ column-start-index square-size)
     row-start-index (-> square-index (/ square-size) (int) (* square-size))
     row-end-index (+ row-start-index square-size)]
    [row-start-index row-end-index column-start-index column-end-index]))

(defn- square [sudoku-board square-index]
  (let
    [[row-start-index row-end-index column-start-index column-end-index] (square-index-ranges square-index)]
    (for 
      [column-idx (range column-start-index column-end-index)
       row-idx (range row-start-index row-end-index)]
      (number-at-pos sudoku-board row-idx column-idx))))

(defn- squares [sudoku-board]
  (for [square-index (range 0 9)] (square sudoku-board square-index)))

(defn- contains-one-to-nine? [s]
  (= (set s) (set (range 1 10))))

(defn- all-rows-columns-squares [sudoku-board]
  (apply concat
    ((juxt rows columns squares) sudoku-board)))

(defn done-or-not [board]
    (if (every? contains-one-to-nine? (all-rows-columns-squares board))
      "Finished!"
      "Try again!"))
