module KataBefungeInterpreterSpec where
  import KataBefungeInterpreter
  import Test.Hspec
  import System.Random (newStdGen)

  spec = describe "Befunge interpreter" $ do
    it "Example from description" $ do
      g <- newStdGen
      interpret g ">987v>.v\nv456<  :\n>321 ^ _@" `shouldBe` "123456789"