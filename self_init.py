class Instructor:
    def __init__(self,ins_name,address):
        self.name=ins_name
        self.address=address
        self.followers=0

instructor_1=Instructor("manasse","kenya")
instructor_2=Instructor("rish","canada")
print(instructor_1.name)
print(instructor_1.address)
print(instructor_2.name)
print(instructor_2.address)