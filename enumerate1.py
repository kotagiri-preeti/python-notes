n=int(input("enter no.of students"))
list1=[]
for i in range(n):
    name=input("enter student name")
    course=input("enter course of the student")
    yop=int(input("enter student yop"))
    tup=(name,course,yop)
    list1.append(tup)
print("all the student details")
for i,j in enumerate(list1,1):
    print(i,":",j)
    
