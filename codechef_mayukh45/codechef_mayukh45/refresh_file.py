from time import sleep
from MAIN import generate_refresh_token
import sys
import importlib
#from conf import refresh_token

#import os
#os.path.append('/home/mayukh/Documents/codechef_mayukh45')

def refresh():

    while(True):
        from conf import refresh_token
        del sys.modules['conf']
        print(refresh_token)

        generate_refresh_token(refresh_token)
        sleep(20*60)

refresh()


