import json

def generate_json(name, description, image, tags, price):
    """Создание структуры для способностей, запарсим где-нибудь (Саня будет писать руками)"""
    return {
        name: {
            "description": description,
            "image": image,
            "tags": tags,
            "price": price
        }
    }

def get_json_data(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return {name: info for name, info in data.items()}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def update_json(filename, json_data):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    data.update(json_data)
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return data
'''Вроде рабочая темка'''

def edit_data(filename, key, new_value):
    data = get_json_data(filename)
    if key in data:
        data[key] = new_value
        with open(filename, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


# update_json("abi.json", generate_json("123","123","123","123","123"))
 