print(10>9)
print(10== 9)
print(10<9)
a = 200
b = 33
if b > a:
    print("b is greater than a")
else: 
    print("b is not greater than a")
#any string is true except emtpy strings
#any number is true except 0
#any list, tuple, set, and dictionary are true except emtpy ones
print(bool("Hello"))
print(bool(0))
print(bool(1j))
print(bool(-5))
print(bool("abc"))
bool(["apple", "cherry", "banana"])
print(bool(False))
print(bool(None))
print(bool())
print(bool([]))

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

x = 13135
print(isinstance(x, int))
print(isinstance(x, str))
print(isinstance(x, set))