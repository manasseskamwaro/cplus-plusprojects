# def greet(name,dept):
#     print(f"Hi {name}")
#     print(f"Are you from {dept} department")
#
# greet("jny","CS")
# positional arguments
# def greet(name,dept):
#     print(f"Hi {name}")
#     print(f"Are you from {dept} department")
#
# greet(dept='CS',name="jenny")
# keyword argument
# default = greet(name,ssubject,dept=cs)
# def add(*numbers):
    # c=0
    # for i in numbers:
        # c=c+i
    # print(f"Sum is {c}")
# add(5,7,9)
def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
info_person(name="ram",age="30",dept="CSE")
info_person(name="shyam",dept="CSE")