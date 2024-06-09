from threading import Thread, Lock
from time import sleep


class Counter:
    def __init__(self):
        self.counter = 0
        self.lock = Lock()

    def increment(self):
        with self.lock:
            self.counter += 1

    def get_counter(self):
        with self.lock:
            return self.counter


def sub_process(args, c):
    while c.get_counter() < 10:
        print("Sub process: %s - %d" % (args, c.get_counter()), flush=True)
        c.increment()
        sleep(1)


def main():
    counter = Counter()
    t1 = Thread(target=sub_process, args=('ping', counter))
    t2 = Thread(target=sub_process, args=('pong', counter))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
