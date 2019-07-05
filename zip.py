sno=[1,2,3]
sname=['a','b','c']
marks=[95,90,88]
mapped=list(zip(sno,sname,marks))

print(mapped)

sno1,sname2,marks3=zip(*mapped)
print(sno1)
print(sname2)
print(marks3)

for a,b,c in mapped:
    print("roll number:",a,"name:",b,"marks:",c)
