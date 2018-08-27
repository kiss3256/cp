from my_agent import Agent
import time


def main():
    a = Agent()

    while True:
        try:
            a.run()
            time.sleep(20)
        except Exception as e:
            print(' ---- ERROR ---- ', e.args)
            time.sleep(10)


if __name__ == '__main__':
    main()
