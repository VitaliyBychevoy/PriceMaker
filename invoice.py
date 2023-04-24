class Invoice():
    def __init__(self, 
                 date: str=None, 
                 name_company:str=None, 
                 products: list=None, 
                 rate: float=None,
                 discount_percent:int=1,
                 total_currency: float = 0.0,
                 total_UAH: float = 0.0,
                 vat_currency: float = 0.0,
                 vat_UAH: float = 0.0,
                 discount_currency: float = 0.0,
                 discount_UAH: float = 0.0,
                 total_vat_discount_currency: float = 0.0,
                 total_vat_discount_UAH: float = 0.0
                 ) -> None:
        self.__date = date
        self.__name_company = name_company
        self.__products = products
        self.__rate = rate
        self.__discount_percent = discount_percent
        self.__total_currency = total_currency
        self.__total_UAH = total_UAH
        self.__vat_currency = vat_currency
        self.__vat_UAH = vat_UAH
        self.__discount_currency = discount_currency
        self.__discount_UAH = discount_UAH
        self.__total_vat_discount_currency = total_vat_discount_currency
        self.__total_vat_discount_UAH = total_vat_discount_UAH
    
    def set_date(self,new_date) -> None:
        self.__date = new_date

    def get_date(self) -> str:
        return self.__date
    
    def set_name_company(self, new_name_company) -> None:
        self.__name_company = new_name_company
    
    def get_name_company(self) -> str:
        return self.__name_company
    
    def set_products(self, product_list: list) -> None:
        self.__products = product_list

    def get_products(self) -> list:
        return self.__products
    
    def set__rate(self, new_rate: str) -> None:
        self.__rate = new_rate

    def get_rate(self) -> float:
        return self.__rate
    
    def set_discount_percent(self, new_discount_percent) -> None:
        self.__discount_percent = new_discount_percent
    
    def get_discount_percent(self) -> float:
        return self.__discount_percent
    
    def set_total_currency(self, products: list) -> None:
        new_total_currency = 0.0
        for product in products:
            new_total_currency += product["price_currency"]
        self.__total_currency = new_total_currency
    
    def get_total_currency(self) -> float:
        return self.__total_currency
    
    def set_total_UAH(self) -> None:
        self.__total_UAH = (self.get_rate() * self.get_total_currency())
    
    def get_total_UAH(self) -> float:
        return self.__total_UAH
    
    def set_vat_currensy(self) -> None:
        self.__vat_currency = self.total_currency() * 0.2
    
    def get_vat_currensy(self) -> float:
        return self.__vat_currency
    
    def set_vat_UAH(self) -> None:
        self.__vat_UAH = self.get_total_UAH() * 0.2
    
    def get_vat_UAH(self) -> float:
        return self.__vat_UAH

    def set_discount_currency(self) -> None:
        self.__discount_currency = self.get_total_currency() + self.get_rate()
    
    def get_discount_currency(self) -> float:
        return self.__discount_currency
    
    def set_discount_UAH(self) -> None:
        self.__discount_UAH = self.get_discount_currency() * self.get_rate()
    
    def get_discount_UAH(self) -> float:
        return self.__discount_UAH

    def set_total_vat_discount_currency(self) -> None:
        self.__total_vat_discount_currency = self.get_total_currency() - self.get_vat_currensy()
    
    def get_total_vat_discount_currency(self) -> float:
        return self.__total_vat_discount_currency

    def set_total_vat_discount_UAH(self) -> None:
        self.__total_vat_discount_UAH = self.get_exchange_rates() * self.get_total_vat_discount_currency()
    
    def get_total_vat_discount_UAH(self) -> float:
        return self.__total_vat_discount_UAH
