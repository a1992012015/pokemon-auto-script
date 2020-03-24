from communal import *

print(f'Delay for {args.delay} seconds.')
print(f'开始SL三帧刷闪')
sleep(args.delay)


def change_one_time():
    send(ns_UP)
    sleep(0.1)


def change_back_time():
    for t in range(0, 3):
        send(ns_DOWN)
        sleep(0.1)


print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 重启游戏')
restart_game()

wake()
print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 开始SL')
for i in range(0, 3):
    if i < 2:
        print(f'\r[{time.strftime("%H:%M:%S", time.localtime())}] 现在第 {i + 1} 帧', end='')
    else:
        print(f'\r[{time.strftime("%H:%M:%S", time.localtime())}] 现在第 {i + 1} 帧')
    send(ns_A)
    sleep(1)
    send(ns_A)
    sleep(2)
    go_change_time()
    change_time(change_one_time)
    back_game()
    send(ns_B)
    sleep(0.5)
    send(ns_A)
    sleep(5)
    for c in range(0, 2):
        send(ns_A)
        sleep(0.6)

send(ns_A)
sleep(0.4)
print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 还原时间')
go_change_time()
change_time(change_back_time)
back_game()
