import psycopg2

import User
import Employee


class Controller(object):

    def __init__(self, dbname, user, password, host):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def insert(self, instance):
        if type(instance) == User.User:
            self.cursor.execute("INSERT INTO customer VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                                (instance.identifier, instance.name, instance.surname,
                                 instance.number, instance.birth_date,
                                 instance.country, instance.city, instance.bonus_points))
        elif type(instance) == Employee.Employee:
            self.cursor.execute("INSERT INTO employee VALUES(%s, %s)",
                                (instance.identifier, instance.specialization))
        self.conn.commit()

    def get_all(self, table_name):
        self.cursor.execute('SELECT * FROM ' + table_name)
        return self.cursor.fetchall()

    def user_exists(self, identifier):
        self.cursor.execute('SELECT * FROM customer WHERE user_id = ' + str(identifier))
        return self.cursor.fetchall()

    def employee_exists(self, identifier):
        self.cursor.execute('SELECT * FROM employee WHERE employee_id = ' + str(identifier))
        return self.cursor.fetchall()
