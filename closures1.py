# Python program to illustrate 
# closures 
def outerFunction(text): 
    def innerFunction(): 
        print(text) 
    return innerFunction # Note we are returning function WITHOUT parenthesis 

myFunction = outerFunction('Hey!') 
myFunction()
