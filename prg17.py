from time import *

start_time = time()
print(start_time)

option=input("Enter 'S' to Stop: ") 
if option.lower()=='S' or 's':
    stop_time = time() 
    print(stop_time)
else:
    print("Invalid input")

total_time = stop_time - start_time
print(total_time , "miliseconds")