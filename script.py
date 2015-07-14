import MySQLdb
import sys


class Database(object):
    __host = '127.0.0.1'
    __user = 'root'
    __password = ''
    __port = 3306
    __database = 'test'

    def __init__(self):
#       create DB connection
        try:
            self.db_connect = MySQLdb.connect(host=self.__host, port=self.__port, user=self.__user, passwd=self.__password, db=self.__database)
#           create cursor
            self.cursor = self.db_connect.cursor()
        except MySQLdb.Error, e:
            print e.args
            print 'ERROR: %d: %s' % (e.args[0], e.args[1])
            sys.exit(1)

    def request(self, sql):
        self.cursor.execute(sql)
        self.sqlout = self.cursor.fetchall()

    def insert(self,sql):
        try:
            self.cursor.execute(sql)
            self.db_connect.commit()
        except MySQLdb.Error, e:
            print e.args
            print "ERROR: %d: %s" % (e.args[0], e.args[1])
 
    def __del__(self):
#         Close cursor
        self.cursor.close ()
#         Close DB
        self.db_connect.close()
        print 'Database connection closed'

def main():
    db = Database()
# Create Table Customers
    sql = """
            CREATE TABLE IF NOT EXISTS customers(
                id int NOT NULL AUTO_INCREMENT,
                first_name  VARCHAR(50),
                last_name   VARCHAR(50),
                phone       VARCHAR(15),
                email       VARCHAR(100),
                address     VARCHAR(150),
                country     VARCHAR(30),
                PRIMARY KEY(id)
            )
    """
    db.request(sql)
# Create Table Products
    sql = """
            CREATE TABLE IF NOT EXISTS products(
                id int NOT NULL AUTO_INCREMENT,
                name        VARCHAR(50),
                price       FLOAT(11,2),
                description TEXT,
                PRIMARY KEY(id) )
    """
    db.request(sql)
# Create Table Orders
    sql = """
            CREATE TABLE IF NOT EXISTS orders(
                
            )
    """
    
    
    print db


if __name__ == '__main__':
    main()    
