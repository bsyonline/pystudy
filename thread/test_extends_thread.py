from threading import Thread
from time import sleep, time


class Foo(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(self.name)
        for i in range(5):
            print(f"{self.name} {i}", flush=True)
            sleep(1)
        print(f"End {self.name}")


def main():
    start = time()
    t1 = Foo('foo')
    t1.start()
    t2 = Foo('bar')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print("Execution time: %.2f" % (end - start))


if __name__ == "__main__":
    main()