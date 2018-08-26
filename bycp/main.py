from my_agent import Agent
import time


def main():
    a = Agent()

    while True:
        try:
            d = a.lottery()
            r = a.settle(d)
            a.buy(r)

            time.sleep(20)
        except Exception as e:
            print(' ---- ERROR ---- ', e)
            time.sleep(10)


if __name__ == '__main__':
    main()
