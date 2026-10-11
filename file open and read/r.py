f=open("ram.txt","r")
name=f.read()
f=open("ram.txt","r+")
data=f.read()
f.write("ram eats mango.")
print(data)

f.close()