from time import time, sleep
from multiprocessing import Process


def foo(name):
    print(name)
    for i in range(5):
        print(f"{name} {i}", flush=True)
        sleep(1)
    print(f"End {name}")


def bar(name):
    print(name)
    for i in range(10):
        print(f"{name} {i}", flush=True)
        sleep(1)
    print(f"End {name}")


def main():
    start = time()
    p1 = Process(target=foo, args=('foo',))
    p1.start()  # 启动进程p1
    p2 = Process(target=bar, args=('bar',))
    p2.start()  # 启动进程p2
    p1.join()  # 等待进程p1结束
    p2.join()  # 等待进程p2结束
    end = time()
    print("Execution time: %.2f" % (end - start))


if __name__ == "__main__":
    main()
