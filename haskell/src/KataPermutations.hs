-- https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/haskell

module KataPermutations where
  import Data.List (findIndices, sort)

  successorPairs :: String -> [(Char, Char)]
  successorPairs s = zip s (tail s)

  indexOfElementSmallerThanSuccessor :: String -> Int
  indexOfElementSmallerThanSuccessor s =
    foldl max (-1) $ findIndices (\(a, b) -> a < b) (successorPairs s)
  
  indexLargerThanLetterAtIndex :: String -> Int -> Int
  indexLargerThanLetterAtIndex s i = foldl1 max $ findIndices (\x -> x > (s !! i)) s

  swap :: String -> Int -> Int -> String
  swap s k l =
    let
      elemI = s !! k
      elemJ = s !! l
      left = take k s
      middle = take (l - k - 1) (drop (k + 1) s)
      right = drop (l + 1) s
    in left ++ [elemJ] ++ middle ++ [elemI] ++ right

  transformString :: String -> Int -> Int -> String
  transformString s k l =
    let
      strWithSwap = swap s k l
      firstPart = take (k + 1) strWithSwap
      secondPart = drop (k + 1) strWithSwap
    in firstPart ++ (reverse secondPart)


  nextPermutation :: String -> String
  nextPermutation s =
    let
      k = indexOfElementSmallerThanSuccessor s
    in
      if k == -1 then s
      else transformString s k (indexLargerThanLetterAtIndex s k)

  -- https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
  permutationsFrom :: String -> [String]
  permutationsFrom xs | xs == nextPermutation xs = [xs]
  permutationsFrom xs = xs : permutationsFrom (nextPermutation xs)

  permutations :: String -> [String]
  permutations "" = [""]
  permutations s = permutationsFrom $ sort s