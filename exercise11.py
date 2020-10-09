
a=int(input("Enter a year:"))
r1=a %4
r2=a %100
r3=a%400
if r1!=0:
  print("This year",a,"was not a leap year")
elif r2==0:
  if r3==0:
   print("This year",a,"is a leap year")
  else:
    print("This year",a,"was not a leap year")
elif r1==0:
  print("This year",a,"is a leap year")