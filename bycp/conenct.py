import sqlite3


def main():
    cx = sqlite3.connect("data/by_yf_ssc.db")
    cx.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")
    for t in [(0, 10, 'abc', 'Yu'), (1, 20, 'cba', 'Xu')]:
        cx.execute("insert into catalog values (?,?,?,?)", t)


if __name__ == '__main__':
    main()
