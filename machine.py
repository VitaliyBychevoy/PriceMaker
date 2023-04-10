class Machine:
    def __init__(self, model: str=None, style_stripper: str=None, length: float=None):
        self.model = model
        self.style_stripper = style_stripper
        self.length = length
    
    def set_model(self, new_model) -> None:
        self.model = new_model
    
    def get_model(self) -> str:
        return self.model
    
    def set_style_stripper(self, style) -> None:
        self.style_stipper = style

    def get_style_stripper(self) -> str:
        return self.style_stipper