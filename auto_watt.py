from communal import *

print(f'Delay for {args.delay} seconds.')
print(f'开始自动刷瓦特任务！')
sleep(args.delay)


def set_one_time():
    send(ns_UP, 0.07)
    sleep(0.1)


def reset_one_time():
    t_move = 0.03
    t_click = 0.07
    send(ns_A, t_click)
    sleep(0.1)
    for i in range(0, 3):
        send(ns_LEFT, t_click)
        sleep(t_move)
    send(ns_DOWN, t_click)
    for i in range(0, 3):
        send(ns_RIGHT, t_click)
        sleep(t_move)
    send(ns_A, t_click)
    sleep(0.11)


wake()
try:
    watt_count = 0
    while True:
        go_change_time()
        change_time(set_one_time)
        reset_one_time()
        back_game()
        for c in range(0, 3):
            send(ns_A)
            sleep(0.6)
        send(ns_B, 0.07)
        sleep(1)
        watt_count += 1
        print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 完成第 {watt_count} 次瓦特，一共获取 {watt_count * 2000} 瓦特！')

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
