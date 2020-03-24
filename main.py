import argparse
import serial
import time
from time import sleep
import datetime


def send(msg, duration=0.2):
    # now = datetime.datetime.now()
    now = time.localtime()
    now_str = time.strftime("%H:%M:%S", now)
    if args.monitor:
        print('[{:}] {:}'.format(now_str, msg))
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')


parser = argparse.ArgumentParser()
parser.add_argument('port')
# --- hatching related ---
parser.add_argument('--box', '-b', type=int, default=1)
parser.add_argument('--hatch_mode', '-hm', default='normal')
# --- frameskip related ---
parser.add_argument('--frame', '-f', type=int, default=200)
parser.add_argument('--frame_save', '-fs', type=int, default=400)
# --- egg collection related ---
parser.add_argument('--egg_cycle', '-ec', type=int, default=3)
# --- auto den hunting related ---
parser.add_argument('--connection_time', '-ct', type=int, default=10)
parser.add_argument('--recruit_duration', '-rd', type=int, default=90)
parser.add_argument('--battle_duration', '-bd', type=int, default=40)
parser.add_argument('--raid_password', '-rp', type=int, default=4523)
parser.add_argument('--exit_mode', '-em', default='reload')
# --- other setting ---
parser.add_argument('--delay', '-d', type=int, default=3)
parser.add_argument('--monitor', type=bool, default=False)

args = parser.parse_args()
ser = serial.Serial(args.port, 9600)

ns_X = 'Button X'
ns_Y = 'Button Y'
ns_A = 'Button A'
ns_B = 'Button B'
ns_L = 'Button L'
ns_R = 'Button R'
ns_ZL = 'Button ZL'
ns_ZR = 'Button ZR'
ns_LEFT = 'LX MIN'
ns_RIGHT = 'LX MAX'
ns_UP = 'LY MIN'
ns_DOWN = 'LY MAX'
ns_UP_LEFT = 'UP_LEFT MIN'
ns_UP_RIGHT = 'UP_RIGHT MIN'
ns_DOWN_LEFT = 'DOWN_LEFT MIN'
ns_DOWN_RIGHT = 'DOWN_RIGHT MIN'
ns_START = 'Button START'
ns_SELECT = 'Button SELECT'
ns_HOME = 'Button HOME'
ns_CAPTURE = 'Button CAPTURE'
ns_L3 = 'Button LCLICK'
ns_R3 = 'Button RCLICK'
