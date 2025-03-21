from pydantic import BaseModel, Field, EmailStr, ConfigDict
from fastapi import FastAPI


app = FastAPI()
data = {
    "email": "abc@gmail.com",
    "bio": None,
    "age": 12,
}


data_w_age = {
    "email": "abc@gmail.com",
    "bio": None,
    # "gender": "mail",
    # "birthday": "2022",
}


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)

    model_config = ConfigDict(extra="forbid")


# user= UserSchema(**data_w_age)

users = []


@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return {"ok": True, "message": "Юзер добавлен"}


@app.get("/users")
def get_users() -> list[UserSchema]:
    return users


# class UserAgeSchema(UserSchema):
#      age: int =Field(ge=0, le=130)
#
# user = UserAgeSchema(**data)
# print(repr(user)) # оборачиваем в  repr, чтобы видеть название класса
#
# user= UserSchema(**data_w_age)
# print(repr(user))
# def func(data:dict):
#     data["age"]+=1

# if __name__=="__main__":
#     uvicorn.run("main_pydantic:app", reload=True)
