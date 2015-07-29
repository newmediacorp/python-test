import MySQLdb
import sys
import time
import os
import subprocess
import cmd
import git
from git import *

############# Removing database warnings #############
from warnings import filterwarnings
import MySQLdb as Database
filterwarnings('ignore', category = Database.Warning)


class Database(cmd.Cmd):
    __host = '127.0.0.1'
    __user = 'root'
    __password = '123456'
    __port = 3306
    __database = 'pythontest'
    
    """Function that hits the MySQL database table Orders.
        returns dictionary for all the rows in the table.	
    """
    def get_dictionary(self, table='orders'):
        import MySQLdb.cursors
        conn = MySQLdb.connect(host=self.__host, port=self.__port, user=self.__user, passwd=self.__password, db=self.__database, cursorclass=MySQLdb.cursors.DictCursor)
        cursor = conn.cursor()
        cursor.execute("SELECT * from {}".format(table))
        return cursor.fetchall()

    """Invokes get_dictionary() for orders table
        then converts to yaml
    """
    def dictionary_to_yaml(self):        
        import yaml
        data = self.get_dictionary()    
        orders_list = []

    #   Converting values with L(long) from db to int
        for dic in data:
          d = {}
          for k,v in dic.items():                
            d[k] = int(dic[k]) if type(dic[k]) == long else dic[k]
          orders_list.append(d)

        """Checks if the folder ./out already exists.
        If not creates one.
        """
        directory = './out'		
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Writing output to orders.yaml file
        with open(os.path.join(directory,'orders.yml'), 'w') as yaml_file:
            yaml_file.write( yaml.dump(orders_list, default_flow_style=False))

    def do_build(self, line):
        self.dictionary_to_yaml()

    """
        Creates the git tags.
        Checks if the tag with the same name is already created.
        If not creates new one with the given name.
    """
    def do_release(self, line):
        repo = Repo('.')
        tags = repo.tags
        tag_name = raw_input("Please Enter a tag name to Create:")
        new_tag = tag_name
        if new_tag not in tags:
            repo.create_tag(new_tag, message='V2.0')
            repo.git.push(tags=True)
        else:
            print "Tag already exists with the same name"

        """Deleting tags"""
#        for tag in tags:
#            print tag
#            tagref = tag.tag
#            print tagref
            #repo.delete_tag(tagref)
    """
    Function to deploy the code to github. It executes following commands
    1- git init .
    2- git add --all
    3- git commit -m "Database Dump 1"
    4- git push origin
    """	
#    def do_deploy(self, line):
#        repo_dir = os.path.join(os.path.dirname(__file__), './')
#        repo = git.Repo.init(repo_dir)
#        print repo
#        repo = git.Repo(repo_dir, search_parent_directories=True)
#        print repo.git.status()
#        # add all files
#        print repo.git.add('*')
#        # commit
#        print repo.git.commit(message='Database Dump 2' )
#        # now we are one commit ahead
#        print repo.git.status()
#
#        #here is the new change
#        repo.git.push()

    def do_deploy(self, line):        
        git_url = raw_input("Please enter the clone URL: ")
        directory = git_url.rsplit('/',1)[1].split('.')[0]		
        if not os.path.exists('./out'+directory):
            os.makedirs('./out/'+directory)
        repo_dir = os.path.join(os.path.dirname(__file__), './out/'+directory)
        from git import Repo
        Repo.clone_from(git_url, repo_dir)
        # TODO rename
        print "Clone Successful"
        
    def do_EOF(self, line):
        return True


def main():
    d = Database()
    # d.do_get_dictionary()
    d.do_dictionary_to_yaml()

if __name__ == '__main__':
    # main()
    Database().cmdloop()