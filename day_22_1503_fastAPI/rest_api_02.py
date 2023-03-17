import os
import uvicorn
from fastapi import FastAPI, HTTPException, Request, status, Response

__PORT__ = os.getenv("APP_PORT", 5500)
app: FastAPI = FastAPI()


# endpoint w api
@app.get("/")
def fn_main():
    return {"opis": "nic"}


@app.get("/auth/{auth_id}")
def fn_auth(request: Request, auth_id: str):
    if not auth_id == 'TEST-OK':
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail=f"AUTH Error for {auth_id} from {request.client.host}")
    return {"informacja": "Połączenie poprawne"}


@app.get("/auth/v2/{auth_id}", status_code=status.HTTP_202_ACCEPTED)
def fn_auth(request: Request, response: Response, auth_id: str):
    if not auth_id == 'TEST-OK':
        response.status_code = status.HTTP_410_GONE
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                             detail=f"AUTH Error for {auth_id} from {request.client.host}")
    return {"informacja": "Połączenie poprawne"}


if __name__ == "__main__":
    print(f"Start APP on port {__PORT__}")
    uvicorn.run(app, host="127.0.0.1", port=int(__PORT__))
