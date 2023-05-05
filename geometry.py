import math

#from db_handler import DB_shapes as dbs 


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
    
    def oblong(big_side: float, small_side: float) -> float:
        return big_side if big_side >= small_side else small_side
    
    def single_D(diamert: float, height: float) -> float:
        if diamert > height:
            return diamert 
        else:
            raise ValueError
        
    def double_D(diamert: float, height: float) -> float:
        if diamert > height:
            return diamert
        else:
            raise ValueError
    
    def quad_D(diamert: float, dimention: float) -> float:
        if diamert > dimention:
            return diamert
        else:
            raise ValueError
    
    def quad_R(side_a: float, side_b: float, radius: float) -> float:
        side_a_1 = side_a - (2 * radius)
        side_b_1 = side_b - (2 * radius)
        diagonal = round( pow((side_a_1 ** 2) + (side_b_1 ** 2) , 0.5), 3)
        return diagonal + (2 * radius)

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
        self.__shape_name_ua = shape_name_ua
        self.__shape_name_en = shape_name_en
        self.__image = image
        self.__dimentions = dimentions
        self.__circumscribed_circle = circumscribed_circle
        self.__shape_name_ua_full = shape_name_ua_full
        self.__shape_name_en_full = shape_name_en_full
        self.__margin = margin


    def set_shape_name_ua(self, new_shape_name_ua) -> None: #Set user in wiget
        self.__shape_name_ua = new_shape_name_ua
        
    def get_shape_name_ua(self) -> str:
        return self.__shape_name_ua

    def set_shape_name_en(self, new_shape_name_en) -> None:#Set in db_hendler with shape_name_ua
        self.__shape_name_en = new_shape_name_en
        
    def get_shape_name_en(self) -> str: 
        return self.__shape_name_en
    
    def set_image(self, new_image: str) -> None:
        self.__image = new_image

    def get_image(self) -> None: # How to public picture in wiget?
        return self.__image
    
    def set_dimentions(self) -> None:
        # name = self.get_shape_name_en()
        # if name is None:
        #     print("Need shape name")
        # elif name in dbs.get_list_shape(): #How to handle different shapes
        #     if name == "round":
        #         pass
        #     elif name == "square":
        #         pass
        #     elif name == "rectangle":
        #         pass
        # else:
        #     print("Invalid name shape.")
        pass

    def get_dimentions(self) -> dict:
        return self.__dimentions

    def set_circumscribed_circle(self) -> None:
        self.__circumscribed_circle = self.count_circumscribed_circle()

    def get_circumscribed_circle(self) -> float:
        return self.__circumscribed_circle
    
    def set_shape_name_ua_full(self) -> None:
        pass
        #self.__shape_name_ua_full = ?

    def get_shape_name_ua_full(self) -> float:
        return self.__shape_name_ua_full
    
    def set_shape_name_en_full(self) -> None:
        pass
        #self.__shape_name_en_full = ?
    
    def get_shape_name_en_full(self) -> float:
        return self.__shape_name_en_full

    def set_margin(self) -> None:
        pass
        #self.__margin = ?

    def get_margin(self) -> float:
        return self.__margin

    def count_circumscribed_circle(self) -> float:
        pass


print(Shape_Standard.quad_R(80.0, 50.0, 10.0))