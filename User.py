# coding=utf-8
from Connector import Connenct
from utils import *


def password_is_valid(password):
    import re
    if re.match(r'^[A-Za-z0-9а-яА-я]+$', password) is not None:
        return True
    else:
        from termcolor import colored
        print colored("The presence of Latin letters, сyrillic characters and numbers.", "cyan")
        return False


def view_user_list():
    with Connenct() as cursor:
        query = "SELECT id,login FROM User;"
        response = cursor.execute(query)
        tempDict = response.fetchall()
        from termcolor import colored
        print colored('id login', 'blue')
        for id, login in tempDict:
            print colored(str(id) + ' ' + login, 'green')
        return tempDict


class User(object):
    def create(self):
        with Connenct() as cursor:
            query = "INSERT INTO History(what,who) VALUES ('create user','" + self.session_id + "')"
            cursor.execute(query)
            query = "INSERT INTO User(login,password,laws,blocked) VALUES ('" + self.login + "','" + self._password + "','" + str(
                self._laws) + "','" + str(self.__blocked) + "')"
            cursor.execute(query)

    def __init__(self, login, _password, _laws=0, __blocked=0):
        self.login = login
        self._password = _password
        self._laws = _laws
        self.__blocked = __blocked
        self.session_id = ''

    def authorization(self, login, password):
        self.login = login
        self._password = password
        with Connenct() as cursor:
            query = "SELECT laws FROM User WHERE login='" + login + "' AND password= '" + password + "'"
            response = cursor.execute(query)
            tempDict = createDict(response)
            from datetime import datetime
            self.session_id = str(tempDict.values()[0]) + ' ' + str(datetime.now()) + ' ' + self.login
            self._law = tempDict.values()[0]

    def __str__(self):
        return self.login

    def change_own_password(self):
        global new_password1, new_password2, old_password
        while True:
            try:
                old_password = input("Enter old password:")
                new_password1 = input("Enter new valid password:")
                new_password2 = input("Repeat new password:")
            except SyntaxError:
                print "Print valid values"
            except UnboundLocalError:
                print "Print valid values"
            except NameError:
                print "Print valid values"
            if not password_is_valid(new_password1):
                from termcolor import colored
                print colored("Password isn't valid", 'red')
            elif new_password1 == new_password2 and old_password == self._password:
                with Connenct() as cursor:
                    query = "INSERT INTO History(what,who) VALUES ('change own password','" + self.session_id + "')"
                    cursor.execute(query)
                    query = "UPDATE User SET password='" + new_password1 + "' WHERE login='" + self.login + "';"
                    cursor.execute(query)
                    print "Successful change"
                    return True
            else:
                pass

    def user_blocker(self, id, value):
        with Connenct() as cursor:
            if value == 'block':
                query = "INSERT INTO History(what,who) VALUES ('block user" + str(id) + "','" + self.session_id + "')"
                cursor.execute(query)
                query = "UPDATE User SET blocked='1' WHERE id='" + str(id) + "'"
                cursor.execute(query)
                return self
            elif value == 'unblock':
                query = "INSERT INTO History(what,who) VALUES ('unblock user" + str(id) + "','" + self.session_id + "')"
                cursor.execute(query)
                query = "UPDATE User SET blocked='0' WHERE id='" + str(id) + "'"
                cursor.execute(query)
                return self
            else:
                raise StandardError
