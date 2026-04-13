from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    with open(file_name, "r") as file:
        data = json.load(file)
    keys = ["unordered_numbers", "ordered_numbers", "dna_sequence"]
    for key in data:
        if key != field:
            return None
        else:
            vystup = data.get(field)
            return vystup

    # get current working directory path

    cwd_path = Path.cwd()

    file_path = cwd_path / file_name

def linear_search(sekvence, hledane_cislo):
    slovnik = {}
    seznam = []
    count = 0
    for i in range(len(sekvence)):
        if sekvence[i] == hledane_cislo:
            seznam.append(i)
            count += 1
    slovnik["positions"] = seznam
    slovnik["count"] = count
    return slovnik

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    print(linear_search([1, 2, 3, 4], 2))
    pass


if __name__ == "__main__":
    main()
