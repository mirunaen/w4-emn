price_ticket=9
age=int(input("Enter your age:"))

if age<5:
  p=price_ticket-price_ticket*0.6
  print("Price ticket: ",p)
elif age>=5 and age<26:
  p=price_ticket-price_ticket*0.2
  print("Price ticket: ",p)
elif age>60:
  p=price_ticket-price_ticket*0.55
  print("Price ticket: ")
else:
  print("Price ticket: ",price_ticket)

