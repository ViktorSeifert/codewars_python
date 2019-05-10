module KataEqualSidesOfAnArray where
  import Debug.Trace
  -- findEvenIndexImpl arr n | trace ("findEvenIndexImpl " ++ show arr ++ " " ++ show n) False = undefined

  findEvenIndexImpl :: [Int] -> Int -> Int
  findEvenIndexImpl arr n
    | n == length arr = (-1)
    | otherwise =
      let
        firstPart = take n arr
        secondPart = drop (n + 1) arr
      in
        if (sum firstPart) == (sum secondPart)
        then n
        else findEvenIndexImpl arr (n + 1)

  findEvenIndex :: [Int] -> Int
  findEvenIndex arr = findEvenIndexImpl arr 0