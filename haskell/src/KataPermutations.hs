-- https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/haskell

module KataPermutations where
  import Data.List (sort)

  indexOfElementSmallerThanSuccessor :: String -> Int
  indexOfElementSmallerThanSuccessor s = 
    indexOfElementSmallerThanSuccessorImpl s 0 where
      indexOfElementSmallerThanSuccessorImpl (x:[]) _ = -1
      indexOfElementSmallerThanSuccessorImpl (x:y:xs) n =
        if x < y then n
          else indexOfElementSmallerThanSuccessorImpl (y:xs) (n+1)

  -- https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
  nextPermutation :: String -> String
  nextPermutation = error "TODO"

  permutationsFrom :: String -> [String]
  permutationsFrom xs | xs == nextPermutation xs = [xs]
  permutationsFrom xs = xs : [nextPermutation xs]

  permutations :: String -> [String]
  permutations "" = [""]
  permutations s = permutationsFrom $ sort s