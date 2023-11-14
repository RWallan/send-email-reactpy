from pydantic import BaseModel, EmailStr


class PersonData(BaseModel):
    firstName: str
    secondName: str
    email: EmailStr


class OutputMessage(BaseModel):
    detail: str
