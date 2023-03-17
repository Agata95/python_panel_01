import os
import uvicorn
from fastapi import FastAPI, HTTPException, Request

__PORT__ = os.getenv("APP_PORT", 5500)
app: FastAPI = FastAPI()


# endpoint w api
@app.get("/")
def fn_main():
    return {"opis": "nic"}


@app.get("/auth/{auth_id}")
def fn_auth(request: Request, auth_id: str):
    if not auth_id == 'TEST-OK':
        return HTTPException(status_code=401,
                             detail=f"AUTH Error for {auth_id} from {request.client.host}")
    return {"informacja": "Połączenie poprawne"}


if __name__ == "__main__":
    print(f"Start APP on port {__PORT__}")
    uvicorn.run(app, host="127.0.0.1", port=int(__PORT__))
