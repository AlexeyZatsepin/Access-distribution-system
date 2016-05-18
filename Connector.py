import portalocker as portalocker


class Connenct(object):
    def __enter__(self):
        import sqlite3
        self.connection = sqlite3.connect('test.db')
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


