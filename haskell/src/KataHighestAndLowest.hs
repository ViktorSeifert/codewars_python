module KataHighestAndLowest (highAndLow) where

  import Data.List.Split

  tokenize aString = splitOn " " aString

  strToInt aString = read aString :: Integer

  minNumber = foldl1 min
  maxNumber = foldl1 max

  joinWithSeparator sep a b = (show a) ++ sep ++ (show b)
  
  join = joinWithSeparator " "

  highAndLow :: String -> String
  highAndLow input = 
    let tokenizedInput = tokenize input
        inputAsNumbers = map strToInt tokenizedInput
        maxInput = maxNumber inputAsNumbers
        minInput = minNumber inputAsNumbers
      in join maxInput minInput
