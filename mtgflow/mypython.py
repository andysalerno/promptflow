from promptflow import tool
from promptflow.core import Prompty


@tool
def my_python_tool(prompty_path: str, card_text: str, card_uuid: str) -> str:
    prompty = load_prompty(prompty_path)
    output = prompty(card_text=card_text)

    return output

def load_prompty(prompty_path: str) -> Prompty:
    return Prompty.load(source=prompty_path)
