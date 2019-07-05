# Python program to illustrate 
# nested functions 
def outerFunction(text): 
    def innerFunction(): 
        print(text) 
    innerFunction() 

outerFunction('Hey!') 
