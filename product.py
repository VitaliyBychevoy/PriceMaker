from geometry import Shape_Standart

system_list = [
    'Standart', 
    'Quickset', 
    'Slotting', 
    'Fully guided', 
    'RP'
    ]

punch_name = [
    'Пуансон', 
    'Вставка пуансона'
    ]


shape_type_ua = {
    'Round' : 'Коло',
    'Rectangle': 'Прямокутик',
    'Square': 'Квадрат'
}

shapes = [
    'round', 
    'rectangle', 
    'square'
    ]

shape_name_ua_list = [
    'коло', 'прямокутник', 'квадрат'
]

shape_list = {

    'round': 
        {
        'name': 'round',
        'code': 'R',
        'diametr_a': 0.0,
        },

    'rectangle': {
        'name': 'rectangle',
        'code': 'RE',
        'size_a': 0.0,
        'size_b': 0.0
    },
    'square': {
        'name': 'square',
        'code': 'SQ',
        'size_a': 0.0
    }
}
class Punch:

    def __init__(
            self,
            type_mashine: str=None,
            type_sistem: str=None, 
            punch_name_en: str=None, 
            punch_name_ua: str=None,
            shape_name_ua: str=None, 
            shape: dict=None,
            station: str=None, 
            purchase_price: float=0.0, 
            selling_price: float=0.0
            ) -> None:
        self.type_mashime = type_mashine
        self.type_system = type_sistem
        self.punch_name_en = punch_name_en
        self.punch_name_ua = punch_name_ua
        self.shape_name_ua = shape_name_ua
        self.shape = shape
        self.station = station
        self.purchase_price = purchase_price
        self.selling_price = selling_price


    def set_type_mashine(self, new_type: str) -> None:
        self.type_mashime = new_type

    def get_type_mashine(self) -> str:
        return self.type_mashime
    
    def set_type_system(self, new_system: str) -> None:
        self.type_system = new_system

    def get_type_system(self) -> str:
        return self.type_system
    
    def set_punch_name_en(self, new_punch_name_en: str) -> None:
        self.punch_name_en = new_punch_name_en

    def get_punch_name_en(self) -> str:
        return self.punch_name_en
    
    def set_punch_name_ua(self, new_punch_name_ua: str) -> None:
        self.punch_name_ua = new_punch_name_ua

    def get_punch_name_ua(self) -> str:
        return self.punch_name_ua
    
    def set_shape_name_ua(self, new_shape_name_ua: str) -> None:
        if new_shape_name_ua in shape_name_ua_list:
            self.shape_name_ua = new_shape_name_ua
        else:
            print("Error shape_name_ua")
    
    def get_shape_name_ua(self) -> str:
        name = self.shape_name_ua
        return name

    def set_station(self) -> None:
        if self.type_system == 'Standart' and self.punch_name_ua == 'Вставка пуансона' and 0.8 < self.shape['circumscribed_circle'] < 6.01:
            self.station = 'SOA'
        elif self.type_system == 'Standart' and self.punch_name_ua == 'Вставка пуансона' and 6.01 < self.shape['circumscribed_circle'] < 10.5:
            self.station = 'SOB'
        elif self.type_system == 'Standart' and self.punch_name_ua == 'Пуансон' and 0.8 < self.shape['circumscribed_circle'] < 30.01:
            self.station = 'S1'
        elif self.type_system == 'Standart' and self.punch_name_ua == 'Пуансон' and 30.01 < self.shape['circumscribed_circle'] < 40.01:
            self.station = 'S2A'
        elif self.type_system == 'Standart' and self.punch_name_ua == 'Пуансон' and 40.01 < self.shape['circumscribed_circle'] < 50.81:
            self.station = 'S3B'
        elif self.type_system == 'Standart' and self.punch_name_ua == 'Пуансон' and 50.81 < self.shape['circumscribed_circle'] < 60.0:
            self.station = 'S4C'    
        elif self.type_system == 'Standart' and self.punch_name_ua == 'Пуансон' and 60.1 < self.shape['circumscribed_circle'] < 76.3:
            self.station = 'S5D' 
    
    def get_station(self) -> str:
        return self.station

    def set_shape(
            self,       
            radius: float = 0.0,  
            a: float = 0.0,
            b: float = 0.0,
            ) -> None:
        new_shape = dict
        if self.get_shape_name_ua == 'коло' and radius > 0.0 and a == 0.0 and b == 0.0:
            new_shape = {
                'name': "round",
                'code': "R",
                'radius': radius,
                'circumscribed_circle': radius,
            }
        elif self.get_shape_name_ua == 'прямокутник' and radius == 0.0 and a > 0 and b > 0:
            print('Створюємо прамокутник')
            new_shape = {
                'name': "rectangle",
                'code': "RE",
                'A': a,
                'B': b,
                'circumscribed_circle': Shape_Standart.rectangle(a, b),
            }
        elif self.get_shape_name_ua == 'квадрат' and a != 0:
            print('Створюємо квадрат')
            new_shape = {
                'name': "square",
                'code': "SQ",
                'A': a,
                'circumscribed_circle': Shape_Standart.rectangle(a),
            }
        else:
            print('Error in method set_shape')

        self.shape = new_shape

    def get_shape(self) -> dict:
        return self.shape
    
    def set_purchase_price(self, new_purchase_price: float) -> None:
        self.purchase_price = new_purchase_price

    def get_purchse_price(self) -> float:
        return self.purchase_price

    def set_selling_price(self, new_selling_price: str) -> None:
        self.set_selling_price = new_selling_price
    
    def get_selling_price(self) -> float:
        return self.selling_price
   
p1 = Punch()

p1.set_punch_name_en("Punch insert")
p1.set_punch_name_ua("Вставка пуансона")
p1.set_shape_name_ua('квадрат')
print(p1.punch_name_en)
print(p1.punch_name_en)
print(p1.punch_name_en)
