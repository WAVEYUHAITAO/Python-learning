import time
def time_master(func):
    def call_func():
        print("start the function~")
        start=time.time()
        func()
        stop=time.time()
        print("stop the function")
        print(f"The total time consumed:{(stop-start):.2f}s")
    return call_func
@time_master #装饰器
def myfunc():
    time.sleep(2)
    print("Hello HAITAO!")
myfunc()