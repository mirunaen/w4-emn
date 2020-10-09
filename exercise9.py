x_axis=float(input("Enter a x_axis point:"))
if x_axis==0:
  x_axis=float(input("The values are not valid"))
y_axis=float(input("Enter a y_axis point:"))
if y_axis==0:
  y_axis=float(input("The values are not valid"))

if x_axis>0 and y_axis>0:
  print("The point lies in the 1st quadrant")
elif x_axis<0 and y_axis>0:
  print("The point lies in the 2nd  quadrant")
elif x_axis<0 and y_axis<0:
  print("The point lies in the 3rd  quadrant")
else:
  print("The point lies in the 4th  quadrant")
