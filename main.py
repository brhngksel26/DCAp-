from fastapi import FastAPI
import aiohttp

from model.contacts import Contacts
from model.people import People
from utils import clear_all_item_by_dict
import yaml


app = FastAPI()

config_file = open("config.yaml", "r")
config = yaml.load(config_file, Loader=yaml.FullLoader)

url = config["url"]
bearer_token = config["bearer_token"]
username= config["username"]
password= config["password"]

headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {bearer_token}'
    }

@app.get("/people")
async def people():
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f"{url}people") as response:
            result = await response.json()
    return result


@app.post("/contacts")
async def contacts(contacts: Contacts):
    contacts = clear_all_item_by_dict(contacts.dict())

    auth=aiohttp.BasicAuth(username, password)
    async with aiohttp.ClientSession(auth=auth) as session:
        async with session.post(f"{url}contacts", data=contacts) as response:
            result = await response.json()
    return result
