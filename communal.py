from main import *


# 战斗前置准备
def battle_preparation():
    print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 链接网络 等待: {args.connection_time}')
    connect_internet(args.connection_time)
    if len(str(args.raid_password)) == 4:
        print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 设置密码 密码: {args.raid_password}')
    else:
        print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 没有密码')
    set_password(args.raid_password)


def exit_raid(exit_mode):
    if exit_mode == 'flight':
        flight_mode()
    elif exit_mode == 'reload':
        restart_game()


# 飞行模式重启游戏
def flight_mode():
    send(ns_HOME, 2)
    for i in range(0, 4):
        send(ns_DOWN)
        sleep(0.02)
    send(ns_A)
    send(0.1)
    send(ns_A)
    send(0.1)
    send(ns_B)
    send(0.1)
    send(ns_A)
    sleep(10)


# 重启游戏
def restart_game():
    wake()
    # --- game close
    send(ns_HOME)
    sleep(1)
    send(ns_X)
    sleep(0.5)
    send(ns_A)
    sleep(3)
    # --- game open
    send(ns_A)
    sleep(1.5)
    send(ns_A)
    sleep(17)
    send(ns_A)
    sleep(10)


# 链接网络
def connect_internet(con_time):
    wake()
    send(ns_Y)
    sleep(1)
    send(ns_START)
    sleep(con_time)
    send(ns_B)
    sleep(0.2)
    send(ns_B)
    sleep(2)


# 输入密码
def set_password(psw):
    wake()
    send(ns_A)
    sleep(6)
    if len(str(psw)) == 4:
        a = psw // 1000
        b = (psw - a * 1000) // 100
        c = (psw - a * 1000 - b * 100) // 10
        d = psw - a * 1000 - b * 100 - c * 10
        send(ns_START)
        sleep(1)
        codes = [1, a, b, c, d]
        for num in range(0, 4):
            nx, ny = num_dist(codes[num], codes[num + 1])
            if nx > 0:
                for i in range(0, nx):
                    send(ns_RIGHT)
                    sleep(0.02)
            elif nx < 0:
                for i in range(0, -nx):
                    send(ns_LEFT)
                    sleep(0.02)
            if ny > 0:
                for i in range(0, ny):
                    send(ns_DOWN)
                    sleep(0.02)
            elif ny < 0:
                for i in range(0, -ny):
                    send(ns_UP)
                    sleep(0.02)
            send(ns_A)
            sleep(0.1)
        send(ns_START)
        sleep(1)
        send(ns_A)
        sleep(0.5)


def num_dist(a, b):
    cols = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    rows = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    ny = rows[b - 1] - rows[a - 1]
    nx = cols[b - 1] - cols[a - 1]
    return nx, ny


# 招募
def recruiting_players(duration):
    send(ns_A)
    start_recruit = time.time()
    while time.time() - start_recruit < duration:
        sleep(1)
    send(ns_UP)
    sleep(0.2)
    send(ns_A)
    sleep(0.5)
    send(ns_A)
    sleep(2)


# 唤醒游戏按键操作
def wake():
    print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 唤醒手柄 ')
    count = 5
    while count > 0:
        count = count - 1
        send(ns_B)
        sleep(0.5)


# 前往修改时间界面
def go_change_time():
    send(ns_HOME)
    sleep(0.5)
    send(ns_DOWN)
    sleep(0.1)
    for i in range(0, 4):
        send(ns_RIGHT, 0.1)
        sleep(0.1)
    send(ns_A)
    sleep(0.4)
    send(ns_DOWN, 1.5)
    send(ns_A)
    sleep(0.1)
    for i in range(0, 4):
        send(ns_DOWN, 0.1)
        sleep(0.1)
    send(ns_A)
    sleep(0.4)
    for i in range(0, 2):
        send(ns_DOWN, 0.1)
        sleep(0.1)


# 返回游戏
def back_game():
    send(ns_HOME)
    sleep(1.0)
    send(ns_HOME)
    sleep(0.5)


# 简单的修改时间操作
def change_time(callback):
    send(ns_A)
    sleep(0.4)
    for c in range(0, 2):
        send(ns_RIGHT)
        sleep(0.1)
    callback()
    for c in range(0, 3):
        send(ns_RIGHT)
        sleep(0.1)
    send(ns_A)
    sleep(0.5)
