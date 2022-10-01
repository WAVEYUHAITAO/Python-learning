import time
def myfunc():
    time.sleep(2)
    print("Hello HAITAO!")
def time_master(func):
    print("start the function~")
    start=time.time()
    func()
    stop=time.time()
    print("stop the function")
    print(f"The total time consumed:{(stop-start):.2f}s")

time_master(myfunc)
