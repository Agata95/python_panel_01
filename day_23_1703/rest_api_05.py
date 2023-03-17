import os
import sys
import uvicorn
from fastapi import FastAPI, HTTPException, Request, status, Response
from funkcje.baza_danych import check_database, generate_token, create_user_record, check_user_passwd, client_info

__PORT__ = os.getenv("APP_PORT", 5500)
DB = "baza_api.db"
app: FastAPI = FastAPI()


@app.get("/")
def fn_main():
    return {"opis": "Serwis 'transakcyjny'",
            "/create_user/{user_name}?token_lenght=22": "Stworzymy usera, hasło i zapiszemy do bazy",
            "/verification/{user_name}/{password}": "Weryfikacja poprawności hasła",
            "/clients/": "Wszyscy klienci"
            }


@app.get("/create_user/{user_name}")
def create_user(user_name: str, token_length: int = 7):
    new_token = generate_token(token_length)
    if create_user_record(DB, user_name, new_token):
        return {"CREATED": "OK",
                "new password": new_token}
    else:
        HTTPException(status_code=status.HTTP_205_RESET_CONTENT,
                      detail=f"Creation error for {user_name}")


@app.get("/verification/{user_name}/{password}")
def fn_verify(user_name: str, password: str, response: Response):
    if not check_user_passwd(DB, user_name, password):
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail="USER verification ERROR")
    else:
        return {"Verification": "OK"}


@app.get("/clients/")
def fn_all_clients():
    info = client_info(DB)
    return info


if __name__ == "__main__":
    if not check_database(DB):
        print("Database init error!")
        sys.exit(2)

    print(f"Start APP on port {__PORT__}")
    uvicorn.run(app, host="127.0.0.1", port=int(__PORT__))
