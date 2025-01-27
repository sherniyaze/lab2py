fruits = ['apple','orange','cherry']
fruits.append("orange")
print(fruits)

a = ["apple","banana","cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

fruits = ['apple','banana','cherry','orange']
fruits.clear()
print(fruits)

x = fruits.copy()
print(x)

fruits = ['apple','banana','cherry']
x = fruits.count("cherry")
print(x)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)

print(x)

cars = ['Ford','BMW','Volvo']

fruits.extend(cars)

print(fruits)

x = fruits.index("cherry")
print(x)

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

fruits.pop(2)
print(fruits)
x = fruits.pop(2)
print(x)

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

fruits = ['apple','banana','cherry']
fruits.reverse()
print(fruits)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

def myFunc(e):
    return len(e)

cars = ['Ford','Mitsubishi','BMW','VW']

cars.sort(key=myFunc)
print(cars)