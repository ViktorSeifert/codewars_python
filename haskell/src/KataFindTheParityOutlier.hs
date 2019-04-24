module KataFindTheParityOutlier (findOutlier) where
  groupEm :: [Int] -> [[Int]]
  groupEm xs = [(filter odd xs), (filter even xs)]

  findOutlier :: [Int] -> Int 
  findOutlier xs = (head . head) $ filter (\x -> length x == 1) $ groupEm xs