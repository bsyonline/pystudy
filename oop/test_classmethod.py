from datetime import datetime


class Clock:
    @classmethod
    def now(cls):
        return datetime.now()


def main():
    current_time = Clock.now()
    print(current_time)


if __name__ == "__main__":
    main()
