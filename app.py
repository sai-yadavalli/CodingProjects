import sqlite3

def exerciseOne():
    try:
        ### Exercise 1
        connection = sqlite3.connect('python_db.db')
        cursor = connection.cursor()
        print("Successfully Connected to Database")
        query = "SELECT sqlite_version();"
        cursor.execute(query)
        result = cursor.fetchone()
        print("Version number: ")
        print(result)
        connection.commit()
        cursor.close()

        return result

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if (connection):
            connection.close()
            print("The SQLite connection is closed")
exerciseOne()