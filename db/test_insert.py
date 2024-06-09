import pymysql


def insert(conn):
    try:
        with conn.cursor() as cursor:
            sql = 'insert into user (name, age) values (%s, %s)'
            cursor.execute(sql, ('Tom', 20))
        conn.commit()
    except pymysql.MySQLError as e:
        print(type(e), e)
        conn.rollback()
    finally:
        conn.close()


def insertAll(conn):
    try:
        with conn.cursor() as cursor:
            sql = 'insert into user (name, age) values (%s, %s)'
            cursor.executemany(sql, [('Kate', 20), ('Jerry', 22), ('Jack', 23)])
        conn.commit()
    except pymysql.MySQLError as e:
        print(type(e), e)
        conn.rollback()
    finally:
        conn.close()


def main():
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8')
    insert(conn)
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8')
    insertAll(conn)


if __name__ == '__main__':
    main()
