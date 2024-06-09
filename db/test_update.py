import pymysql


def update(conn):
    try:
        with conn.cursor() as cursor:
            sql = 'update user set age=%s where name=%s'
            cursor.execute(sql, (21, 'Kate'))
        conn.commit()
    except pymysql.MySQLError as e:
        print(type(e), e)
        conn.rollback()
    finally:
        conn.close()


def main():
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8')
    update(conn)


if __name__ == '__main__':
    main()