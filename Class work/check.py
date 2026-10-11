str1=input("enter your Charactor:")
if(str1.islower()==True):
    print("charactor in lower case:")
        
   
elif(str1.isupper()==True):
    print("string in upper case")  
elif(str1.istitle()==True):
    print("string in Title  case") 
elif(str1.isalpha()==True):
    print("string in both upper and lower  case")
             
else:
    print("special charactor")    