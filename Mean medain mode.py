### MEAN,MEDIAN,MODE ###


###MEAN## #AVERAGE#

list = [1,23,45,66,77,43,22,43] # if we use ["12,34,56"] like this its a string 0 index

print(list[7])
print(type(list))

x = len(list) # the len().. function returns the number of items in an object in this case its a list.

sum = list[0]+list[1]+list[2]+list[3]+list[4]+list[5]+list[6]+list[7] #mean formuala
mean = sum//x
print('mean =',mean)
print(sum)



##MEDIAN## ..MIDDLE VALUE IF THE SEQUENCE IS EVEN NUMBER BOTH MIDDLE VALUE AND DEVIDE BY 2 (a+b)/2##

list2 = [12,34,5,6,8,9]
y = len(list2)
print("the number of elements in the list =",y)

if y%2==0: # if the number of elements in the list is an even number..
    Z = y//2
    print("Z=",Z)
    z = Z-1
    print("middle value=",list2[z])
    print('nearest value to the middle value =',list2[z+1])
    median = ((list2[z]+list2[z+1])/2) #median formula USING PEDMAS- PARENTHESIS(1),,EXPONENT(2),,DIVISION(3),,MULTIPLICATION(4),,ADDITION(5),,SUBSCTRACTION(6)
    print("medianc=",median)
    
if y%2!=0: # if number of elements in the list is an odd number..
    N = len(list2)
    N = N-1
    R = N//2
    R = R+1
    print("median =",list2[R-1])

##MODE## RECURRING NUMBER FROM  THE SEQUENCE IS CALLED MODE..##
print("mode=",list2)


    

