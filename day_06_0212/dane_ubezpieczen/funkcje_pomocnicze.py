"""
funkcje dodatkowe do programu

"""
import pickle

print(f"Importowane funkcje - {__name__}")


def zapis_pliku(dane: dict, nazwa_pliku: str) -> bool:
    with open(nazwa_pliku, "wb") as fp:
        pickle.dump(dane, fp)
    return True


def dodaj_ubezpieczonego(szablon: dict) -> dict:
    if type(szablon) is not dict:
        return False
    # bardziej poprawne i szybsze niż type()
    if not isinstance(szablon, dict):
        return False
    ret_dict = {}
    for any_key in szablon:
        new_value = input(f"Podaj wartość dla {any_key}: ")
        ret_dict[any_key] = new_value
    return ret_dict


if __name__ == "__main__":
    print("To plik tylko do zaimportowania")
