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

    def query(self, statement):
        if not self.connected:
            return False
        self.lock.acquire()
        cur = self.__cursor()
        if not cur:
            self.lock.release()
            return False
        cur.execute(statement)
        result = cur.fetchall()
        cur.close()
        self.lock.release()
        return result

    def execute(self, statement):
        if not self.connected:
            return False
        self.lock.acquire()
        cur = self.__cursor()
        if not cur:
            self.lock.release()
            return False
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
    #     delete from translation;
    # """)

    # db.execute("""drop table translation""")
