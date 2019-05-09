module KataPascalsTriangle where
  innerSums :: [Int] -> [Int]
  innerSums (x:[]) = []
  innerSums (x:y:xs) = (x + y) : innerSums (y:xs)

  pascalSuccessor :: [Int] -> [Int]
  pascalSuccessor [1] = [1, 1]
  pascalSuccessor xs = [1] ++ (innerSums xs) ++ [1]

  allPascalLists :: [[Int]]
  allPascalLists = iterate pascalSuccessor [1]

  pascalsTriangle :: Int -> [Int]
  pascalsTriangle n = concat $ take n allPascalLists