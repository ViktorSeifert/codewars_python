-- https://www.codewars.com/kata/526c7b931666d07889000a3c/train/haskell

module KataBefungeInterpreter where
  import System.Random (StdGen, next)

  currentInstruction :: (Int, Int) -> [String] -> Char
  currentInstruction (x,y) instructions = instructions !! x !! y

  nextPosition :: StdGen -> (Int, Int) -> [String] -> (Int, Int)
  nextPosition rng pos@(x,y) instructions =
    let
      i = currentInstruction pos instructions
    in
      undefined

  runBF :: StdGen -> (Int, Int) -> [Int] -> [String] -> String
  runBF rng pos@(x,y) stack instructions = 
    let
      i = currentInstruction pos instructions
      nextPos = nextPosition rng pos instructions
    in
      case i of
        '@' -> concat $ map show stack
        '0' -> runBF rng nextPos (0 : stack) instructions

  interpret :: StdGen -> String -> String
  interpret rng instructions = runBF rng (0, 0) [] (lines instructions)