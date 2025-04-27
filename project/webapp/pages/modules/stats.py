import json

def vercheck():
    with open("pages/static/db/stat.json", "r") as file:
        data = json.load(file)
    return data["Data version"] == data["Overwatch version"], data["Data version"]