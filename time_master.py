import time
def myfunc():
    print("myfunc is running!")
def time_master(func):
    print("start the function~")
    start=time.time()
    func()
    stop=time.time()
    print("stop the function")
    print(f"The total time consumed:{(stop-start):.2f}s")

