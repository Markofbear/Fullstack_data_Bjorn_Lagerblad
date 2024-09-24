import duckdb

#implements context manager protocol
class Database:
    def __init__(self, db_path) -> None:
        self.db_path=db_path
        self.connection = None

    def __enter__(self):
        print ("Enters database")
        # connection to db
        self.connection = duckdb.connect(self.db_path)
        return self

    def query(self,query):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exits database")
        #close connection to db
        if self.connection:
                self.connection.close()

with Database() as db:
    print ("inside with statement")
    print("still inside with statement")

print("outside with statement")

