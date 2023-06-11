import pyfirmata
from pyfirmata import Arduino, util, STRING_DATA, INPUT
import time

board = pyfirmata.Arduino('COM7')
iteration = pyfirmata.util.Iterator(board)
iteration.start()

alert1 = " ALERT ATTACK!!"
def access(board, alert1):
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(alert1))
access(board, alert1)