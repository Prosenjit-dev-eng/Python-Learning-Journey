from threading import Thread 
from time import sleep,time
#io bound task
def download(filename):
    print("Downloading...... ",filename)
    sleep(0.5)
    print("Download Completed ",filename)
#cpu bound task
def calc(n1,n2):
    sum = 0
    for n in range(n1,n2):
        sum += n**n
if __name__ == "__main__":
    files = ["File1","File2","File3","File4"]
    start = time()
    for f in files:
        download(f)
    end = time()
    print(f"Serial time {end-start: .2f} seconds")

    #threading
    threads = []
    for f in files:
        t = Thread(target=download,args=(f,))
        threads.append(t)
    start = time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time()
    print(f"Threading time {end-start: .2f} seconds")

    n = 5000
    start = time()
    calc(1,n)
    end = time()
    print(f"Serial time {end-start: .2f} seconds")
    mid = n // 2
    t1 = Thread(target=calc,args=(1,mid))
    t2 = Thread(target=calc,args=(mid,n))
    start = time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print(f"Thread time {end-start: .2f} seconds")

    print("Bye")