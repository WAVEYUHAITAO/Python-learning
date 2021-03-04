#! /usr/bin/env python3
import pyautogui
print('press ctrl-C to quit.')
try:
    while True:
        #get and print the mouse coordinate
        x,y=pyautogui.position()
        positionStr='X:'+str(x).rjust(4)+'Y:'+str(y).rjust(4)
        print(positionStr,end='')
        print('\b'*len(positionStr),end='',flush=True)
except KeyboardInterrupt:
    print('Done.')