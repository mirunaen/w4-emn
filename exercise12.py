#A program made to calculate cuantities
cuantity= float(input("Enter a  cuantity: "))
if cuantity !=0:
  if cuantity>=0:
    a= int(cuantity/500)
    rest= float(cuantity%500)
    if rest>=0:
      b=int(rest/200)
      rest=float(rest%200)
      if rest>=0:
       c=int(rest/100)
       rest=float(rest%100)
       if rest>0:
         d=int(rest/50)
         rest=float(rest%50)
         if rest>0:
          e=int(rest/20)
          rest=float(rest%20)
          if rest>0:
            e=int(rest/20)
            rest=float(rest%20)
            if rest>0:
              f=int(rest/10)
              rest=float(rest%10)
              if rest>0:
                g=int(rest/5)
                rest=float(rest%5)
                if rest>0:
                  j=int(rest/2)
                  rest=float(rest%2)
                  if rest>0:
                    h=int(rest/1)
                    rest=float(rest%1)
                    if rest>0:
                      i=int(rest/0.5)
                      rest=float(rest%0.5)
                      if rest>0:
                        k=int(rest/0.2)
                        rest=float(rest%0.2)
                        if rest>0:
                          L=int(rest/0.1)
                          rest=float(rest%0.1)
                          if rest>0:
                            m=int(rest/0.05)
                            rest=float(rest%0.05)
                            if rest>0:
                              G=int(rest/0.02)
                              rest=float(rest%0.02)
                              if rest>0:
                                H=int(rest/0.01)
                                rest=float(rest%0.01)


if a>0:
  print("500$: ",a)
if b>0:
  print("200$: ",b)
if c>0:
  print("100$: ",c)
if d>0:
  print("50$: ",d)
if e>0:
  print("20$: ",e)
if f>0:
  print("10$: ",f)
if g>0:
  print("5$: ",g)
if j>0:
  print("2$: ",j)
if h>0:
  print("1$: ",h)
if i>0:
  print("0.5$: ",i)
if k>0:
  print("0.2$: ",k)
if L>0:
  print("0.1$: "L)
if m>0:
  print("0.05$: ",m)
if G>0:
  print("0.02$: ",G)
if H>0:
  print("0.01$: ",H)

          

          
          

      
                            
        
