#reversing a string 
str ="goat"
stringlength=len(str)
slicedstr=str[stringlength::-1]
print(slicedstr)

a_string="Python Programming" 
substring1="Programming" 
substring2="Language" 
print("Check if "+a_string+" contains "+substring1+":")
print(a_string.find(substring1)) 
print("Check if "+a_string+" contains "+substring2+":")
print(a_string.find(substring2))