from threading import Thread
from time import sleep, time


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
    t1 = Thread(target=foo, args=('foo',))
    t1.start()
    t2 = Thread(target=bar, args=('bar',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print("Execution time: %.2f" % (end - start))


if __name__ == "__main__":
    main()
