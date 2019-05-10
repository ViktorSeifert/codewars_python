module KataEqualSidesOfAnArraySpec where
  import KataEqualSidesOfAnArray

  import Test.Hspec
  import Text.Printf (printf)

  testFind :: [Int] -> Int -> Spec
  testFind arr u = 
    it (printf "should return findEvenIndex for array : %s " (show arr)) $
      findEvenIndex arr `shouldBe` u

  spec = describe "findEvenIndex" $ do
    testFind [1,2,3,4,3,2,1] 3
    testFind [1,100,50,-51,1,1] 1
    testFind [1,2,3,4,5,6] (-1)
    testFind [20,10,30,10,10,15,35] 3
    testFind [20,10,-80,10,10,15,35] 0
    testFind [10,-80,10,10,15,35,20] 6
    testFind [0,0,0,0,0] 0
    testFind [-1,-2,-3,-4,-3,-2,-1] 3