from main import *

print(f'Delay for {args.delay} seconds.')
print(f'Pls check make sure the date is 1 Jan and the cursor is at the right end.')
sleep(args.delay)


# send(ns.L3)

def frameskip():
    t_move = 0.03
    t_click = 0.07
    for i in range(0, 3):
        send(ns_LEFT, t_click)
        sleep(t_move)
    send(ns_UP, t_click)
    sleep(t_move)
    for i in range(0, 3):
        send(ns_RIGHT, t_click)
        sleep(t_move)
    send(ns_A, t_click)
    sleep(0.11)
    send(ns_A, t_click)
    sleep(0.1)
    # send(ns_A, t_click)
    # sleep(t_move)


def savegame():
    # --- back to game
    sleep(1)
    send(ns_HOME)
    sleep(3)
    send(ns_HOME)
    sleep(2)
    # --- insurance
    send(ns_B)
    sleep(1)
    # --- save
    send(ns_X)
    sleep(3)
    send(ns_R)
    sleep(3)
    send(ns_A)
    sleep(4)
    # --- back to time pannel
    send(ns_HOME)
    sleep(3)
    send(ns_DOWN)
    sleep(0.1)
    for i in range(0, 4):
        send(ns_RIGHT)
        sleep(0.1)
    send(ns_A)
    sleep(0.4)
    send(ns_DOWN, 1.8)
    # for i in range(0,15):
    #    send(ns_DOWN)
    #    sleep(0.1)
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
    send(ns_A)
    sleep(0.4)
    for i in range(0, 5):
        send(ns_RIGHT, 0.1)
        sleep(0.1)


try:
    frame_counter = 1
    date_counter = 1
    time_0 = time.time()
    send(ns_RIGHT, 0.1)
    sleep(0.1)
    while frame_counter < args.frame:
        start_time = time.time()
        date_counter += 1
        frameskip()
        if date_counter <= 31:
            frame_counter += 1
        else:
            date_counter = 1
        if frame_counter % args.frame_save == 0:
            savegame()
        dtime = round(time.time() - start_time, 2)
        now = time.strftime("%H:%M:%S", time.localtime())
        time_remain = time.strftime("%H:%M:%S", time.localtime(time.time() + dtime * (args.frame - frame_counter)))
        print('[ {:} ] current frame: {:}, date: {:}, remaining frames: {:}, estimated finishing time: {:}'.format(
            now,
            frame_counter,
            date_counter,
            args.frame - frame_counter,
            time_remain
        ))
    send('RELEASE')
    ser.close()
    print('finished. time consumed: {:}'.format(time.strftime("%H:%M:%S", time.gmtime(time.time() - time_0))))

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
