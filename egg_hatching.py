from main import *

print(f'Delay for {args.delay} seconds.')
sleep(args.delay)
send(ns_L3)


def box_to_crew(col):
    time_s = 0.2
    send(ns_A)
    sleep(time_s)
    send(ns_UP)
    sleep(time_s)
    send(ns_A)
    sleep(time_s)

    for j in range(0, col):
        send(ns_LEFT)
        sleep(time_s)
    send(ns_DOWN)
    sleep(time_s)
    send(ns_A)
    sleep(time_s)


def crew_to_box(col):
    time_s = 0.2
    send(ns_LEFT)
    sleep(time_s)
    send(ns_DOWN)
    sleep(time_s)
    send(ns_A)
    sleep(time_s)
    send(ns_UP)
    sleep(time_s)
    send(ns_UP)
    sleep(time_s)
    send(ns_A)
    sleep(time_s)
    send(ns_UP)
    sleep(time_s)

    for j in range(0, col):
        send(ns_RIGHT)
        sleep(time_s)
    send(ns_A)
    sleep(time_s)


if args.hatch_mode == 'normal':
    n_loop = 4
elif args.hatch_mode == 'short':
    n_loop = 2
elif args.hatch_mode == 'long':
    n_loop = 8
else:
    raise Exception('Wrong hatch mode. Only long, normal and short is possible.')
    send('RELEASE')
    ser.close()

try:
    for nbox in range(0, args.box):
        start_time = time.time()
        for col in range(1, 6 + 2):
            lap_start_time = time.time()
            # ========= Egg selection and replacement =========
            # --- Box entry
            send(ns_X)
            sleep(0.6)
            send(ns_A)
            sleep(1.5)
            send(ns_R)
            sleep(1.5)
            # --- Select eggs
            send(ns_Y)
            sleep(0.2)
            send(ns_Y)
            sleep(0.2)
            if col > 1:
                crew_to_box(col - 1)
                if col == 7:
                    send(ns_R)
                    sleep(0.4)
                else:
                    send(ns_RIGHT)
                    sleep(0.2)
                    box_to_crew(col)
            else:
                box_to_crew(col)
            # --- Exit 
            send(ns_B)
            sleep(1.5)
            send(ns_B)
            sleep(1)
            send(ns_B)
            sleep(1)
            # =========== Cycling and hatching =========
            if col < 7:
                for lp in range(0, n_loop):
                    send(ns_RIGHT, duration=12)
                    send(ns_DOWN, duration=1)
                    send(ns_LEFT, duration=13)
                # --- confirmation
                for n_egg in range(0, 5):
                    send(ns_B)
                    sleep(14)
                    send(ns_B)
                    sleep(2.5)
                    send(ns_RIGHT, duration=1)
        dt_box = round(time.time() - start_time, 2)
        time_remain = time.strftime("%H:%M:%S", time.localtime(time.time() + dt_box * (args.box - nbox)))
        print('{:} / {:}, takes {:}s for one box, estimated finishing time: {:}'.format(nbox + 1, args.box, dt_box,
                                                                                        time_remain))
    send('RELEASE')
    ser.close()

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
