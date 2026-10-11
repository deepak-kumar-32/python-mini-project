str1="Deepak kumar"
print(str1.find("k"))
print(str1.find("a"))
print(str1.find("u"))
print(str1.find("m"))
print(str1.find("x"))
print(str1.find("y"))   
print(str1.find("a",5)) #find "a" after index 5     
print(str1.find("u",5)) #find "u" after index 5
print("-----------------------------")
print(str1.rfind("m"))#find "m" from right
print(str1.rfind("a"))#find "a" from right  (last se jo pahle aayega uska index dega aur index left se count karega jaisa hota tha waisa hi hoga )
print(str1.rfind("k",5))#find "k" from right after index 5  
print(str1.rfind("x"))
print("-----------------------------")
print(str1.index("k")) #find "k" and if not found then it will give error
print(str1.index("a")) #find "a" and if not found then it will give error
print(str1.index("u")) #find "u" and if not found then it will give error
print(str1.index("m")) #find "m" and if not found then it will give error
# print(str1.index("x")) #find "x" and if not found then it will give error
print("-----------------------------")
print(str1.rindex("k")) #find "k" and if not found then it will give error
print(str1.rindex("a")) #find "a" and if not found then it will give error
print(str1.rindex("u")) #find "u" and if not found then it will give error  