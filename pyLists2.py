ohyesmynewlist = ["apple", "banana", "cherry"]
ohyesmynewlist.remove("banana")
print(ohyesmynewlist)

ohyesmynewlist.append("coconut")
ohyesmynewlist.insert(0,"banana")
ohyesmynewlist.append("banana")
print(ohyesmynewlist)

ohyesmynewlist.remove("banana")
print(ohyesmynewlist)

ohyesmynewlist.pop(1)
print(ohyesmynewlist)



### now check this 
### inserted before our last element (-1) aka "banana" 
### or this new element is our new pre-last element
### but when we pop in index (-1) we pop not a CHECK
### we pop our last element "banana"

ohyesmynewlist.insert(-1, "CHECK")
print(ohyesmynewlist)

ohyesmynewlist.pop(-1)
print(ohyesmynewlist)

CHECKERLIST = ["cobalt", "bmw", "audi", "aston martin", "porsche"]
CHECKERLIST.pop()
print(CHECKERLIST)

CHECKERLIST.append("porsche")
print(CHECKERLIST)

CHECKERLIST.pop(-1)
print(CHECKERLIST)

### there we can see that pop(-1) and pop() 
# are equal and both of them removes the last
# element

del CHECKERLIST[0]
print(CHECKERLIST)

del CHECKERLIST
# print(CHECKERLIST) <----- shows error

#the result of this execution shows that
#  del CHECKERLIST really deleted it and 
#  there are error 

SONEWCHECKER = ["toyota", "lexus", "kia", "honda"]
SONEWCHECKER.clear()
print(SONEWCHECKER)

#the results really shows us [] as SONEWCHECKER



#   NOOOOOOOOOOWWWWWWWWW ABOOOOOOUUUUUTTTTT LOOOOPS
#   IIIIIIIIIIIIIIINNNN  LIIIIISSSTTTTTSSSSSSSS

thislistie = ["apple", "banana", "cherry"]
for x in thislistie:
    print(x)

#   btw without scopes and quotes

for i in range(len(thislistie)):
    print(thislistie[i])

i = 0
while i < len(thislistie):
    print(thislistie[i])
    i = i + 1

[print(x) for x in thislistie]



###################################################################
#############################################################

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

NEWlist = [x for x in fruits if "a" in x]

print(NEWlist)

numberslist = [x for x in range(11)]
print(numberslist)

oddnumberslist = [x for x in numberslist if x%2==1]
print(oddnumberslist)

evennumberslist = [x for x in numberslist if x%2==0]
print(evennumberslist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

#######################################################
# there numberslist = [x for x in range(11)] is NOT
# the same as newlist = [x for x in range(10) if x]
# maybe because when x = 0 it might be equal to FALSE
# for python in boolean
########################################################

newlist = [x.upper() for x in fruits]
print(newlist)

# also we can change everything to 1 thing
newlist = ['jellyfish' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# тут короче говоря для меня такая заметка, 
# выведи х если: 
#   он не равен банану
# иначе: 
#   выведи апельсин
# so new element in newlist aka x will be the same fruit
# but if it is banana we change it to orange
# х выведется без изменений если != банану
# иначе выведется апельсин
# now practice it

animelist = ["tokyo ghoul", "attack on titan", "re:zero", "cowboy bebop", "one piece", "solo leveling"]
myfavourite = [x if x == "solo leveling" else "missed chance" for x in animelist]
print(myfavourite)

myfavourite = [x for x in animelist if x == "solo leveling"]
print(myfavourite)