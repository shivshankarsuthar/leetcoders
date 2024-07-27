import multiprocessing
import os

# Simple demonstration of multiprocessing in python
def process1(num):
    print("Process id:",os.getpid())
    print("Square:",num*num)
    

def process2(num):
    print("Process id:",os.getpid())
    print("Cube:",num**3)

def main():
    print("Main process id:",os.getpid())
    p1 = multiprocessing.Process(target=process1,args=(10,))
    p2 = multiprocessing.Process(target=process2,args=(10,))
    
    p1.start()
    p2.start()
 
    p1.join()
    p2.join()

#main()

# Data sharing between child and parent process using shared memory , ideally two independent processes doesn't share memory space
def process(result,array,value):
    for i in range(len(result)):
        array[i] = result[i]**2
    value.value = sum(array)

def main2():
    result = [1,2,3,4]
    array = multiprocessing.Array('i',4)
    value = multiprocessing.Value('i')
    p = multiprocessing.Process(target=process,args=(result,array,value,))
    p.start()
    p.join()
    print("Result after Process execution",array[:])
    print("Sum of squares",value.value)

#main2()
    
# Data sharing using Queue
def process1(result,queue):
    for i in range(len(result)):
        queue.put(result[i]**2)

def process2(queue):
    while not queue.empty():
        print(queue.get())
    

def main2():
    result = [1,2,3,4]
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=process1,args=(result,queue,))
    p2 = multiprocessing.Process(target=process2,args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Done')
    
#main2()
    
#Data sharing between processes using Pipe
    
def process1(result,parent_conn):
    for i in range(len(result)):
        parent_conn.send(result[i])

def process2(child_conn):
    while True:
        msg = child_conn.recv()
        print(msg)
        if msg == 'END':
            break
    

def main2():
    result = ['Hey','How',"are you","END"]
    parent_conn,child_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=process1,args=(result,parent_conn,))
    p2 = multiprocessing.Process(target=process2,args=(child_conn,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

main2()

