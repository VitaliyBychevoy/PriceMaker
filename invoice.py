class Invoice():
    def __init__(self, 
                 date: str=None, 
                 name_company:str=None, 
                 products: list=None, 
                 exchange_rates: float=None,
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
        self.date = date
        self.name_company = name_company
        self.products = products
        self.exchange_rates = exchange_rates
        self.discount_percent = discount_percent
        self.total_currency = total_currency
        self.total_UAH = total_UAH
        self.vat_currency = vat_currency
        self.vat_UAH = vat_UAH
        self.discount_currency = discount_currency
        self.discount_UAH = discount_UAH
        self.total_vat_discount_currency = total_vat_discount_currency
        self.total_vat_discount_UAH = total_vat_discount_UAH
    
    def set_date(self,new_date) -> None:
        self.date = new_date

    def get_date(self) -> str:
        return self.date
    
    def set_name_company(self, new_name_company) -> None:
        self.name_company = new_name_company
    
    def get_name_company(self) -> str:
        return self.name_company
    
    def set_products(self, product_list: list) -> None:
        self.products = product_list

    def get_products(self) -> list:
        return self.products
    
    def set_exchange_rates(self, new_exchange_rates: str) -> None:
        self.exchange_rates = new_exchange_rates

    def get_exchange_rates(self) -> float:
        return self.exchange_rates
    
    def set_discount_percent(self, new_discount_percent) -> None:
        self.discount_percent = new_discount_percent
    
    def set_total_currency(self, products: list) -> None:
        new_total_currency = 0.0
        for product in products:
            new_total_currency += product["price_currency"]
        self.total_currency = new_total_currency
    
    def get_total_currency(self) -> float:
        return self.total_currency
    
    def set_total_UAH(self) -> None:
        self.total_UAH = (self.get_exchange_rates() * self.get_total_currency())
    
    def get_total_UAH(self) -> float:
        return self.total_UAH
    
    def set_vat_currensy(self) -> None:
        self.vat_currency = self.total_currency() * 0.2
    
    def get_vat_currensy(self) -> float:
        return self.vat_currency
    
    def set_vat_UAH(self) -> None:
        self.vat_UAH = self.get_total_UAH() * 0.2
    
    def get_vat_UAH(self) -> float:
        return self.vat_UAH

    def set_total_vat_discount_currency(self) -> None:
        self.total_vat_discount_currency = self.get_total_currency() - self.get_vat_currensy()
    
    def get_total_vat_discount_currency(self) -> float:
        return self.total_vat_discount_currency

    def set_total_vat_discount_UAH(self) -> None:
        self.total_vat_discount_UAH = self.get_exchange_rates() * self.get_total_vat_discount_currency()
    
    def get_total_vat_discount_UAH(self) -> float:
        return self.total_vat_discount_UAH
