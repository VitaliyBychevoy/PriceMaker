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
        # image: str = None,
        dimentions: dict = None,
        circumscribed_circle: float = 0.0,
        shape_name_ua_full: str=None,
        shape_name_en_full: str=None,
        margin: float = None) -> None:
        self.shape_name_ua = shape_name_ua
        self.shape_name_en = shape_name_en
        # self.image = image
        self.dimentions = dimentions
        self.circumscribed_circle = circumscribed_circle
        self.shape_name_ua_full = shape_name_ua_full
        self.shape_name_en_full = shape_name_en_full
        self.margin = margin

    def set_shape_name_ua(self, new_shape_name_ua) -> None:
        self.shape_name_ua = new_shape_name_ua
    
    def set_shape_name_ua(self) -> None:
        return self.shape_name_ua

    def set_shape_name_en(self, new_shape_name_en) -> None:
        self.shape_name_en = new_shape_name_en
    
    def get_shape_name_en(self) -> str:
        return self.shape_name_en
    
    # def set_image(self, new_image) -> None:
    #     self.image = new_image
    
    # def get_image(self) -> str:
    #     return self.image
    
    def set_dimentions(self, new_dimention: dict) -> None:
        self.dimentions = new_dimention
    
    def get_dimentions(self) -> dict:
        return self.dimentions
    
    def set_circumscribed_circle(self, new_dimentions:dict) -> None:
        pass
        #self.circumscribed_circle = new_dimentions
    
    def get_circumscribed_circle(self) -> float:
        return self.circumscribed_circle
    
    def set_shape_name_ua_full(self, new_shape_name_ua: str, dimentions: dict) -> None:
        self.set_shape_name_ua_full = "Використати get_shape_name_ua() та get_dimentions()"
    
    def get_shape_name_ua_full(self) -> str:
        return self.shape_name_ua_full
    
    def set_shape_name_en_full(self, new_shape_name_en: str, dimentions: dict) -> None:
        self.set_shape_name_ua_full = "Використати get_shape_name_ua() та get_dimentions()"
    
    def get_shape_name_en_full(self) -> str:
        return self.shape_name_en_full
    
