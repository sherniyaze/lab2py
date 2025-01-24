fruitslist = ["dragonfruit", "banana", "apple", "cherry"]
fruitslist.sort()
print(fruitslist)

numbers = [10, 20, 5, 30, 15, 45]
numbers.sort()
print(numbers)

numbers.sort(reverse = True)
print(numbers)

fruitslist.sort(reverse = True)
print(fruitslist)


newnumbers = [100, 35, 60, 75, 90]
numbers.extend(newnumbers)
# print(numbers)
# numbers.sort()
# print(numbers)


def myfunction(n):
    return abs(n-50)

numbers.sort(key = myfunction)
print(numbers)


def myinterestingfunc(n):
    if n > 75 or n < 25:
        return abs(50 - n)
    else:
        return abs(50 - n*2)

numbers.sort(key=myinterestingfunc)
print(numbers)

#now check to case sensitivity

theirlist = ["banana", "Orange", "Kiwi", "cherry", "BANANA"]
theirlist.sort()
print(theirlist)

#in first situation BANANA Kiwi and after
#  that was Orange

theirlist[1] = "ORANGE"
theirlist.sort()
print(theirlist)

#now it is changed because of rewriting 
# Orange as ORANGE

# ['BANANA', 'Kiwi', 'Orange', 'banana', 'cherry']        
# ['BANANA', 'ORANGE', 'Orange', 'banana', 'cherry']  

theirlist.sort(key=str.lower)
print(theirlist) 

# no matter upper or lower, it will sort alphabetically

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

    