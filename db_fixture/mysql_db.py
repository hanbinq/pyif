import pymysql.cursors


# ========操作MySql===========
class DB(object):

    def __init__(self):
        try:
            self.connection = pymysql.connect(host='127.0.0.1',
                                              user='root',
                                              password='123456',
                                              db='guest',
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # 清空表数据
    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # 向表中插入数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " ("+key+") VALUES (" + value + ")"

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # 关闭数据库连接
    def close(self):
        self.connection.close()


if __name__ == '__main__':
    db = DB()
    table_name1 = "sign_event"
    data = {'id': 1, 'name': '红米', '`limit`': 2000, 'status': 1,
            'address': '北京会展中心', 'start_time': '2016-08-20 14:00:00'}

    table_name2 = "sign_guest"
    data2 = {'realname': 'alen', 'phone': '19500002412', 'email': 'alen@mail.com',
             'sign': 0, 'event_id': 1}

    db.clear(table_name1)
    db.insert(table_name1, data)
    db.close()
