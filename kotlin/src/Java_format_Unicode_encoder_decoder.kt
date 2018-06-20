object JavaUnicodeEncoder {
    fun decode(input:String?):String {
        if (input == null)
            return ""

        val result = StringBuilder()
        for (part in input.split("\\u").filter { x -> x.isNotBlank() }) {
            val value = Integer.parseInt(part, 16).toChar()
            result.append(value)
        }

        return result.toString()
    }

    fun encode(input:String?):String {
        if (input == null)
            return ""

        val result = StringBuilder()

        for (c in input) {
            val hexString = c.toInt().toString(16)

            result.append("\\u" + hexString.padStart(4, '0'))
        }

        return result.toString()
    }
}

fun main(args: Array<String>) {
    println(JavaUnicodeEncoder.encode("hola"))
    println(JavaUnicodeEncoder.decode("\\u0068\\u006f\\u006c\\u0061"))
}