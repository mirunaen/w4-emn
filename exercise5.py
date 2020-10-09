name1=str(input("Enter a name:"))
name2=str(input("Enter another name:"))
age1=int(input("Enter an age:"))
age2=int(input("Enter another age:"))

if age1<age2:
  print(name1," is younger than",name2)
elif age2>age1:
  print(name2," is older than",name1)
else:
  print(name1,"and",name2,"are the same age")
