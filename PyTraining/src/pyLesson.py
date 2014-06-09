#print "Hello interbutts"

#wage = 2000
#groceries = 400
#rent = 200
#whatever = 600

#summary = wage -(groceries + rent + whatever)
#print summary
#

#name = "Lando"
#status = "Butt"
#age = raw_input("How old is he?")

#print "His name is "+name+" and he is a "+status+" who is "+age
#if int(age) == 15:
#    print "lol old"

#else:
#    for i in range(0,int(age)):
#        print "what."

#create list, convert to dict, write to file
pet_list = [["1", "dog"], ["2", "cat"], ["3", "Guinea Pig"]]
print pet_list
jk = pet_list.pop()
print pet_list
new_dict = dict(pet_list)

f = open("stuff.txt", "w")
xyz = new_dict.values()
str(xyz)
f.write("%s" % xyz)
f.close()
#cleanup
import os
os.remove("stuff.txt")





