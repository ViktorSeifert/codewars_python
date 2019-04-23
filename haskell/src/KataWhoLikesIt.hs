module KataWhoLikesIt where
  likes :: [String] -> String
  likes [] = "no one likes this"
  likes (x:[]) = x ++ " likes this"
  likes (x:y:[]) = x ++ " and " ++ y ++ " like this"
  likes (x:y:z:[]) = like x y z
  likes (x:y:xs) = like x y $ (show $ length(xs)) ++ " others"

  like :: String -> String -> String -> String
  like x y z = x ++ ", " ++ y ++ " and " ++ z ++ " like this"
