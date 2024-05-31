# key value pair
# dict_name={key:value}
phone_no = {
    'Ram':1234,
    'Shyam':3456,
    'Mohan':1111
}
# print(phone_no['Shyam'])
# mutable integers,immutable strings

# phone_no = dict([('Ram',1234),('Shyam',3456),('Mohan',1111)])
# print(phone_no)
phone_no['Mohan']=9999
phone_no['Madhav']={1111,2222,3333}
phone_no['Shyam']={'Shyam_home':5555,'Shyam_work':4444}
print(phone_no['Shyam']['Shyam_work'])
print(phone_no.get('Ram'))
del phone_no['Ram']
# or
print(phone_no.pop('Shyam'))
print(phone_no.keys())
print(phone_no.values())
print(phone_no.items())
for i in phone_no.items():
    print(i)
    print(phone_no[i])
phone_no2 = phone_no.copy()
print(phone_no2)
print(len(phone_no))
