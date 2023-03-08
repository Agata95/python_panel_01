import threading
import dumper
import time
from random import randint
from sys import exit

# blokada na wyłączność
# przykład: w czasie pracy na dany plik nakłądana jest blokada, by żadna inna app nie mogła nic w nim zmienić
lock = threading.Lock()
dumper.dump(lock)

# Global dictionary to store information from the first two threads
# MAX - maksymalna ilość wątków, która może się łączyć z daną bazą
# CURRENT - ile aktualnie wątków działa
info_dict = {
    "MAX": 3,
    "CURRENT": 0,
    "DANE": {},
    "CZAS_WYK": {},
    "DONE": {},
}


def check_database(db_file):
    thread_name = threading.current_thread().name
    while info_dict["CURRENT"] == info_dict["MAX"]:
        print(f"Proces {thread_name} is waiting for free slot...")

    # założenie blokady - aby dwa procesy naraz coś zapisywały
    lock.acquire()
    if info_dict["CURRENT"] < info_dict["MAX"]:
        print(f"{thread_name} aquaried")
        info_dict["CURRENT"] += 1
        lock.release()
        # poniżej operacje na bazie
        print(f"{thread_name} released")
        start_time = time.time()
        time.sleep(randint(1, 16))  # simulate some checking time
        info_dict["DANE"][thread_name] = f"Database {db_file} - checked - {time.time()}"
        info_dict["CZAS_WYK"][thread_name] = time.time() - start_time
        info_dict["DONE"][thread_name] = f"Database {db_file} - checked and release"
        lock.acquire()
        info_dict["CURRENT"] -= 1

    lock.release()
    print(f"{thread_name} released, {info_dict}")
    # conn.close()


# Create threads to run the database checking tasks
db_thread_1 = threading.Thread(target=check_database, args=("database1.db",), name="Thread 1")
db_thread_2 = threading.Thread(target=check_database, args=("database2.db",), name="Thread 2")
db_thread_3 = threading.Thread(target=check_database, args=("database3.db",), name="Thread 3")
db_thread_4 = threading.Thread(target=check_database, args=("database4.db",), name="Thread 4")
db_thread_5 = threading.Thread(target=check_database, args=("database5.db",), name="Thread 5")
db_thread_6 = threading.Thread(target=check_database, args=("database6.db",), name="Thread 6")

# Start all three threads to run the database checking tasks
db_thread_1.start()
db_thread_2.start()
db_thread_3.start()
db_thread_4.start()
db_thread_5.start()
db_thread_6.start()
print("all started")

print(info_dict)

db_thread_1.join()
db_thread_2.join()
db_thread_3.join()
db_thread_4.join()
db_thread_5.join()
db_thread_6.join()
print("------------------------------------")
dumper.dump(info_dict)
print("------------------------------------")
print(info_dict)
