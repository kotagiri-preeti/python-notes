from functools import reduce
def pow(a,b):
    return a**b
list1=[3,2,1]
power=reduce(pow,list1)
print(power)
