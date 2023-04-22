class Invoice():
    def __init__(self, 
                 date=None, 
                 name_company:str=None, 
                 products: list=None, 
                 exchange_rates: float=None,
                 discount_percent:int=1) -> None:
        self.date = date
        self.name_company = name_company
        self.products = products
        self.exchange_rates = exchange_rates
        self.discount_percent = discount_percent
    
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

    def get_exchange_rates(self) -> str:
        return self.exchange_rates
    
    def set_discount_percent(self, new_discount_percent) -> None:
        self.discount_percent = new_discount_percent
    
