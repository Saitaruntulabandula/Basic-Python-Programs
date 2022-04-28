list = []
for i in range(3):  # Save the integers in a list
    list.append(int(input("Enter the value: ")))

print("Before Sorting : ", list)
list.sort()  # Sort the list
print("After Sorting : ",list)