from pydantic import BaseModel

class CustomProperties(BaseModel):
    airtable_id: str
    lifetime_value: float

class Contacts(BaseModel):
    first_name: str
    last_name: str
    birthdate: str  
    email: str
    custom_properties: CustomProperties
