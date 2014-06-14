n = raw_input("How many decimal places of pi do you want?\n")
pi = "3."
pi38 = "14159265358979323846264338327950288419"
if int(n) > 0:
    if int(n) <= 38:
        print pi + pi38[:int(n)]

else:
    print "Out of bounds"

#Elected to not calculate pi every single time as this would cause a significant delay.
#Since Pi doesn't change and the project specifies to have a limit imposed on "n", so I hardcoded Pi in.
#if necessary I can revise this to actually calculate pi, but I would rather have that as a call to another program
