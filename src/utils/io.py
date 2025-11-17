import json


def load_prompts(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def save_results(file_path, results):
    with open(file_path, "w") as file:
        for result in results:
            file.write(f"{result}\n")


def save_to_json(data: dict, file_path: str):
    """
    Saves a dictionary to a JSON file.

    Args:
        data (dict): The dictionary to save.
        file_path (str): The path to the JSON file.
    """
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
