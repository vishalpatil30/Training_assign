import logging
import time

logging.basicConfig(filename='StackLogging.log',level=logging.DEBUG)
logging.debug("------------------------------------------------------")

class Stack:
     def __init__(self):
         self.items = []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

class main():
    s=Stack()
    now = time.asctime( time.localtime(time.time()) )
    while(1):
        x=input("Plase Enter operation no. you want to execute: 1. PUSH 2.POP 3.PEEK 4.EXIT \n")
        if x == 1:
            i=input("Enter the value \n")
            s.push(i)
            logging.debug(now + ": pushed value is "+str(i))
        elif x == 2:
            v = s.pop()
            logging.debug(now + ": poped value is "+str(v))
            print "Poped value is ",v
        elif x == 3:
            print "Top of the stack is ",s.peek()
            logging.debug(now + ": Top of the stack is " + str(s.peek()))
        elif x == 4:
            exit(0)

if __name__ == '__main__':
    main()
