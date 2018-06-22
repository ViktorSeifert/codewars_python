package longestconsec

fun longestConsec(strarr:Array<String>, k:Int):String {
    if (strarr.isEmpty().or( k <= 0).or(k > strarr.size))
        return ""

    val lengths = mutableListOf<Int>()

    for ((index, element) in strarr.withIndex()) {
        if (index + k - 1 >= strarr.size)
            break

        val l = strarr.sliceArray(index until index + k).sumBy { x -> x.length }

        lengths.add(l)
    }

    val largestIndex = lengths.indexOfFirst { x -> x == lengths.max() }

    return strarr.sliceArray(largestIndex until largestIndex + k).fold("") { acc, elem
        -> acc + elem}
}

fun main(args: Array<String>) {
    println(longestConsec(arrayOf<String>("zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"), 2))
    println(longestConsec(arrayOf<String>("ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"), 1))
}