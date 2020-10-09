sec=int(input("Enter num of seconds:"))
min=0
hours=0
if sec>=60:
    min=int(sec/60)
    sec=int(sec%60)
    if min>=60:
        hours=int(min/60)
        min=int(min%60)
    else:
        min=min
elif sec<60:
    sec=sec
print(hours,":",min,":",sec)