from threading import Thread 
from time import sleep
def hello():
       for i in range(5):
           print("Hello ",i+1) 
           sleep(0.3)
def hi():
       for i in range(5):
           print("Hi ",i+1) 
if __name__ == "__main__":
    t1 = Thread(target=hello)
    sleep(0.2)#delay
    t2 = Thread(target=hi)
    t1.start()
    t2.start()
    t1.join()#wait until t1 is finished
    t2.join()#wait until t2 is finished
    print("Bye")