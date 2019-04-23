module KataStray (stray) where
  import Data.List

  stray :: [Int] -> Int
  stray xs = (head . head) $ filter (\x -> length x == 1) $ group $ sort xs
