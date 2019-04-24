module KataPeteTheBakerSpec where
  import KataPeteTheBaker (cakes)
  import Data.Function (on)
  import Data.List (nubBy)
  import Test.Hspec
  import Control.Applicative
  
  spec = describe "cakes" $ do
      it "should work for some small examples" $ do
        cakes [("flour",500), ("sugar",200), ("eggs",1)] [("flour",1200), ("sugar",1200), ("eggs",5), ("milk",200)]  `shouldBe` 2
        cakes [("apples",3), ("flour",300), ("sugar",150), ("milk",100), ("oil",100)] [("sugar",500), ("flour",2000), ("milk",2000)] `shouldBe` 0