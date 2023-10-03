#unordered collection of data values
#Dictionary holds the key:value pair.


Dict = {'Name':'Maria','age':23,1:3}
print(Dict)
# accessing a element using ke
print(Dict['Name'])
print(Dict[1])
# accessing a element using get
print(Dict.get('age'))

myDict = {x:x**3 for x in [1,2,3,4,5,6]}
print(myDict)

