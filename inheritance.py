class Human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def __init__(self,name,heart):
        self.name=name
        super().__init__(heart)
    def flirt(self):
        print("Hello,my amore")
    def work(self):
        super().work()
        print(("Ican code"))
    def display(self):
        print(f"Hi,I am {self.name} and I have {self.num_heart} heart. ")



male_1=Male("Aqash",1)
male_1.flirt()
male_1.work()
male_1.display()
