from pydantic import BaseModel, EmailStr


class PersonData(BaseModel):
    firstName: str
    secondName: str
    email: EmailStr
