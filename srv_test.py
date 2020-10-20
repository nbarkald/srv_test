#!/usr/bin/python
from time import sleep, asctime, localtime, time


def main():
    print("hello, starting!")
    while True:
        lt = asctime(localtime(time()))
        print("reporting at %s before sleeping for 1 sec" % lt)
        sleep(1)


if __name__ == "__main__":
    main()

