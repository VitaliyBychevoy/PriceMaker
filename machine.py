import db_handler as db

class Machine:
    def __init__(
            self, 
            machine_name_en: str=None, 
            model_machine_en: str=None
            ) -> None:
        self.machine_name_en = machine_name_en
        self.model_machine_en = model_machine_en

    def set_machine_name_en(self, new_machine_name) -> None:
        self.machine_name_en = new_machine_name
    
    def get_machine_name_en(self) -> str:
        return self.machine_name_en
    
    def set_model_machine_en(self, new_machine_name) -> None:
        self.model_machine_en = new_machine_name

    def get_model_machine_en(self) -> str:
        return self.model_machine_en