# Simple thread demonstration in python
import threading
import time
import os

def print_cube(num):
    print(f'Process id:{os.getpid()}')
    print(f'Cube:{num*num*num}')

def print_square(num):
    print(f'Process id:{os.getpid()}')
    print(f'Square:{num*num}')

def main():
    thread1 = threading.Thread(target=print_cube,args=(10,))
    thread2 = threading.Thread(target=print_square,args=(10,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('Done!')

main()

# Thread syncronization using Thread lock
global_x = 0

def increment(lock):
    #print(f'{threading.current_thread().name} is incrementing')
    global global_x
    lock.acquire()
    y = global_x 
    for _ in range(1000000):
        y += 1
    global_x = y
    lock.release()

def main2():
    global global_x
    global_x = 0
    lock = threading.Lock()
    thread1 = threading.Thread(target=increment,name='Thread 1',args=(lock,))
    thread2 = threading.Thread(target=increment,name='Thread 2',args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    
    #print('Done!')

for _ in range(10):
    main2()
    print("Global x : ",global_x)