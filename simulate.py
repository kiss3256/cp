import sys

from conenct import Connect


def to_big(n):
    return 1 if n > 4 else 0


def anti_big(n):
    return 0 if n else 1


class User(object):
    def __init__(self):
        self.last = ()
        self.balance = 100
        self.record = ()
        self.lose = 0

    def cal(self, n5):
        if self.last != ():
            b, c = self.last
            if n5 == b:
                self.balance += c * 1.99
                self.lose = 0
                self.last = ()
            else:
                self.lose += 1

    def update(self, n5):
        if self.record == ():
            self.record = (n5, 1)
        else:
            b, c = self.record
            if n5 == b:
                self.record = (b, c + 1)
            else:
                self.record = (n5, 1)

    def buy(self, n):
        b, c = self.record
        if c >= 3 and self.lose <= 3:
            if self.last == ():
                self.balance -= 1
                self.last = (n, 1)
            else:
                b1, c1 = self.last
                self.balance -= c1 * 2
                self.last = (n, c1 * 2)

    def run(self, data):
        n5 = to_big(data['n1'])
        self.cal(n5)
        self.update(n5)
        if self.balance <= 50:
            print('---------------- DANGER ---------------- ')

        if self.balance <= 10:
            print('-------died-------')
            sys.exit(0)
        print(n5, self.balance, self.lose)
        self.buy(anti_big(n5))


def main():
    client = Connect.get_connection()
    bb77 = client["bb77"]
    col = bb77["om_ssc"]
    data = col.find({})
    u = User()

    for i in range(550, -1, -1):
        u.run(data[i])


if __name__ == '__main__':
    main()
