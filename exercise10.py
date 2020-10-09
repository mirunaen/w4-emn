salary=int(input("Enter your salary: "))
seniority=int(input("Enter your seniority: "))
if salary<500:
  if seniority>=10:
    salary=salary*1.2
    print("your salary will be:",salary)
  else:
    salary=salary*1.05
    print("your salary will be:",salary)
else:
  print("your salary will be:",salary)

