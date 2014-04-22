"""
This module caters all the database related classes

Contains
=======

* DatabaseConnection

Author: Sudhanshu Mishra
"""


from __future__ import division, print_function

import time
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

    def get_current_rate(share_code):
        """
        This method returns the current rate of the stock
        in the market.
        It takes share_code as a parameter and returns its
        current rate as a float.

        """

        with self.db:
            cur = self.db.cursor()
            query = "SELECT `current_rate` FROM market WHERE `share_code` = " + \
                share_code
            cur.execute(query)
            data = cur.fetchone()
            return data[0]

    def add_purchase(share_code, purchase_rate):
        """
        This method inserts a purchase transaction in the purchase
        table. It takes share_code and purchase_rate as parameters
        and return nothing.

        """

        with self.db:
            cur = self.db.cursor()
            query = "INSERT INTO purchase VALUES(" + share_code + \
                ", " + purchase_rate + ", " + time.ctime() + ")"
            cur.execute(query)

    def delete_purchase(share_code):
        """
        This method deletes a purchase record from the purchase
        table. It takes share_code as a parameter and returns nothing.

        """

        with self.db:
            cur = self.db.cursor()
            query = "DELETE FROM purchase WHERE share_code = " + share_code
            cur.execute(query)
