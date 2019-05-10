-- https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/haskell

module KataPermutations where
  import Data.List (nub, delete)
  allPermutations :: String -> [String]
  allPermutations (x:[]) = [x:[]]
  allPermutations xs = 
    concat $
      map (\element ->
        let
          allPermutationsWithoutElement = allPermutations $ delete element xs
        in
          map (element :) allPermutationsWithoutElement
      ) xs

  permutations :: String -> [String]
  permutations "" = [""]
  permutations s = nub $ allPermutations s