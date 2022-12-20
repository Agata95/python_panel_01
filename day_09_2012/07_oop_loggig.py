from icecream import ic
from datetime import datetime
import logging
# przykład użycia: https://github.com/abixadamj/aplikacja_epodreczniki_0416

# do pliku od poziomu INFO
logging.basicConfig(filename="oop_dziennik.log", filemode="a", level=logging.INFO)

# na ekran od ERROR
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

# do innego pliku CRITICAL
fh = open("oop_dziennik_critical.log", mode = 'a')
critical_file = logging.StreamHandler(fh)
critical_file.setLevel(logging.CRITICAL)
# add the handler to the root logger
logging.getLogger('').addHandler(critical_file)
def fn_test_ic(value: int) -> str:
    return "*" * value

def zapis_dziennika(info: str):
    log = f"({datetime.now()}) - {info}"
    logging.info(log)

ic(fn_test_ic(10))
ic.configureOutput(outputFunction=zapis_dziennika)
ic(fn_test_ic(20))
zapis_dziennika("test logowania")
logging.info("Test info")
logging.debug("test Debug") # uwaga! to nigdzie nie jest widoczne...
logging.error("A to Error!")
logging.critical("Krytyczny ERROR !!!!")

# więcej o logowaniu:  https://docs.python.org/3/howto/logging-cookbook.html