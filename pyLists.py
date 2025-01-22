myListie = ["apple", "cherry", "banana", "lemon", "orange"]
print(myListie)
print(len(myListie))
difflist = [11, 718, "Wowowow", False, -273.15, 75 - 2j, "bread"]
print(len(difflist))
thisnewlist = list(["apple", "juice", "so_delicious"])
print(thisnewlist)
those_his_new_list = list(("pinapple", "pen", "pineapplepen", "applepen"))
print(those_his_new_list)
those_his_new_list.append("pineapplepenapplepen")
print(those_his_new_list)
#  List is a collection which is ordered 
#  and changeable. Allows duplicate members.
#  Tuple is a collection which is ordered
#  and unchangeable. Allows duplicate members.
#  Set is a collection which is unordered, 
#  unchangeable*, and unindexed. No duplicate members.
#  Dictionary is a collection which is ordered**
#  and changeable. No duplicate members.
print(those_his_new_list[1])
print(myListie[-3])
print(myListie[2:4])
print(myListie[:3])
print(myListie[2:])
print(myListie[-5:-1])
if "orange" in myListie:
    print("Oh, YES! There is some orange in my listie")

myListie[0] = "blueberry"
myListie[1] = "mango"

print(myListie)

myListie[0:2] = ["apple", "cherry"]
# if there is my listie again like it was doesn't changed
print(myListie)
myListie[3:4] = ["blackcurrant", "grape", "lime"]
print(myListie)
myListie[1:5] = ["big_pineapple"]
print(myListie)
myListie.insert(3, "big_watermelon")
myListie.insert(-1, "melon")
print(myListie)


##########################################################

fruits = ["apple", "banana"]
fruits.append("orange")
fruits.insert(-1, "cherry")
print(fruits)
tropicals = ["mango", "pineapple", "papaya"]
fruits.extend(tropicals)
print(fruits)
#you can also add any iterable object (tuples, sets, dictionaries etc.)
newfr = ("grapefruit", "avocado", "coconut")
fruits.extend(newfr)
print(fruits)
