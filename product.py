from machine import Machine
from tool import Tool
from geometry import Shape
from price import Price

class Product:
    def __init__(self,
        machine: Machine = None,
        tool: Tool = None,
        shape: Shape = None,
        price: Price = None,
        amount: int = 0,
        ) -> None:
        self.machine = machine
        self.tool = tool
        self.shape = shape
        self.price = price
        self.amount = amount
    
    def set_machine(self, new_machine: Machine) -> None:
        self.machine = new_machine
    
    def get_machine(self) -> Machine:
        return self.machine
    
    def set_tool(self, new_tool: Tool) -> None:
        self.tool = new_tool
    
    def get_tool(self) -> Tool:
        return self.tool

    def set_shape(self, new_shape: Shape) -> None:
        self.shape = new_shape
    
    def get_shape(self) -> Shape:
        return self.shape
    
    def set_amount(self, amount: int) -> None:
        self.amount = amount
    
    def get_amount(self) -> int:
        return self.amount
    