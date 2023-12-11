from datetime import datetime
import os
import sys

os.system("git add .")
if(len(sys.argv) == 1):
    os.system("git commit -m 'update " +
              datetime.now().strftime("%d/%m/%Y/%H:%M") + "'")
else:
    os.system("git commit -m '" + sys.argv[1] + "'")
os.system("git push")
