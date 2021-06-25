from communal import *

print(f'Delay for {args.delay} seconds.')
print(f'开始连续A任务！')
sleep(args.delay)

try:
    at = 0
    while True:
        at = at + 1
        print(f'\r[{time.strftime("%H:%M:%S", time.localtime())}] 当前时间 {at}', end='')
        send(ns_A, 0.1)
        sleep(0.5)

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
