# -*-coding:utf-8 -*-
__author__ = 'yanshi'
from threading import Thread
from Queue import Queue, Empty
import random

queue = Queue(1000)
write_queue = Queue()
test_array = [i for i in range(0, 1000)]
count = 0
workers = []


class Product(Thread):
    def run(self):
        global count
        while count < 10000:
            queue.put(random.choice(test_array))
            count += 1
        print 'try...stop'
        for w in workers:
            w.stop()


class Worker(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(Worker, self).__init__(group, target, name, args, kwargs, verbose)
        self.thread_stop = False

    def run(self):
        while True:
            try:
                v = queue.get(timeout=10)
                queue.task_done()
                write_queue.put(v)
            except Empty:
                break
        print self.thread_stop


    def stop(self):
        self.thread_stop = True
        print self.thread_stop, 'shop'


class Write(Thread):
    def run(self):
        f = open('test', 'a')
        while True:
            try:
                line = write_queue.get(timeout=10)
                f.write(str(line))
                f.write('\n')
                write_queue.task_done()
            except Empty:
                break
        f.close()


Product().start()
Write().start()
for i in range(0, 5):
    worker = Worker(name=i)
    worker.start()
    workers.append(worker)
