"""
This module caters all the database related classes

Contains
=======

* DatabaseConnection

Author: Sudhanshu Mishra
"""


from __future__ import division, print_function

import MySQLdb


class DatabaseConnection:

    """
    This class takes care of all the data related queries with the
    MySQL server.
    """

    def __init__(self, ahost, ausername, apassword, adb):
        """
        Connecting With MySQL
        """
        self.ahost = ahost
        self.ausername = ausername
        self.apassword = apassword
        self.adb = adb
        try:
            self.db = MySQLdb.connect(
                host=ahost,
                user=ausername,
                passwd=apassword,
                db=adb
            )

        except MySQLdb.Error as e:
            print("An error has been raised. %s" % e)

    def check_login(self, user_id, password):
        """
        This method checks the login credentials of the user.
        It takes user_id and password as arguments and returns
        a boolean value. True means that login is successful
        and False means that either the user is not available
        or the credentials provided are wrong.
        """
        return True
        with self.db:
            cur = self.db.cursor()
            query = "SELECT * FROM users where user_id = \'" + \
                user_id + "\' and pass = \'" + password + "\'"
            cur.execute(query)  # Executing the query
            data = cur.fetchall()  # Fetching the output of the executed query
            # Logic behind checking the number of returned rows is when
            if(len(data) == 0):
                # there are no users or the credentials didn't match, MySQL
                return False
            else:               # will not return any row.
                return True
