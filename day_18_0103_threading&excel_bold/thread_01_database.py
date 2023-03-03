import threading
import time
import sqlite3

# Global dictionary to store information from the first two threads
info_dict = {}


def check_database(db_file, info_dict):
    # conn = sqlite3.connect(db_file)
    # perform some checking
    time.sleep(3)  # simulate some checking time
    # write some information to the global dictionary
    info_dict[threading.current_thread().name] = f"Database {db_file} - checked"
    # conn.close()


# Create threads to run the database checking tasks
db_thread_1 = threading.Thread(target=check_database, args=("database1.db", info_dict), name="Thread 1")
db_thread_2 = threading.Thread(target=check_database, args=("database2.db", info_dict), name="Thread 2")
db_thread_3 = threading.Thread(target=check_database, args=("database.3db", info_dict), name="Thread 3")

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
