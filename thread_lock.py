import threading, time

global_var = -1
lock = threading.Lock()

#have worker thread i try and set the global variable to its worker number
def func(num, lock):
    global global_var  # use the global variable "var"
    while (True):
        lock.acquire() #BEGIN CRITICAL SECTION
        var = num
        time.sleep(0.0001) #allow other threads to overwrite var
        print("worker %d has var= %d" % (num, var))
        lock.release() #END CRITICAL SECTION
        time.sleep(0.0001) #add some randomness

def main():
    for i in range(4): #make our 4 worker threads
        temp_thread = threading.Thread(target=func, args=(i, lock))
        temp_thread.start()


main()
