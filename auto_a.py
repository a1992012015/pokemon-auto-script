from communal import *

print(f'Delay for {args.delay} seconds.')
print(f'开始连续A任务！')
sleep(args.delay)

waiting_time = 10000
try:
    for t in range(0, waiting_time):
        nt = t + 1
        if nt == waiting_time:
            print(f'\r[{time.strftime("%H:%M:%S", time.localtime())}] 当前时间 {nt}')
        else:
            print(f'\r[{time.strftime("%H:%M:%S", time.localtime())}] 当前时间 {nt}', end='')
        send(ns_A)
        sleep(0.5)
    print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 捕获完成请检查捕获情况')

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
