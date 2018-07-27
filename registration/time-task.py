import datetime
import time
import schedule


def doMyTask():
    print('任务启动了:' + str(datetime.datetime.now()))

# def main(h=8, m=49):
#     while True:
#         now = datetime.datetime.now()
#         if now.hour == h and now.minute == m:
#             break
#         time.sleep(10)
#     doMyTask()

# def timerFun(sched_Timer):
#     flag = 0
#     while True:
#         now = datetime.datetime.now()
#         # print(now)
#         if now.hour == sched_Timer and now.minute == sched_Timer.minute:
#             doMyTask()
#             flag = 1
#         elif flag == 1:
#             sched_Timer = sched_Timer + datetime.timedelta(minutes=1)
#             flag = 0
#
# if __name__ == '__main__':
#     sched_Timer = datetime.datetime(2018,7,27,9,14)
#     print('run the timer task at {0}'.format(sched_Timer))
#     timerFun(sched_Timer)

# while True:
#     doMyTask()
#     time.sleep(10)

# schedule.every().minute.do(doMyTask)
schedule.every(2).seconds.do(doMyTask)
while True:
    schedule.run_pending()