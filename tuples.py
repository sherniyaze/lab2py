thistuple = ("apple", "banana", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
thistuple = ("apple",)
print(type(thistuple))

#they not added comma and its not the tuple

thistuple = ("apple")
print(type(thistuple))

tuple_forever = ("apple", 1, False, 0, 1j)
print(tuple_forever)
print(type(tuple_forever))
newest = tuple(("apple", "banana","cherry"))
print(newest)

print(tuple_forever[1])
print(tuple_forever[-2])
tupleeer = ("apple", "secondelement", 3, "banana", 5, 6.0+0j, "seventh",8.0)

print(tupleeer[2:5])
print(tupleeer[:5])
print(tupleeer[2:])
print(tupleeer[-4:-1])
if "apple" in tupleeer:
    print("Yes, there is apple in my tuple sir")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
#i will not show del because of compilation error
x = list(tupleeer)
x[0] = "kiwi"
print(x)
myNEW = ("apple","banana","cherry")
(green, blue, yellow) = myNEW
print(green)
print(blue)
print(yellow)
for x in tupleeer:
    print(x)

for i in range(len(tupleeer)):
    print(tupleeer[i])

i = 0
while i < len(tupleeer):
    print(tupleeer[i])
    i = i + 1

tuplik1 = ("wow", "good job", "pl")
tuplik2 = (1,2,3)
tuplik3 = tuplik1 + tuplik2
print(tuplik3)

print(tuplik3 * 2)
