(ns kata.caesar2-test
  (:require [clojure.test :refer :all]
            [kata.caesar2 :refer :all]))

(deftest a-test1
  (testing "Test1"
    (def u "I should have known that you would have a perfect answer for me!!!")
    (def v ["ijJ tipvme ibw","f lopxo uibu z","pv xpvme ibwf ","b qfsgfdu botx","fs gps nf!!!"])
    (is (= (encode-str u 1) v))))
(deftest a-test2
  (testing "Test2"
    (def u "How can we become the kind of people that face our fear and do it anyway?")
    (def v ["hiIpx dbo xf cf","dpnf uif ljoe p","g qfpqmf uibu g","bdf pvs gfbs bo","e ep ju bozxbz?"])
    (is (= (encode-str u 1) v))))
