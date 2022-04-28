n=int(input("Enter the range: "))
list=[] #mutable
for i in range(n):
    value=input("Enter the element to add: ")
    list.append(value)
print(list)
tuple=tuple(list) #immutable
print(tuple)