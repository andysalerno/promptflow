
from promptflow import tool
from promptflow.core import Prompty


@tool
def my_python_tool(prompty_path: str, user_input: str, chat_history: list) -> str:
    prompty = load_prompty(prompty_path)
    output = prompty(chat_history=chat_history, user_input=user_input)

    return output

def load_prompty(prompty_path: str) -> Prompty:
    return Prompty.load(source=prompty_path)
