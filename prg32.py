import os
print("Effective group id :",os.getgroups())
print("Effective user id :",os.geteuid())
print("Real group id :", os.getgid())
print("Real user id :", os.getuid())

#for unix os only