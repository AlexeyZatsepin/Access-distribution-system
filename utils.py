from Connector import Connenct


def createDict(cursor):
    data = cursor.fetchone()
    if data == None:
        return None
    desc = cursor.description
    dict = {}
    for (name, value) in zip(desc, data):
        dict[name[0]] = value
    return dict


class switch(object):
    value = None

    def __new__(class_, value):
        class_.value = value
        return True


def case(*args):
    return any((arg == switch.value for arg in args))


def count_in_file():
    users_list = [line.rstrip('\n') for line in open('base.txt')]
    return users_list.__len__()

def count_in_base():
    with Connenct() as cursor:
        query = "SELECT id,login,password,blocked,laws FROM User;"
        response = cursor.execute(query)
        return len(response.fetchall())


