module KataValidPhoneNumber where
  import qualified Data.Char as DC

  data Token = OpenParen | CloseParen | Digit | Space | Dash | Unkown Char deriving (Eq, Show)

  phoneNumberTemplate :: [Token]
  phoneNumberTemplate =
    [OpenParen,
    Digit,
    Digit,
    Digit,
    CloseParen,
    Space,
    Digit,
    Digit,
    Digit,
    Dash,
    Digit,
    Digit,
    Digit,
    Digit]

  toToken :: Char -> Token
  toToken '(' = OpenParen
  toToken ')' = CloseParen
  toToken ' ' = Space
  toToken '-' = Dash
  toToken c
    | DC.isDigit c = Digit
    | otherwise = Unkown c

  validPhoneNumber :: String -> Bool
  validPhoneNumber phoneNumber = phoneNumberTemplate == (map toToken phoneNumber)