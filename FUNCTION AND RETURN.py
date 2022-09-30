#PYTHON FUNCTION AND RETURN FUNCTION.def is a keyword meaning defintion.

def userdefined(a,b): # a user defined function, the variables inside a function is called parameters.
    
    return a+b # by default a function value is none if no parameter were given .and return function makes the given value ultimatly the functions value.

# so  in this case 5+9  14 is returned so the value of userdefined is =14 now.


print(userdefined(5,9)) # this variable is called arguments also called actual parameter.

# here we called the function inside print function so the value of the function to display.


#FUNCTION CALLING WITHOUT RETURN FUNCTION.

def callme(d,c):
    var  =  d / c
    print("\n",var)


callme(34,5)#,regular function calling.

print(callme(25,5)) # in this case we didint used the return function to give the callme function the value of the car variable, so the function value by defualt is none.
    
    
    
    
