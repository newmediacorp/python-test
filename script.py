import MySQLdb
import sys
import time
import os


class Database(object):
    __host = '127.0.0.1'
    __user = 'root'
    __password = ''
    __port = 3306
    __database = None

    def __init__(self,name):
#       create DB if Not Exists
        try:
            self.db_connect = MySQLdb.connect(host=self.__host, port=self.__port, user=self.__user, passwd=self.__password)
#           create cursor
            self.cursor = self.db_connect.cursor()
            self.request("CREATE DATABASE IF NOT EXISTS {}".format(name))
            self.__database = name
        except MySQLdb.Error, e:
            print e.args
            print 'ERROR: %d: %s' % (e.args[0], e.args[1])
            sys.exit(1)

        
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
        if self.cursor:
            self.cursor.close ()
#         Close DB
        if self.db_connect:
            self.db_connect.close()
        print 'Database connection closed'

    def get_dump(self):
        #import subprocess
        #print subprocess.Popen("mysqldump -u root -h 127.0.0.1 -P 3306 pythontest > backup12.sql",shell=True)
        #dumpcmd = "mysqldump -u " + 'root' + " -p" + '' + " " + 'pythontest' + " > " + './' + "/" + 'pythontest' + ".sql"
        #os.system(dumpcmd)
        try:
            os.popen("mysqldump -u root -h 127.0.0.1 -P 3306 pythontest > backup.sql")
        except Exception as e:
            print e
            
        #filestamp = time.strftime('%Y-%m-%d-%I:%M')
        #print os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (self.__user,'',self.__host,self.__database,self.__database+"_"+filestamp))

        #print os.popen("mysqldump -P 3306 -u root -h 127.0.0.1 pythontest1 > db_backup.sql")
        #print os.popen("mysqldump --help").read()
        #print os.popen("mysqldump -u root --h 127.0.0.1 pythontest > wikidb.sql")
        #print "\n-- please have a the dump file in "+self.__database+"_"+filestamp+".gz --"
        

def main():
    db = Database(name='pythontest')
    db.get_dump()
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
                id int NOT NULL AUTO_INCREMENT,
                customer_id INT(11),
                product_id INT(11),
                quantity INT(11),
                price FLOAT(11,2),
                PRIMARY KEY(customer_id, product_id),
                KEY(id)
            )
    """
    db.request(sql)
# INSERTING DUMMY DATA FOR TABLES customers, products, orders
    sql = """
            INSERT INTO customers(first_name, last_name, phone, email, address, country)
            VALUES
                ('Goren', 'AngelKovski', '38971371213', 'info@newmediacorp.com', 'Bitola, Fyro', 'Macedonia'),
                ('Nawazish', 'Qadir', '923314133340', 'nawazish@gmail.com', 'Dera Ghazi Khan', 'Pakistan');
    """
    db.insert(sql)
    
    sql = """
            INSERT INTO products(name, price, description)
            VALUES
                ('Facial Skin Care', 5.0, 'Awesome product to use for facial.'),
                ('Synology Storage', 25.0, 'Product with storing network attached data.');
    """
    db.insert(sql)
    
    sql = """
            INSERT INTO orders(customer_id, product_id, quantity, price)
            VALUES
                (1, 1, 25, 35.55),
                (1, 2, 12, 45);
    """
    db.insert(sql)

   

    #print db





if __name__ == '__main__':
    main()    
