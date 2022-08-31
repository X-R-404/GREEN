import os, platform
try:os.system('git pull')
except:pass
try:os.mkdir('OK')
except:pass
try:os.mkdir('CP')
except:pass
try:os.system('touch .prox.txt')
except:pass
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from GREEN import apv
    apv()
elif bit == '32bit':
    from GREEN32 import apv
    apv()
