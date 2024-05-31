class Instructor:
    followers=0
    def __init__(self,name,address):
        self.name=name
        self.address=address
        # self.followers=0

    def display(self,subject_name):
        print(f"Hi,I am {self.name} and I teach {subject_name}")
    def update_follower(self,follower_name):
        self.followers += 1

instructor_1=Instructor("manasse","kenya")
print(instructor_1.name)
instructor_1.display("Python")
instructor_1.update_follower("rish")
print(instructor_1.followers)