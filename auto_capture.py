from communal import *

print(f'Delay for {args.delay} seconds.')
print(f'开始自动捕获任务！')
sleep(args.delay)

print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 重启游戏')
restart_game()
# 战斗准备
battle_preparation()

print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 招募开始 等待: {args.recruit_duration}s')
recruiting_players(args.recruit_duration)

waiting_time = 200
print(f'[{time.strftime("%H:%M:%S", time.localtime())}] 开始捕获 等待: {waiting_time / 2}s')
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
