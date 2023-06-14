#name=input("what is your name")
#print("hello" + name)

#old_age=input("enter your old age:")
#new_age=int(old_age)+2                             #IF WE DONT PUT INT IT WILL PRINT OLDAGE AS STR#
#print(new_age)

#first=input("enter first number:")                           #SUM OF NUMBER#
#second=input("enter second number:")
#sum=int(first)+int(second)
#print(sum)

name="Tony Stark"
#print(name.upper())                                               #WHEN WE WANT IN UPPERCASE#
#print(name.lower())                                          #WHEN WE WANT IN LOWECASE#
#print(name.find('S'))                                         #WHEN WE HAVE TO FIND LETTER#
#print(name.find('stark'))
#print(name.replace("Stark", "Ironman"))                  #replace#

#i=5
#i=i+2
#i+=2
#i*=2
#result=2+3*5
#print(result)

#_________comparsion operator________________#
#print(3>2)
#print(5<2)
#print(7==7)
#print(3!=3)

#_________logical operator____________#
#print(2>3 or 2>1)
#print(3>2 and 1>2)



#_________if_elif_else________#
#age=19
#if age>=18:
    #print("adult")
#elif age<18 and age>3:
    #print("student")
#else:
    #print("child")


#________range____________#
#num=range(5)
#print(num)


#__________while_________#
#i=1
#while i<=5:
    #print(i*"*")
    #i+=1

#_______for________#
#for item in range(5):
     #print (item)

#_______list________#
marks=[95,98,96]
#print(marks[1])                   #indexing
#print(marks[1:3])

#for score in marks:
    #print(score)

#marks.append(99)             #add 99 at end#
#print(marks)

#marks.insert(0,99)            #first index no then what to insert that no#
#print(marks)

#print(95 in marks)            #does 95 exist in list#

#print(len(marks))

#marks.clear()                 #empty list will be printed marks will be cleared#
#print(marks)

#_____break_continue_____#
#stud=["ram","shyam","radha","kisan"]
#for student in stud:
    #if student=="radha":
        #break;                         #break
    #print(student)

#stud=["ram","shyam","radha","kisan"]
#for student in stud:
    #if student=="kisan":
        #continue;                       #continue
    #print(student)




#____________tuple_________#
#marks=(94,95,98,97,97)
#print(marks.count(97))                 #count
#print(marks.index(95))                 #index



#___________sets__________#
#marks={95,94,97,97,97}
#print(marks)                  #97 will print only 1 time and indexing does not exist#

#for score in marks:
   # print(score)


#___________dictionary________#
marks={"english":95,"chem":85}
#print(marks["chem"])

#marks["phy"]=75;            #add phy marks
#print(marks)

marks["phy"]=99;
print(marks)                #change phy marks


