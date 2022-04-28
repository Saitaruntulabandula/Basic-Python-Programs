import sys

print("System defined recursion limit : ",sys.getrecursionlimit())
sys.setrecursionlimit(100)
print("User defined recursion limit : ", sys.getrecursionlimit())
#A recursive function could call itself indefinitely. 
#In other words, you could end up with an endless loop.
#The recursion depth limit in Python is by default 1000 .
#You can change it using sys. setrecursionlimit() function.