import threading
import time
import sqlite3
from sys import exit

# Global dictionary to store information from the first two threads
info_dict = {
    "DANE": {},
    "CZAS_WYK": {},
             }

def check_database1(db_file):
    start_time = time.time()
    # conn = sqlite3.connect(db_file)
    # perform some checking
    time.sleep(10) # simulate some checking time
    # write some information to the global dictionary
    info_dict["T1"] = f"Database {db_file} - checked - {time.time()}"
    # info_dict["DANE"]["T1"] = 934
    info_dict["CZAS_WYK"]["T1"] = time.time() - start_time
    # conn.close()

def check_database2(db_file):
    start_time = time.time()
    # conn = sqlite3.connect(db_file)
    # perform some checking
    dane_out = [2, 3, 4]
    while not "T1" in info_dict["DANE"].keys():
        pass
        # print("Oczekuję na T1")
    print(f'Mamy {info_dict["DANE"]["T1"]=}')
    dane_out.append(info_dict["DANE"]["T1"])

    # write some information to the global dictionary
    info_dict["T2"] = dane_out  # f"Database {db_file} - checked"
    info_dict["CZAS_WYK"]["T2"] = time.time() - start_time
    # conn.close()

def check_database3(db_file):
    start_time = time.time()
    # conn = sqlite3.connect(db_file)
    # perform some checking
    try:
        suma = sum(info_dict["T2"])
    except:
        suma = 0

    time.sleep(3) # simulate some checking time
    # write some information to the global dictionary
    info_dict["T3"] = f"Database {db_file} - checked: {suma=} - {time.time()}"
    info_dict["CZAS_WYK"]["T3"] = time.time() - start_time
    # conn.close()


# Create threads to run the database checking tasks
db_thread_1 = threading.Thread(target=check_database1, args=("database1.db",), name="Thread 1")
db_thread_2 = threading.Thread(target=check_database2, args=("database2.db",), name="Thread 2")
db_thread_3 = threading.Thread(target=check_database3, args=("database.3db",), name="Thread 3")

# Start all three threads to run the database checking tasks
db_thread_1.start()
db_thread_2.start()
print("started 1..2")

print(info_dict)
# Wait for all three threads to finish their database checking tasks
print("will join 1")
db_thread_1.join()
print("joined 1")
print(info_dict)

print("will join 2")
# Aby zabezpieczyć się na czas wykonania......
db_thread_2.join(timeout=4)
print("joined 2")
print(info_dict)

print("3 start...")
db_thread_3.start()
db_thread_3.join()
print("finnish")
print(info_dict)

# All three threads have finished their tasks
print("All threads finished!")

