str1="Ram is a good boy"
str2=str1.split()
print(str2)
str1="Ram is, a good boy"
str2=str1.split(",")
print(str2)
str1="Ram is a good boy"
str2=str1.split("a")      
print(str2)
print("______________________________")
str1="Ram is a good boy"
str2=str1.rsplit()
print(str2) 
print("______________________________")
str1="Ram is a good boy"
str2="-" .join(str1)
print(str2)
tuple1=tuple(str1)
print(tuple1)