module KataSumOddNumbers where
  sumToN :: Integer -> Integer
  sumToN n = (n * n + n) `quot` 2

  rowSumOddNumbers :: Integer -> Integer
  rowSumOddNumbers n =
    let
      sumn = sumToN n
      sumn_minus1 = sumToN $ n - 1
    in (sumn * sumn) - (sumn_minus1 * sumn_minus1)