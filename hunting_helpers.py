from communal import *

print(f'Delay for {args.delay} seconds.')
print(f'开始猎具生物收集！')
sleep(args.delay)

waiting_time = 300
try:
    for t in range(0, waiting_time):
        nt = t + 1
        if nt == waiting_time:
            print(f'\r[{time.strftime("%H:%M:%S", time.localtime())}] 当前次数 {nt}')
        else:
            print(f'\r[{time.strftime("%H:%M:%S", time.localtime())}] 当前次数 {nt}', end='')
        send(ns_A, 0.1)
        sleep(2)
        send(ns_Y, 0.1)
        sleep(2)
    print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 猎具生物收集完毕，检查马绘')

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
