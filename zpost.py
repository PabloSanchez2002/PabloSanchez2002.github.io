import os
import sys

os.system("git add .")
if(len(sys.argv) == 1):
    os.system("git commit -m 'update'")
else:
    os.system("git commit -m '" + sys.argv[1] + "'")
os.system("git push")
