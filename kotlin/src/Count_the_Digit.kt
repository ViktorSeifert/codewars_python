package countdig

fun nbDig(n:Int, d:Int):Int {
    val target = d.toString().toCharArray()[0]
    var count = 0

    for (i in 0..n) {
        val digits = (i * i).toString()


        for (digit in digits)
            if (digit == target)
                count += 1
    }

    return count
}

fun main(args: Array<String>) {
    println(nbDig(5750, 0))
    println(nbDig(11011, 2))
}