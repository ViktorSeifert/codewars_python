class Node {
    val next : Node? = Node()
}

fun loopSize(n: Node): Int {
    var runner = n
    var jumper = n
    var jumpSize = 2
    var steps = 0

    while (true) {
        val next = runner.next ?: return 0

        runner = next
        steps += 1

        if (runner == jumper)
            return countLoop(runner)

        if (steps % jumpSize == 0) {
            steps = 0
            jumpSize *= 2
            jumper = runner
        }
    }
}

fun countLoop(start: Node): Int {
    var current = start
    var steps = 0

    do {
        current = current.next!!
        steps += 1
    }
    while (current != start)

    return steps
}
