import queue

q = queue.Queue(maxsize=2)  # 队列最大容量为 2

q.put(1)
q.put(2)

try:
    q.put(3, block=True, timeout=2)  # 队列已满，立即抛出异常
except queue.Full:
    print("Queue is full, cannot put more items.")