from pydantic import BaseModel

class Fields(BaseModel):
    firstName: str
    lastName: str
    dateOfBirth: str  
    email: str
    lifetimeValue: str 

class People(BaseModel):
    id: str
    fields: Fields
