first_name=input("Enter the first name: ")
last_name=input("Enter the last name: ")
#list[<start>:<stop>:<step>]
#This means that the object is going to slice every "step" index from the given start index
#till the stop index (excluding the stop index) and return it to you.
print(first_name[::-1]," ",last_name[::-1])