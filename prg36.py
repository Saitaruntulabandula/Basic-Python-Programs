try:
  a = 1
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")
try:
    b
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")