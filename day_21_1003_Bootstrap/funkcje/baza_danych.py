from secrets import token_hex
from sqlite3 import *
import os


# https://sqlitebrowser.org/

def generate_token(long=12):
    if not isinstance(long, int):
        long = 12
    return token_hex(long)


def create_user_record(db, user, token):
    field_1 = "mail"
    field_2 = "token"
    new_values = (user, token)
    if os.path.exists(db):
        try:
            connection = connect(db)
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO userdata ({field_1},{field_2}) VALUES (?,?)', new_values)
            connection.commit()
            connection.close()
            return True
        except:
            return False
    else:
        return False


def check_mail(db, mail, token):
    table = "userdata"
    if os.path.exists(db):
        connection = connect(db)
        cursor = connection.cursor()
        result = cursor.execute(f"SELECT * FROM {table} WHERE token=?", (token,))
        rekordy = result.fetchall()
        # print("--->>", len(rekordy), rekordy)
        if len(rekordy) != 1:
            connection.close()
            return False

        _, db_mail, db_token = rekordy[0]
        if db_mail == mail and db_token == token:
            ret = True
        else:
            ret = False
        connection.close()
        return ret
    else:
        return False
