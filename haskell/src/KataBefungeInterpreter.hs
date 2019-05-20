-- https://www.codewars.com/kata/526c7b931666d07889000a3c/train/haskell

module KataBefungeInterpreter where
  import System.Random (StdGen, next)
  import Data.Char (digitToInt)

  runBF :: StdGen -> (Int, Int) -> [String] -> [Int] -> String
  runBF rng pos@(x,y) instructions stack = 
    let
      i = currentInstruction pos instructions
      (nextX, nextY, nextRng) = nextPosition rng pos instructions
      runIt = runBF nextRng (nextX, nextY) instructions
    in
      case i of
        '@' -> concat $ map show stack
        i | i `elem` "012345689" -> runIt (digitToInt i : stack)
        '+' -> runIt (performAdd stack)
        '-' -> runIt (performSub stack)
        '*' -> runIt (performMult stack)
        '/' -> runIt (performDiv stack)
        '%' -> runIt (performMod stack)
        '!' -> runIt (performNot stack)
        '`' -> runIt (performGt stack)

  currentInstruction :: (Int, Int) -> [String] -> Char
  currentInstruction (x,y) instructions = instructions !! y !! x

  nextPosition :: StdGen -> (Int, Int) -> [String] -> (Int, Int, StdGen)
  nextPosition rng pos@(x,y) instructions =
    let
      i = currentInstruction pos instructions
      (randN, nextRng) = next rng
      (deltaX, deltaY) = move randN i
      nextX = (x + deltaX) `rem` (length (instructions !! 0))
      nextY = (x + deltaY) `rem` (length instructions)
    in
      (nextX, nextY, nextRng)

  move :: Int -> Char -> (Int, Int)
  move _ '^' = (0, -1)
  move _ '<' = (-1, 0)
  move _ '>' = (1, 0)
  move _ 'v' = (0, 1)
  move rand '?' = move rand $ "<>^v" !! rand
  move r _ = move r '>'

  performAdd :: [Int] -> [Int]
  performAdd (x:y:xs) = x + y : xs

  performSub :: [Int] -> [Int]
  performSub (x:y:xs) = y - x : xs

  performMult :: [Int] -> [Int]
  performMult (x:y:xs) = x * y : xs

  performDiv :: [Int] -> [Int]
  performDiv (x:y:xs) = y `quot` x : xs

  performMod :: [Int] -> [Int]
  performMod (x:y:xs) = y `rem` x : xs

  performNot :: [Int] -> [Int]
  performNot (0:xs) = 1 : xs
  performNot (1:xs) = 0 : xs

  performGt :: [Int] -> [Int]
  performGt (x:y:xs) = if y > x then 1:xs else 0:xs

  interpret :: StdGen -> String -> String
  interpret rng instructions = runBF rng (0, 0) (lines instructions) []