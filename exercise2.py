a, b, c, d = 5, 3, 20, 20
c -= (a + 1) / b – 3 + a % b
#to 20 we subtract (5+1)/ 3-3 + 5 % 3(the rest is 2)
#(a+1)=6
d -= (a + 1) / (b + 3 - 4 * a) % b
#(b+3-4*a)=-14
#(b+3-4*a)%b=1
#(a+1)/(b+3-4*a)%b=2.57
#To 20 we substract (5+1)/(3+3-4*5)%3(rest 1)
print("c:", c)
print("d:", d)
