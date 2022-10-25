from desafiolunarapi.infra.db import minerios
from datetime import datetime

def all():
    return minerios


def bind_minerio(data):
    return {
        "id": data["id"],
        "name": data["name"],
        "description": data["description"],
        "last_update_date": data["last_update_date"],
    }

def find_by_id(id):

    data = [item for item in minerios if id == item['id']]

    if data == []:
        return None

    return {k: v for k, v in data[0].items()
            if k in ['id', 'name', 'description']}

def get_date_time(now): return now.strftime("%Y-%m-%d %H:%M:%S")

def create_id(data): return data[-1]["id"] + 1

def create(data: dict) -> None:

    "Executa o cadastro de minério"

    minerios.append({
        "id": create_id(minerios),
        "name": data["name"],
        "description": data["description"],
        "register_date": get_date_time(datetime.now()),
        "last_update_date": None
    })


def edit(id, data):

    for dic in minerios:
        if id == dic["id"]:
            dic["name"] = data["name"]
            dic["description"] = data["description"]


def remove(id):
    for item in minerios.copy():
        if item.get('id') == id:
            minerios.remove(item)
            break
