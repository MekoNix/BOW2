import json

def generate_json(name, description, image, tags, price):
    return {
        name: {
            "description": description,
            "image": image,
            "tags": tags,
            "price": price
        }
    }



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




# update_json("abi.json", generate_json("123","123","123","123","123"))
 