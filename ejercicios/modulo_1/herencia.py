class Animal:
    def __init__(self,edad):
        self.edad = edad
        
class Ave(Animal):
    def __init__(self, edad):
        super().__init__(edad)