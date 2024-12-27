import json
from typing import Optional


def read_all_identifiers():
    with open('./AllIdentifiers.json') as f:
        data = json.load(f)
    return data

def make_card_lookup(data) -> dict:
    values = iter(data.values())

    return {card["uuid"]: card for card in values}

def transform_data(input):
    data: dict = input["data"]
    values = iter(data.values())

    output = []

    for card in values:
        if card["setCode"] == 'FDN':
            output.append({"name": card["name"], "uuid": card["uuid"], "cardText": card["text"] if "text" in card else ""})

    return output

def find_scryfall_id_by_id(lookup: dict, uuid: str) -> str:
    return lookup[uuid]['identifiers']["scryfallId"]

def get_lookup():
    content = read_all_identifiers()
    data: dict = content["data"]
    lookup = make_card_lookup(data)

    return lookup

def read_events_jsonl(path: str) -> list:
    with open(path) as f:
        lines = f.readlines()
    return [json.loads(line) for line in lines]

if __name__ == "__main__":
    lookup = get_lookup()
    all_events = read_events_jsonl('/root/.promptflow/.runs/mtgflow_variant_0_20241226_210525_814587/flow_outputs/output.jsonl')

    with open("./fdn_output.jsonl", "w") as f:

        for event_obj in all_events:
            output = event_obj['output']
            output['mtgjson_uuid'] = event_obj['card_uuid']
            output['card_name'] = event_obj['card_name']
            output['card_text'] = event_obj['card_text']
            output["scryfall_id"] = find_scryfall_id_by_id(lookup, event_obj["card_uuid"])
            del output['simplified_text']
            f.write(json.dumps(output) + "\n")


    # outputs = transform_data(data)
    # # write outputs as jsonl file
    # with open("./card_texts_fdn.jsonl", "w") as f:
    #     for output in outputs:
    #         f.write(json.dumps(output) + "\n")