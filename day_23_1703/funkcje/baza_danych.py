from random import randint
from secrets import token_hex
from sqlite3 import *
import os


# https://sqlitebrowser.org/

def generate_token(long=12):
    if not isinstance(long, int):
        long = 12
    return token_hex(long)


def create_user_record(db, user, token):
    field_1 = "name"
    field_2 = "password"
    new_values = (user, token)
    if os.path.exists(db):
        try:
            connection = connect(db)
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO users ({field_1},{field_2}) VALUES (?,?)', new_values)
            connection.commit()
            connection.close()
            return True
        except:
            return False
    else:
        return False


def check_user_passwd(db, name, token):
    if os.path.exists(db):
        connection = connect(db)
        cursor = connection.cursor()
        result = cursor.execute(f"SELECT * FROM users WHERE name=?", (name,))
        rekordy = result.fetchall()
        if len(rekordy) != 1:
            connection.close()
            return False

        _, db_user, db_token = rekordy[0]
        if db_user == name and db_token == token:
            ret = True
        else:
            ret = False
        connection.close()
        return ret
    else:
        return False


def client_info(db, client_id=None):
    if os.path.exists(db):
        connection = connect(db)
        cursor = connection.cursor()
        if client_id:
            result = cursor.execute(f"SELECT * FROM clients WHERE id=?", (client_id,))

        else:
            result = cursor.execute(f"SELECT * FROM clients")
            res_ret = {}
            for each_client in result.fetchall():
                res_ret[each_client[1]] = f"http://127.0.0.1:5500/client/{each_client[0]}"

            connection.close()
            return res_ret

        client_data = result.fetchall()[0]
        connection.close()

        return {
            "Returned data about": client_data[1],
            "Salary": client_data[2],
            "Update salary with random": f"http://127.0.0.1:5500/client_update/{client_data[0]}?new_salary={randint(20, 3000)}"
        }

    else:
        return False


def check_database(db: str) -> bool:
    if os.path.exists(db):
        return True
    else:
        return False


def client_salary_update(db: str, id: int, new_salary: int):
    if os.path.exists(db):
        connection = connect(db)
        cursor = connection.cursor()
        cursor.execute(f"UPDATE clients SET Salary=? WHERE id=?", (new_salary, id))
        connection.commit()
        connection.close()
        return True

    else:
        return False
