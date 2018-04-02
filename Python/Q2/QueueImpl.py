import logging
import time

logging.basicConfig(filename='QueueLogging.log',level=logging.DEBUG)
logging.debug("------------------------------------------------------")

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]

class main():
    s=Queue()
    now = time.asctime( time.localtime(time.time()) )
    while(1):
        x=input("Plase Enter operation no. you want to execute: 1. ENQUEUE 2.DEQUEUE 3.FRONT 4.EXIT \n")
        if x == 1:
           i = input("Enter the value \n")
           s.enqueue(i)
           logging.debug(now + ": Enqueued value is "+str(i))
        elif x == 2:
            v = s.dequeue()
            print "Dequeued value is ",v
            logging.debug(now + ": Dequeued value is "+str(v))
        elif x == 3:
            print "Front value of queue is ",s.front()
            logging.debug(now + ": Front value of queue is " + str(s.front()))
        else:
            exit(0)

if __name__ == '__main__':
    main()
