import MySQLdb
import sys
import time
import os
import subprocess

############# Removing database warnings #############
from warnings import filterwarnings
import MySQLdb as Database
filterwarnings('ignore', category = Database.Warning)


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

  def create(self, sql):
    try:
      return self.cursor.execute(sql)
    except MySQLdb.Error, e:
      print "ERROR: %d: %s" % (e.args[0], e.args[1])
  
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

  def delete(self,sql):
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
    
    try:
      subprocess.call("mysqldump -u root -h 127.0.0.1 -P 3306 pythontest > backup.sql",shell=True)
    except Exception as e:
      print e

  def restore(self):
    try:
      subprocess.call("mysql -u root -h 127.0.0.1 -P 3306 yabargoon < backup.sql",shell=True)            
    except Exception as e:
      print e
      
    
def main():
  db = Database(name='pythontest')
  
##  q = raw_input("Do You want to create New Database(Yes/No)?")
##  if q.lower() == 'yes':
##    name = raw_input("Please enter the Database name:")
##    db = Database(name)
  
     
# Create Table Customers
  table = "customers"
  sql = """
      CREATE TABLE IF NOT EXISTS {} (
        id int NOT NULL AUTO_INCREMENT,
        first_name  VARCHAR(50),
        last_name   VARCHAR(50),
        phone       VARCHAR(15),
        email       VARCHAR(100),
        address     VARCHAR(150),
        country     VARCHAR(30),
        PRIMARY KEY(id)
      )
  """.format(table)

  msg = "Table {} Created successfully.".format(table) if db.create(sql) else "Table {} already exists.".format(table)
  print msg   
  
# Create Table Products
  table = "products"
  sql = """
      CREATE TABLE IF NOT EXISTS {}(
        id int NOT NULL AUTO_INCREMENT,
        name        VARCHAR(50),
        price       FLOAT(11,2),
        description TEXT,
        PRIMARY KEY(id) )
  """.format(table)
  
  msg = "Table {} Created successfully.".format(table) if db.create(sql) else "Table {} already exists.".format(table)
  print msg   
  
# Create Table Orders
  table = "orders"
  sql = """
      CREATE TABLE IF NOT EXISTS {} (
        id int NOT NULL AUTO_INCREMENT,
        customer_id INT(11),
        product_id INT(11),
        quantity INT(11),
        price FLOAT(11,2),
        PRIMARY KEY(customer_id, product_id),
        KEY(id)
      )
  """.format(table)
  
  msg = "Table {} Created successfully.".format(table) if db.create(sql) else "Table {} already exists.".format(table)
  print msg
  
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

#   Delete database
  sql = """
      DROP DATABASE pythontest
  """
  db.get_dump()
  #db.delete(sql)

  db = Database(name='pythontest')
  db.restore()


if __name__ == "__main__":
  main()    
