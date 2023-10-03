# list List Comprehension synatax used to ease creation of list
my_list =[i for i in range(1,20)]
print(my_list)

#lambda function can have any no of parameters but one statemnt 
a = lambda x,y :x+y
print(a(2,3))

#difference between / and //
print(5//2)
print(5/2)

# swap case

string= "geeks"
string.swapcase


my = {i:1+7 for i in range(1,10)}

print(my)



import numpy as np
my_list = [2,4,6,8,10]
my_array = np.array(my_list)
# printing my_array
print(my_array)
# printing the type of my_array
print(type(my_array))

rollNumbers =[122,233,353,456]
names = ['alex','bob','can', 'don'] 
NewDictionary={ i:j for (i,j) in zip (rollNumbers,names)}
print(NewDictionary)

Fruits = {'a': "Apple", 'b': "Banana", 'c': "Carrot"}
key_to_lookup = '3'

if key_to_lookup in Fruits:
    print("Key exists")
else:
    print("Key does not exist")

dict = {}
dict['1'] = 'apple'
dict['3'] = 'orange'
dict['2'] = 'pango'

lst = dict.keys()

# Sorted by key
print("Sorted by key: ", sorted(lst))


