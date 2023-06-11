import pyfirmata
from pyfirmata import Arduino, util, STRING_DATA

board = pyfirmata.Arduino('COM7')

led = board.digital[5]
led.write(1)