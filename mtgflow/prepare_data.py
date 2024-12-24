import json


def read_all_identifiers():
    with open('./AllIdentifiers.json') as f:
        data = json.load(f)
    return data

def transform_data(input):
    data: dict = input["data"]
    values = iter(data.values())

    output = []

    for card in values:
        output.append({"name": card["name"], "uuid": card["uuid"], "cardText": card["text"] if "text" in card else ""})

    return output

if __name__ == "__main__":
    data = read_all_identifiers()
    outputs = transform_data(data)

    # write outputs as jsonl file
    with open("./card_texts.jsonl", "w") as f:
        for output in outputs:
            f.write(json.dumps(output) + "\n")