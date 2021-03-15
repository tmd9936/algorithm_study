import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)
print("Start")

# threads = []
# for i in range(5):
#     # 쓰레드를 생성한다
#     t = threading.Thread(target=long_task)
#     threads.append(t)

# for t in threads:
#     # 쓰레드를 실행한다
#     t.start()

# print("End")

# start와 end가 먼저출력 되고 스레드가 실행됨
# 원하는 동작은 Start - 쓰레드 함수 모두 실행 - End

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    # join으로 스레드가 종료될 때까지 기다린다.
    t.join()

print("End")
