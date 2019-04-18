module KataIsThisATriangle where

import Data.List (sort)

isTriangle :: Int -> Int -> Int -> Bool
isTriangle a b c = (firstSmallerThanRest . reversedSort) [a, b, c]

firstSmallerThanRest (x : xs) = x < (sum xs)

reversedSort = reverse . sort