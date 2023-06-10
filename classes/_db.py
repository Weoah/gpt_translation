from threading import Lock
import sqlite3


class Database:

    def __init__(self) -> None:
        self.connected: bool = False
        self.lock: Lock = Lock()
        self.__connect()

    def __connect(self):
        self.db = sqlite3.connect('db.sqlite3')
        self.connected = True

    def __close(self):
        self.db.close()
        self.connected = False

    def __cursor(self):
        if self.connected:
            return self.db.cursor()
        return False

    def __start(self):
        if not self.connected:
            return False
        cur = self.__cursor()
        if not cur:
            return False
        return cur

    def query(self, statement: str):
        cur = self.__start()
        self.lock.acquire()
        cur.execute(statement)
        result = cur.fetchall()
        cur.close()
        self.lock.release()
        if not result:
            return False
        return result

    def execute(self, statement: str, values: tuple | None = None):
        cur = self.__start()
        self.lock.acquire()
        if values is not None:
            cur.execute(statement, values)
        else:
            cur.execute(statement)
        self.db.commit()
        cur.close()
        self.lock.release()
        return True


db = Database()

if __name__ == "__main__":
    ...
    # db.execute("""
    #     create table translation
    #     (id integer primary key autoincrement,
    #     key varchar(255),
    #     value longtext)
    # """)
    # db.execute("""
    #     create table unstranslated
    #     (id integer primary key autoincrement,
    #     key varchar(255),
    #     value longtext)
    # """)

    # db.execute("""
    #     delete from translation;
    # """)
    # db.execute("""
    #     delete from unstranslated;
    # """)

    # db.execute("""drop table translation""")
