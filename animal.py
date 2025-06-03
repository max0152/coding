class Animal:
    name = ''
    species = ''
    age = 0
    
    def __init__(self,name, species, age):
        self.name = name
        self.species = species
        self.age = age
        
    def display_info(self):
        return f"имя: {self.name} \nразновидность: {self.species} \nвозраст: {self.age}"

class shelter:  
    
    def  __init__(self):
        self.animals = []
        
    def add_animal(self, animal):
        self.animals.append(animal)
        
cat = Animal("barsik", "manchkin", 4)
print(cat.display_info())
