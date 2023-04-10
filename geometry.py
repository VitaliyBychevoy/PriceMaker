import math

RAD_30 = 30 * math.pi / 180
RAD_45 = 45 * math.pi / 180


class Shape_Standart:


    def equilateral_triangle(side: float)->float:
        return  round(2 * side* math.tan(RAD_30), 3)
    
    def square(side: float)->float:
        return round(side / math.cos(RAD_45), 3)

    def rectangle(big_side: float, small_side: float)->float:
        return round( pow((big_side ** 2) + (small_side ** 2) , 0.5), 3)
    
    def hexagon(dimension: float) -> float:
        return round(( 2 * (dimension * 0,5 / (math.cos(RAD_30)))), 3)

