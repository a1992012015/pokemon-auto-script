from main import *

print(f'Delay for {args.delay} seconds.')
print(f'开始自动放生！')
sleep(args.delay)

box = args.box
t_move = 0.15


def row_release():
    ud = True
    for r in range(0, 6):
        column_release(ud)
        ud = bool(1 - ud)
        if r < 5:
            send(ns_RIGHT)
            sleep(t_move)
    for r in range(0, 5):
        send(ns_LEFT)
        sleep(t_move)


def column_release(ud):
    for b in range(0, 5):
        release()
        if b < 4:
            if ud:
                send(ns_DOWN)
            else:
                send(ns_UP)
            sleep(t_move)


def release():
    send(ns_A)
    sleep(t_move)
    for t in range(0, 2):
        send(ns_UP)
        sleep(t_move)
    send(ns_A)
    sleep(0.5)
    send(ns_UP)
    sleep(t_move)
    send(ns_A)
    sleep(1)
    send(ns_A)
    sleep(t_move)


while box > 0:
    row_release()
    send(ns_RIGHT)
    sleep(t_move)
    box = box - 1
