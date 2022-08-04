
from threading import*
import time

def f1(n):
    for x in range(n):
        time.sleep(4)
        print(current_thread().name,x)
start=time.time()
t1 = Thread(target=f1,args=[5], name='thread1')
print(current_thread().name)

def f2():
    for x in range(6,11):
        print(current_thread().name,x)
t2 = Thread(target=f2, name='thread2')

t1.start()
t2.start()
t1.join()
t2.join()
