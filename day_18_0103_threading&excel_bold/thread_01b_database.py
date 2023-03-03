import threading
import time
import sqlite3

# Global dictionary to store information from the first two threads
info_dict = {}


def check_database1(db_file, info_dict):
    # conn = sqlite3.connect(db_file)
    # perform some checking
    time.sleep(20)  # simulate some checking time
    # write some information to the global dictionary
    info_dict["T1"] = f"Database {db_file} - checked - {time.time()}"
    # conn.close()


def check_database2(db_file, info_dict):
    # conn = sqlite3.connect(db_file)
    # perform some checking
    dane_out = [2, 3, 4]
    time.sleep(10)  # simulate some checking time

    # write some information to the global dictionary
    info_dict["T2"] = dane_out  # f"Database {db_file} - checked"
    info_dict["T2_t"] = f"{time.time()}"
    # conn.close()


def check_database3(db_file, info_dict):
    # conn = sqlite3.connect(db_file)
    # perform some checking
    suma = sum(info_dict["T2"])
    time.sleep(7)  # simulate some checking time
    # write some information to the global dictionary
    info_dict["T3"] = f"Database {db_file} - checked: {suma=} - {time.time()}"
    # conn.close()


# Create threads to run the database checking tasks
db_thread_1 = threading.Thread(target=check_database1, args=("database1.db", info_dict), name="Thread 1")
db_thread_2 = threading.Thread(target=check_database2, args=("database2.db", info_dict), name="Thread 2")
db_thread_3 = threading.Thread(target=check_database3, args=("database.3db", info_dict), name="Thread 3")

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
db_thread_2.join()
print("joined 2")
print(info_dict)

print("3 start...")
db_thread_3.start()
db_thread_3.join()
print("finnish")
print(info_dict)

# All three threads have finished their tasks
print("All threads finished!")
