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
