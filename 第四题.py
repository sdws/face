from queue import Queue
from threading import Thread
from time import sleep

#生产
class Producer(Thread):
   def run(self):
      global q
      count = q.qsize()
      while True:
         if q.qsize() < 1000:
            #生产100个
            for i in range(1,101):
               count += 1
               msg = "面包-%d" %count
               q.put(msg)
               print("生产了：%s" % msg)
         #休眠一会
         sleep(0.5)


#消费者
class Consumer(Thread):
   def run(self):
      global q
      while True:
         if q.qsize() > 100:
            # 生产100个
            for i in range(1, 4):
               msg = q.get()
               print("已经消费了:%s" %msg)
         # 休眠一会
         sleep(0.5)


q = Queue()

#初次生产500个面包
for i in range(1,501):
   q.put("面包-%d"%i)

for i in range(2):
   Producer().start()

for i in range(5):
   Consumer().start()