import math

RAD_30 = 30 * math.pi / 180
RAD_45 = 45 * math.pi / 180


class Shape_Standard:


    def equilateral_triangle(side: float)->float:
        return  round(2 * side* math.tan(RAD_30), 3)
    
    def square(side: float)->float:
        return round(side / math.cos(RAD_45), 3)

    def rectangle(big_side: float, small_side: float)->float:
        return round( pow((big_side ** 2) + (small_side ** 2) , 0.5), 3)
    
    def hexagon(dimension: float) -> float:
        return round(( 2 * (dimension * 0,5 / (math.cos(RAD_30)))), 3)

class Shape:

    def __init__(
        self, 
        shape_name_ua: str = None,
        shape_name_en: str = None,
        image: str = None,
        dimentions: dict = None,
        circumscribed_circle: float = 0.0,
        shape_name_ua_full: str=None,
        shape_name_en_full: str=None,
        margin: float = None) -> None:
        self.shape_name_ua = shape_name_ua
        self.shape_name_en = shape_name_en
        self.image = image
        self.dimentions = dimentions
        self.circumscribed_circle = circumscribed_circle
        self.shape_name_ua_full = shape_name_ua_full
        self.shape_name_en_full = shape_name_en_full
        self.margin = margin

    
