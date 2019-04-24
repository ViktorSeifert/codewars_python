module KataRemoveTheMinimumSpec where
  import KataRemoveTheMinimum
  import Test.Hspec

  spec = describe "removeSmallest" $ do
    it "works for the examples" $ do
      removeSmallest [1,2,3,4,5] `shouldBe` [2,3,4,5]
      removeSmallest [5,3,2,1,4] `shouldBe` [5,3,2,4]
      removeSmallest [2, 2, 1, 2, 1] `shouldBe` [2, 2, 2, 1]
      removeSmallest [] `shouldBe` ([] :: [Int])

