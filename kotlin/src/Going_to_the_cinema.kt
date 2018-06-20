package going

import java.lang.Math.pow

// see https://en.wikipedia.org/wiki/Geometric_series about developing the formula.
// the code calculates the partial sum not the value of the series.
fun priceOfAllDiscountedTickets(ticket: Int, numberOfVisits: Int, discount: Double): Double {
    val x = pow(discount.toDouble(), numberOfVisits.toDouble()) - 1.0
    val y = discount.toDouble() - 1.0
    return Math.ceil(ticket.toDouble() * (x / y))
}

fun movie(card:Int, ticket:Int, perc:Double):Int {
    // if we would need to go for more speed we could transform this into a binary search.
    for (i in 1..Int.MAX_VALUE) {
        val regular = i * ticket
        val cardSystem = Math.ceil(card + priceOfAllDiscountedTickets(ticket, i, perc))

        // unsure why there is a off-by-one-error without the -1.
        if (cardSystem < regular)
            return i - 1
    }

    return 0
}

fun main(args: Array<String>) {
    println(movie(500, 15, 0.9))
    println(movie(100, 10, 0.95))
}