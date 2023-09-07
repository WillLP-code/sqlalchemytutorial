# cd /workspaces/sqlalchemytutorial/database
# sqlite3 chinook.db

from sqlalchemy import create_engine, inspect
engine = create_engine("sqlite+pysqlite:////workspaces/sqlalchemytutorial/database/chinook.db", echo=True, future=True) #connection string with details to connect to db

connection = engine.connect()
inspection = inspect(engine)
print(inspection.get_table_names())