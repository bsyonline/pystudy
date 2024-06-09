import pymysql


def delete(conn):
    try:
        with conn.cursor() as cursor:
            sql = 'delete from user where name=%s'
            cursor.execute(sql, ('Tom',))
        conn.commit()
    except pymysql.MySQLError as e:
        print(type(e), e)
        conn.rollback()
    finally:
        conn.close()


def main():
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='test', charset='utf8')
    delete(conn)


if __name__ == '__main__':
    main()
