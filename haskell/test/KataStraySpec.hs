module KataStraySpec (spec) where

  import Test.Hspec
  import KataStray (stray)
  
  spec :: Spec
  spec = do
    it "example test" $ do
      stray [1,1,2] `shouldBe` 2
      stray [6974,-931,6974] `shouldBe` -931