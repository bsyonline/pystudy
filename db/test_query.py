import pymysql


def query(conn):
    try:
        with conn.cursor() as cursor:
            sql = 'select * from user where age=%s'
            cursor.execute(sql, (21,))
            result = cursor.fetchall()
            for row in result:
                print(row)
    except pymysql.MySQLError as e:
        print(type(e), e)
    finally:
        conn.close()


def page_query(conn, page, size):
    try:
        with conn.cursor() as cursor:
            sql = 'select * from user where age=%s limit %s, %s'
            cursor.execute(sql, [21, (page-1)*size, size])
            result = cursor.fetchall()
            for row in result:
                print(row)
    except pymysql.MySQLError as e:
        print(type(e), e)
    finally:
        conn.close()


def main():
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8')
    query(conn)
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8')
    page_query(conn, 1, 1)


if __name__ == '__main__':
    main()
