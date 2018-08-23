from manager import Manager
from user import User


def main():
    u = User(('kiss3256', 'oop33e01'))
    m = Manager()
    m.add_user(u)
    m.run()


if __name__ == '__main__':
    main()
