import logging
from icecream import ic

def zapis_dziennika(info: str):
    logging.info(info)

# do pliku od poziomu INFO
logging.basicConfig(filename="errory.log", filemode="a", level=logging.INFO)

logging.info("Jakiś błąd")
ic.configureOutput(outputFunction=zapis_dziennika)
ic(print(2+3))