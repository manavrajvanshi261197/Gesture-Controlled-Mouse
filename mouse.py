from pyautogui import *
import serial
import time
FAILSAFE = False
acc_x=0
port = "COM10"
baud = 9600
ser=serial.Serial(port,baud)

def getval():
    global acc_x
    global acc_y
    t2=ser.readline().strip().decode('utf-8')
    value_array = t2.split("-")
    acc_x = int(value_array[0])
    acc_y = int(value_array[1])
    

x_max,y_max = size()
x,y = position()

while(True):
    
    getval()

    if( acc_x >420):
        x += 40
            
    elif( acc_x >380):
        x +=20

    if( acc_x <350):
        x -= 40
           
    elif( acc_x <330):
        x -= 20


        #####
    if( acc_y >420):
       y -= 40

    elif( acc_y >380):
        y -=20
            
            
    if( acc_y <340):
        y += 40
           
    elif( acc_y <310):
        y += 20
            
    
        
                   
            
    moveTo(x,y)
    
         
    print x,y
    
    
    
    
