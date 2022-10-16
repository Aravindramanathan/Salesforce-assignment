import sqlite3

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('Assignment.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from Favouritemovies"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Movie name: ", row[0])
            print("Actor: ", row[1])
            print("Actress: ", row[2])
            print("Year: ", row[3])
            print("Direcor: ", row[4])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()