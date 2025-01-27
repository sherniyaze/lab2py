mysushiset = {"fish", "rice","sauce"}
print(mysushiset)
mysushiset = {"fish", "rice","sauce", "fish", "rice"}
myinvalidsushiset =  {0, False, True, 1, 235j -3.0, "raw fish", "chicken"}
print(myinvalidsushiset)
print(len(myinvalidsushiset))
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(type(myinvalidsushiset))
thisnewset = set(("apple","banana","cherry"))
print(thisnewset)
for x in thisnewset:
    print(x)

print("fish" in mysushiset)
print("raw fish" not in mysushiset)
print("raw fish" not in myinvalidsushiset)
wowowow = {"apple", "banana", "cherry"}
print(wowowow)
wowowow.add("orange")
print(wowowow)
owowowo = {"mango", "kiwi", "pineapple"}
wowowow.update(owowowo)
print(wowowow)
pinokkkw = ["gr", "wda", "sod"]
wowowow.update(pinokkkw)
print(wowowow)
wowowow.remove("orange")
wowowow.discard("mango")
x = wowowow.pop()
print(x)
print(wowowow)
wowowow.clear()
print(wowowow)
for x in wowowow:
    print(x)
#i forget that wowowow is clear now fu
apple = {"apple", "banana", "cherry"}
for x in apple:
    print(x)

set3 = owowowo.union(apple)
print(set3)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

set1 = {"apdfh", "asdb", "cucumber"}
set2 = {1488, 52, 332}
set3 = {"John Wick", "Selena Gomes"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)

print(myset)
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)


set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

