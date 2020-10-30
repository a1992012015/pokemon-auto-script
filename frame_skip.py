from communal import *

print(f'Delay for {args.delay} seconds.')
print(f'开始自动跑帧任务！')
sleep(args.delay)


# 保存游戏
def save_game():
    # 返回游戏
    send(ns_HOME)
    sleep(2)
    send(ns_HOME)
    sleep(2)
    # 存档
    send(ns_X)
    sleep(2)
    send(ns_R)
    sleep(2)
    send(ns_A)
    sleep(4)
    # 返回时间界面
    go_change_time()
    send(ns_A)
    sleep(0.03)
    for i in range(0, 5):
        send(ns_RIGHT, 0.05)
        sleep(0.03)
    send(ns_A)
    sleep(0.03)


# 切换时间
def frame_skip():
    t_click = 0.06
    send(ns_A, t_click)
    sleep(0.1)

    send('LX MIN', t_click)
    send('RX MIN', t_click)
    send('HAT LEFT', t_click)

    send('LY MIN', t_click)

    send('LX MAX', t_click)
    send('RX MAX', t_click)
    send('HAT RIGHT', t_click)

    sleep(0.03)
    send(ns_A, t_click)
    sleep(0.11)


try:
    frame_counter = 0  # 因为测帧的问题提前一帧
    date_counter = 1
    time_0 = time.time()
    send(ns_RIGHT, 0.1)
    sleep(0.1)
    start_time = time.time()
    while frame_counter < args.frame:
        date_counter += 1
        frame_skip()
        if date_counter <= 31:
            frame_counter += 1
        else:
            date_counter = 1
        now = time.strftime("%H:%M:%S", time.localtime())
        remain = args.frame - frame_counter
        consume_time = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
        print(f'[ {now} ] 当前帧: {frame_counter}, 日期: {date_counter}, 剩余帧: {remain}， 花费时间: {consume_time}')
        if frame_counter % args.frame_save == 0:
            save_game()
    send('RELEASE')
    ser.close()
    print(f'finished. time consumed: {time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))}')

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
