# from fastapi import FastAPI, HTTPException, Response, Depends
# from authx import AuthX, AuthXConfig
#
# from pydantic import BaseModel
#
#
# app=FastAPI()
# config = AuthXConfig()
# config.JWT_SECRET_KEY="SECRET_KEY"
# config.JWT_ACCESS_COOKIE_NAME = "my_access_token" # название нашего токена
# config.JWT_TOKEN_LOCATION = ["cookies"]
#
# security = AuthX(config=config)
#
# class UserloginSchema(BaseModel):
#     username: str
#     password: str
#
#
# @app.post("/login")  # авторизация пользователя (который уже зарегистрирован)
# def login(credentials: UserloginSchema, response: Response):
#     if credentials.username=="test" and credentials.password=="test":
#         token=security.create_access_token(uid="12345")
#         response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token) #отправим в куки token
#         return {"access_token": token}
#     raise HTTPException(status_code=404, detail = "Incorrect username or password")
#
#
# @app.get("/protected", dependencies=[Depends(security.access_token_required)]) # тут будет проверка,
# def protected():
#     return {"data": "TOP SECRET"}


from fastapi import FastAPI, HTTPException, Response, Depends
from authx import AuthX, AuthXConfig
from pydantic import BaseModel

config = AuthXConfig()  # создаем класс config, чтобы из него взять параметры (настройки)
config.JWT_SECRET_KEY = "SECRET_KEY"  # позволяет создавать jwt-токены
config.JWT_ACCESS_COOKIE_NAME = "my_access_token"  # указаь название нашего токена
config.JWT_TOKEN_LOCATION = ["cookies"]  # укажем, что у нас JWT будет храниться в куках

security = AuthX(config=config)  # создаем екземпляр класса AuthX с использованием config-ов

app = FastAPI()


class UserloginSchema(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(credentials: UserloginSchema, response: Response):
    if credentials.username == "test" and credentials.password == "test":
        token = security.create_access_token(uid="12345")  # создать токен
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)  # передаем в ответ COOKIE_NAME и сам токен
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")


@app.get("/protected", dependencies=[Depends(security.access_token_required)])  # требоваие access_token
def protected():
    return {"data": "TOP SECRET"}
