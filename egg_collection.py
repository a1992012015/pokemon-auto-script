from main import *

print(f'Delay for {args.delay} seconds.')
sleep(args.delay)
# send(ns.L3)

try:
    start_time = time.time()
    counter = 0
    while True:
        counter += 1
        send(ns_LEFT, 1.7)
        send(ns_RIGHT, 1.5)
        for nbox in range(1, args.egg_cycle - 1):
            send(ns_LEFT, 1.5)
            send(ns_RIGHT, 1.5)
        send(ns_LEFT, 1.5)
        send(ns_RIGHT, 1.0)
        send(ns_UP_RIGHT, 1.2)
        # --- dialogue
        send(ns_A)
        sleep(1.0)
        send(ns_A)
        sleep(2.8)
        send(ns_B)
        sleep(1.5)
        send(ns_B)
        sleep(1.4)
        send(ns_B)
        sleep(0.6)
        dtime = round(time.time() - start_time, 2)
        time_take = time.strftime("%H:%M:%S", time.gmtime(dtime))
        print('{:} loops, takes {:}'.format(counter, time_take))
    send('RELEASE')
    ser.close()

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
