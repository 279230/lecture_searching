from pathlib import Path
import json
import random
import time
import matplotlib.pyplot as plt

from generators import unordered_sequence, ordered_sequence


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

    if field not in keys:
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


def binary_search(seznam_cislo, hledane_cislo):
    left = 0
    right = len(seznam_cislo) -1

    while left <= right:

        middle = (left + right)// 2

        if seznam_cislo[middle] == hledane_cislo:
            return middle
        elif seznam_cislo[middle] < hledane_cislo:
            left = middle+1
        else:
            right = middle -1
    return None



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    print(linear_search(sequential_data, 3))
    seznam = read_data("sequential.json", "ordered_numbers")
    print(seznam)
    print(binary_search(seznam, 2))


"""
def main():
    velikosti = [100, 500, 1000, 5000, 10000]
    sekvencni_cas = []
    binarni_cas = []

    for vlastnost in vlastnosti:
        neserazeny = unordered_sequence(max_len=100)
        serazeny = ordered_sequence(max_len = 100)

        hledana = serazeny(len(serazeny)//2)
        start = time.perf_counter()
        linear_search(neserazeny, hledana)
        end = time.perf_counter()
        sekvencni_cas.append(end-start)
"""

if __name__ == "__main__":
    main()
