# def format_name(f_name,l_name):
#     formatted_f_name=f_name.title()
#     formatted_l_name=l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"
#
#
# print(format_name("jenny","KHATRI"))
# import statistics
# def mean_median_mode(list1):
#     return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]
#
#
# print(mean_median_mode([3,5,45,3,2,1,89]))

def add(a,b):
    if a==0 & b==0:
        return
    else:
        return a+b

var1=int(input("Enter first variable:\n"))
var2=int(input("Enter second variable:\n"))
result=add(var1,var2)
print(result)