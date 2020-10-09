a = 3
b = 8
c = 3.0
r = a == 0
s = a != 0
t = a <= b
u = b >= a
v = b > a
w = b < a
x = c == 3.0
print("r:", r)
#a is not equal to 0 but to 3 so it´s false(it´s a boolean)
print("s:", s)
#It´s a booleand and it says that if a is not equal to 0 then it is true;as a is 3 then it true.
print("t:", t)
#If a is smaller or equal to b then return true else is false.In this case a<b so it´s true.
print("u:", u)
#If b is greater than or equal to b then return true else is false,in this case it´s true. 
print("v:", v)
#If b is greater than a (a=3 and b=8 so it´s true) then return true.
print("w:", w)
#As b is not smaller than a it will return false because the condition is not met.
print("x:", x)
#Returns true because c is equal to 3.0