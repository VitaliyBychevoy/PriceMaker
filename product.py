from machine import Machine
from tool import Tool
from geometry import Shape


class Product:
    def __init__(self,
        machine: Machine = None,
        tool: Tool = None,
        shape: Shape = None,
        price: Price = None,
        amount: int = 0,
        ) -> None:
        self.__machine = machine
        self.__tool = tool
        self.__shape = shape
        self.__price = price
        self.__amount = amount
    
    def set_machine(self, new_machine: Machine) -> None:
        self.__machine = new_machine
    
    def get_machine(self) -> Machine:
        return self.__machine
    
    def set_tool(self, new_tool: Tool) -> None:
        self.__tool = new_tool
    
    def get_tool(self) -> Tool:
        return self.__tool

    def set_shape(self, new_shape: Shape) -> None:
        self.__shape = new_shape
    
    def get_shape(self) -> Shape:
        return self.__shape
    
    def set_amount(self, amount: int) -> None:
        self.__amount = amount
    
    def get_amount(self) -> int:
        return self.__amount
    