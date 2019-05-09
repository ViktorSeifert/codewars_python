module KataTribonacciSequence where
  tribonacciImpl :: Num a => a -> a -> a -> [a]
  tribonacciImpl a b c = (a + b + c) : tribonacciImpl b c (a + b + c)

  tribonacci :: Num a => (a, a, a) -> Int -> [a]
  tribonacci _ 0 = []
  tribonacci (a, b, c) 1 = [a]
  tribonacci (a, b, c) 2 = [a, b]
  tribonacci (a, b, c) 3 = [a, b, c]
  tribonacci (a, b, c) n = [a, b, c] ++ (take (n - 3) (tribonacciImpl a b c))