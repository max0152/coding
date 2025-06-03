class Animal:
    name = ''
    species = ''
    age = 0
    def __init__(self,name, species, age):
        self.name = name
        self.species = species
        self.age = age
    def __str__(self):
        return f"имя {self.name} \nразновидность {self.species} \nвозраст {self.age}"
        
cat = Animal("barsik", "manchkin", 4)
print(cat)
