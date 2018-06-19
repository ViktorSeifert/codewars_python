package voltank

import java.lang.Math.pow
import kotlin.math.PI
import kotlin.math.asin
import kotlin.math.sqrt

fun tankVol(h:Int, d:Int, vt:Int):Int {
    val radius = d.toDouble() / 2.0

    // since the problem is symmetrical (1/4 is basically the same as 3/4) we can just flip the value
    val remainingDistanceToCenter = if (h <= radius)
        radius - h.toDouble()
    else
        (radius - h.toDouble()) * - 1.0

    val liquidSurfaceSideToSideLengthHalved = sqrt(pow(radius, 2.0) - pow(remainingDistanceToCenter, 2.0))

    val circleAngle = asin(liquidSurfaceSideToSideLengthHalved / radius)

    val totalCircleArea = PI * pow(radius, 2.0)
    val partialCircleArea = totalCircleArea * (circleAngle / PI)

    // usually the formula has a factor of 1/2,
    // but we need the area twice
    val triangleArea = liquidSurfaceSideToSideLengthHalved * remainingDistanceToCenter

    val liquidArea = partialCircleArea - triangleArea

    val liquidVolume = vt.toDouble() * (liquidArea / totalCircleArea)

    // symmetry again
    if (h <= radius)
        return liquidVolume.toInt()
    else
        return (vt - liquidVolume).toInt()
}

fun main(args : Array<String>) {
    println(tankVol(40,120,3500))
    println(tankVol(60,120,3500))
    println(tankVol(80,120,3500))
}