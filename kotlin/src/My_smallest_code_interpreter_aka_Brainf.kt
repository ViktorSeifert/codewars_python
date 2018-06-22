class BrainLuck(private val code: String) {
    private val memory = mutableMapOf<Int, Char>()
    private var remainingInput = ""
    private var instructionPointer : Int = 0
    private var dataPointer : Int = 0
    private var output : StringBuilder = StringBuilder()
    private var codeView = code

    fun process(input: String): String {
        remainingInput = input
        instructionPointer = 0
        dataPointer = 0
        output = StringBuilder()
        codeView = code

        while (instructionPointer < code.length) {
            val currentInstruction = code[instructionPointer]
            when (currentInstruction) {
                '>' -> dataPointer += 1
                '<' -> dataPointer -= 1
                '+' -> increment()
                '-' -> decrement()
                '.' -> output.append(getMemWithSafeInit())
                ',' -> {
                    if (remainingInput != "") {
                        memory[dataPointer] = remainingInput[0]
                        remainingInput = remainingInput.slice(1 until remainingInput.length)
                    }
                }
                '[' -> {
                    instructionPointer = jumpRight()
                }
                ']' -> {
                    instructionPointer = jumpLeft()
                }
            }

            if (currentInstruction != '[' && currentInstruction != ']')
                instructionPointer += 1

            updateCodeView()
        }

        return output.toString()
    }

    private fun updateCodeView() {
        if (instructionPointer >= code.length) {
            codeView = code
            return
        }

        val result = StringBuilder()
        if (instructionPointer > 0)
            result.append(code.substring(0, instructionPointer))
        result.append("{")
        result.append(code[instructionPointer])
        result.append("}")
        if (instructionPointer < code.length - 1)
            result.append(code.substring(instructionPointer + 1, code.length))
    }

    private fun increment() {
        val currentValue : Char = getMemWithSafeInit()

        val nextValue = if (currentValue == 255.toChar()) 0.toChar()
            else (currentValue + 1)

        memory[dataPointer] = nextValue
    }

    private fun decrement() {
        val currentValue : Char = getMemWithSafeInit()

        val nextValue = if (currentValue == 0.toChar()) 255.toChar()
        else (currentValue - 1)

        memory[dataPointer] = nextValue
    }

    private fun jumpRight(): Int {
        var pointer = instructionPointer
        var loopLevel = 0

        if (getMemWithSafeInit() == 0.toChar()) {
            do {
                when (code[pointer]) {
                    '[' -> loopLevel += 1
                    ']' -> loopLevel -= 1
                }
                pointer += 1
            } while (loopLevel != 0)

            return pointer
        }

        return pointer + 1
    }

    private fun jumpLeft(): Int {
        var pointer = instructionPointer
        var loopLevel = 0

        if (getMemWithSafeInit() != 0.toChar())
            do {
                when (code[pointer]) {
                    '[' -> loopLevel += 1
                    ']' -> loopLevel -= 1
                }
                pointer -= 1
            }
            while (loopLevel != 0)

        return pointer + 1
    }

    private fun getMemWithSafeInit() : Char {
        if (!memory.containsKey(dataPointer))
            memory[dataPointer] = 0.toChar()

        return memory[dataPointer]!!
    }
}

fun main(args: Array<String>) {
    val input = charArrayOf(8.toChar(), 9.toChar())
    println(BrainLuck(",>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.")
            .process(input[0].toString() + input[1].toString()))

    val fiboIn = StringBuilder().append(10.toChar()).toString()
    println(BrainLuck(",>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]").process(fiboIn))
}