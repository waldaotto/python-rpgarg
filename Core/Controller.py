from abc import ABC

class Controller(ABC):

    MODEL:type
    VIEW:any

    def __init__(self):
        pass

    def view(self):
        
        self.VIEW()

    def redirect(self):
        ...
