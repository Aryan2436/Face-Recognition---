str="abhay chutiya hai"
length=len(str)
print(length)

str1="welcome to python"
search=str1.find("p")
print(search) 

str2=input("enter a string:")
if len(str2) < 2:
    print("empty string")
else:
    s1=str2[:2]+str2[-2:]
    print(s1)


