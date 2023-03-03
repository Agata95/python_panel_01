import threading
import time
import psutil

class MyThread(threading.Thread):
    def run(self):
        # perform some CPU-intensive work
        for i in range(10000000):
            pass

def wait_for_thread_with_less_cpu_utilization(threads):
    while True:
        # get CPU utilization of each thread
        cpu_utilizations = [psutil.Process(t.ident).cpu_percent() for t in threads]
        # find the thread with the least CPU utilization
        min_cpu_utilization = min(cpu_utilizations)
        min_cpu_thread = threads[cpu_utilizations.index(min_cpu_utilization)]
        # check if the least CPU-utilized thread has finished
        if not min_cpu_thread.is_alive():
            break
        # wait a bit and check again
        time.sleep(0.1)
    print(f"The thread with ID {min_cpu_thread.ident} has the least CPU utilization and has finished.")

# create some threads
threads = []
for i in range(5):
    t = MyThread()
    threads.append(t)

# start the threads
for t in threads:
    t.start()

# wait for the thread with the least CPU utilization
wait_for_thread_with_less_cpu_utilization(threads)
