# coding=utf-8
from Connector import Connenct
from utils import createDict
from sqlite3 import OperationalError
from utils import switch, case
from termcolor import colored
from User import User, view_user_list
import csv
import time


class Context(object):
    def __init__(self, type, User):
        self.type = type
        self.user = User

    def __str__(self):
        return self.type +' '+ self.user.login


def identification(login, password):
    with Connenct() as cursor:
        query = "SELECT login FROM User WHERE password='%s'AND login='%s'" %(password,login)
        try:
            response=cursor.execute(query)
        except OperationalError:
            raise SystemExit("You just tried use sql injection")
        logins = createDict(response)
        if logins is None:
            return False
        token=list()
        token.append(login)
        if logins.values() == token:
            query="SELECT laws FROM User WHERE login='%s' AND password= '%s'" %(login,password)
            response=cursor.execute(query)
            logs=createDict(response)
            admin_laws=list()
            admin_laws.append(1)
            if logs.values()==admin_laws:
                user=User(login,password,1)
                context=Context('admin',user)
                return context
            else:
                query = "SELECT blocked FROM User WHERE password='" + password + "'AND login='"+login+"'"
                response=cursor.execute(query)
                logs=createDict(response)
                blocked=list()
                blocked.append(1)
                if logs.values()==blocked:
                    raise SystemExit("You are blocked by admin, please contact him")
                user=User(login,password,0)
                context=Context('common',user)
                return context
        else:
            return False


def admin(context):
    global i
    while True:
        print colored("Admin session", 'yellow')
        print "1.Change own password"
        print "2.Print users list"
        print "3.Create new user with blank password"
        print "4.Block user"
        print "5.Unblock user"
        print "6.Write user list in csv"
        print "7.Exit"
        try:
            i = input('Enter number:')
        except SyntaxError:
            print "Please retype number"
        while switch(i):
            if case(1):
                context.user.change_own_password()
                break
            if case(2):
                view_user_list()
                break
            if case(3):
                try:
                    new_user_login = input("Enter new users login:")
                except:
                    print colored("Reminder : string have format 'string'", 'red')
                    break
                new_user = User(new_user_login, ' ')
                new_user.create()
                print "Successful creation %s" % new_user
                break
            if case(4):
                try:
                    id = input("Enter user_id:")
                except:
                    print colored("Reminder : string have format 'string'", 'red')
                    break
                context.user.user_blocker(id, 'block')
                break
            if case(5):
                try:
                    id = input("Enter user_id:")
                except:
                    print colored("Reminder : string have format 'string'", 'red')
                    break
                context.user.user_blocker(id, 'unblock')
                break
            if case(6):
                with open('logs.csv', 'wb') as csvfile:
                    writer = csv.writer(csvfile, dialect='excel', quotechar='"', quoting=csv.QUOTE_ALL)
                    user_list = view_user_list()
                    writer.writerows(user_list)
                break
            if case(7):
                raise SystemExit
            print "Please retype number"
            break


def user(context):
    global i
    while True:
        print "User session, other functions are permitted"
        print "1.Change password"
        print "2.Exit"
        try:
            i = input('Enter number:')
        except SyntaxError:
            print "Please retype number"
        while switch(i):
            if case(1):
                context.user.change_own_password()
                break
            if case(2):
                raise SystemExit
            print "Please retype number"
            break


def main():
    global i, fails
    fails = 0
    while True:
        print "1.Authorization"
        print "2.Help"
        print "3.Exit"
        try:
            i = input('Enter number:')
        except SyntaxError:
            print colored("Please enter valid number", 'red')
        while switch(i):
            if case(1):
                try:
                    login = str(input("Enter login:"))
                    password = str(input("Enter password:"))
                except:
                    fails += 1
                    print colored("Reminder : string have format 'string'", 'red')
                    if fails == 3:
                        time.sleep(5)
                        raise SystemExit("Third identification is failed")
                context = identification(login, password)
                if not context:
                    fails += 1
                    print colored("Password or login isn't valid", 'red')
                    if fails == 3:
                        time.sleep(5)
                        raise SystemExit("Third identification is failed")
                else:
                    context.user.authorization(login, password)
                    if context.type == 'admin':
                        admin(context)
                    elif context.type == 'common':
                        user(context)
                    else:
                        raise KeyError
            if case(3):
                raise SystemExit
            if case(2):
                print colored("Варіант 6.Зацепін Олексій ФБ-31", 'blue')
                print colored("     Наявність латинських букв, символів кирилиці і цифр.", 'blue')
            print colored("Please retype number", 'red')
            break
