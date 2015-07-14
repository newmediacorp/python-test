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
        


db = Database()
print db
