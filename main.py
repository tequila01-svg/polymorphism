class Cow:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def info(self):
        print(f"i am a cow, my name is {self.name} i am {self.age } years old")
        
    def make_sound(self):
        print("moo")
        
        
class Sheep:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def info(self):
        print(f"i am a sheep, my name is {self.name} i am {self.age } years old")
        
    def make_sound(self):
        print("bleat")
        
cow1=Cow("freedy", 3)
sheep1=Sheep("gold", 4)

for animal in (cow1,sheep1):
 animal.make_sound()
 animal.info()