module KataRemoveTheMinimum where
  removeEm :: [Int] -> [Int] -> [Int] -> [Int]
  removeEm [] _ acc = acc
  removeEm (x:xs) [] acc = removeEm xs [] $ x : acc
  removeEm (x:xs) (y:ys) acc =
    if x == y then removeEm xs ys acc else removeEm xs (y:ys) (x:acc)

  removeSmallest :: [Int] -> [Int]
  removeSmallest xs = reverse $ removeEm xs [minimum xs] []