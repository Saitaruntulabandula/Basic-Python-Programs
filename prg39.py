import os
user_path = 'C:/Users/TARUN/Desktop/Basic Python'
for fname in os.listdir(user_path):
   path = os.path.join(user_path, fname)
   if os.path.isdir(path):
       # skipping directories.
       continue
   # printing the file names.
   print(fname)
