import pyfirmata
from pyfirmata import Arduino, util, STRING_DATA, INPUT
import time

board = pyfirmata.Arduino('COM7')
red_led = board.digital[2]
buzzer = board.digital[7]
Button = board.digital[8]
iteration = pyfirmata.util.Iterator(board)
iteration.start()
Button.mode = pyfirmata.INPUT
red_led.write(1)
buzzer.write(1)

alert1 = " ALERT ATTACK!!"
def access(board, alert1):
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(alert1))
access(board, alert1)
while True : 
    Button_state = Button.read()
    print(Button_state)
    if Button_state is True :
        red_led.write(0)
        buzzer.write(0)
        break
    time.sleep(1)
    



