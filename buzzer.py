import pyfirmata
from pyfirmata import Arduino,util,INPUT
import time

port = pyfirmata.Arduino('COM7')
buzzer = port.digital[7]

for i in range(1,11,1) :
    print(i)
    buzzer.write(1)
    time.sleep(1)
else :
    buzzer.write(0)

