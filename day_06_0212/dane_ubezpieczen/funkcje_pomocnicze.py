"""
funkcje dodatkowe do programu

"""
import pickle

print(f"Importowane funkcje - {__name__}")


def save_file(data: dict, file_name: str) -> bool:
    with open(file_name, "wb") as file:
        pickle.dump(data, file)
    return True


def add_insured(template: dict) -> dict:
    if not isinstance(template, dict):
        return False

    new_dict = {}
    for any_key in template:
        new_value = input(f"Enter a value for {any_key}: ")
        new_dict[any_key] = new_value

    return new_dict


if __name__ == "__main__":
    print("To plik tylko do zaimportowania")
