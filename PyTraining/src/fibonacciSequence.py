x = raw_input("Please enter a number to calculate the fibonacci sequence to: ")
x = int(x)

def getFib(n):
    #num1,num2 = 1,1
    #for i in range(n-1):
    #    num1,num2 = num2,num1+num2
    #return num1
    if n <= 1:
        return n
    else:
        return(getFib(n-1) + getFib(n-2))


if x > 0:
    for i in range(x):
        print getFib(i)

else:
    print "out of bounds"


#I got to say, I am not a big fan of math.  Just for the record.