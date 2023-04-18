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