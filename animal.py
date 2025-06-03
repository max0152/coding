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

    def show_animals(self):
        if not self.animals:
            print("Приют пуст")
        else:
            for animal in self.animals:
                print(animal.display_info())
                print()
        
shelter = shelter()
cat = Animal("barsik", "manchkin", 4)
cat = Animal("barsik", "manchkin", 4)
dog = Animal("bobik", "ovcharka", 15)
bird = Animal("kesha", "vorobey", 1)
shelter.add_animal(cat)
shelter.add_animal(dog)
shelter.add_animal(bird)
shelter.show_animals()
