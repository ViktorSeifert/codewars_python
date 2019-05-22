-- https://www.codewars.com/kata/526c7b931666d07889000a3c/train/haskell

module KataBefungeInterpreter where
  import System.Random (StdGen, next)
  import Data.Char (digitToInt)

  runBF :: StdGen -> (Int, Int) -> [String] -> Char -> String -> [Int] -> String
  runBF rng pos@(x,y) instructions currentDirection output stack = 
    let
      i = currentInstruction pos instructions
      (nextX, nextY, nextRng) = nextPosition rng pos instructions currentDirection
      continueWithDirection = runBF nextRng pos instructions
      continueWithOutputAndStack = runBF nextRng (nextX, nextY) instructions currentDirection
      continueWithStack = continueWithOutputAndStack output
    in
      case i of
        '@' -> output
        i | i `elem` "012345689" -> continueWithStack (digitToInt i : stack)
        '+' -> continueWithStack (performAdd stack)
        '-' -> continueWithStack (performSub stack)
        '*' -> continueWithStack (performMult stack)
        '/' -> continueWithStack (performDiv stack)
        '%' -> continueWithStack (performMod stack)
        '!' -> continueWithStack (performNot stack)
        '`' -> continueWithStack (performGt stack)
        ':' -> continueWithStack (performDup stack)
        '\\' -> continueWithStack (performSwap stack)
        '$' -> continueWithStack (tail stack)
        '.' -> continueWithOutputAndStack (output ++ show (head stack)) (tail stack)
        i | i `elem` "<>v^?" -> continueWithDirection i output stack
        '_' -> if head stack == 0 
          then continueWithDirection '>' output (tail stack)
          else continueWithDirection '<' output (tail stack)
        '|' -> if head stack == 0
          then continueWithDirection 'v' output (tail stack)
          else continueWithDirection '^' output (tail stack)

  currentInstruction :: (Int, Int) -> [String] -> Char
  currentInstruction (x,y) instructions = instructions !! y !! x

  nextPosition :: StdGen -> (Int, Int) -> [String] -> Char -> (Int, Int, StdGen)
  nextPosition rng pos@(x,y) instructions currentDirection =
    let
      (randN, nextRng) = next rng
      (deltaX, deltaY) = move randN currentDirection
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

  performDup :: [Int] -> [Int]
  performDup [] = [0]
  performDup (x:xs) = x:x:xs

  performSwap :: [Int] -> [Int]
  performSwap (x:[]) = 0:x:[]
  performSwap (x:y:xs) = y:x:xs

  interpret :: StdGen -> String -> String
  interpret rng instructions = runBF rng (0, 0) (lines instructions) "" []