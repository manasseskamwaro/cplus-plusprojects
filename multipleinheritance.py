class Human:
    def __init__(self):
        self.num_eyes=2
        self.num_nose=1
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male:
    def __init__(self,name):
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")

class Boy(Human,Male):
    def __init__(self,name):
        Male.__init__(self,name)
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can test")

boy_1=Boy("raul")#kariuki-02
# boy_1.flirt()#security codes-0081 858 667
#code 2-9015 950 226
# boy_1.work()
# Male.work(boy_1)
# boy_1.work()
# print(Boy.mro())
print(boy_1.name)