# Threads is a sepratre flow of execution


import logging
import threading 
import time



def thread_function(name):
    logging.info(f"Thead {name}: Strating")
    time.sleep(5)
    logging.info(f"Thread {name} finishing")



if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"

    logging.basicConfig(format=format , level = logging.INFO , datefmt  = "%H:%M:%S")

    logging.info("Main   : before creatiung thread")

    x = threading.Thread(target= thread_function , args=(1,), daemon = True)

    logging.info("Main  : before runnig thread")
    x.start()
    logging.info("Main  : wait for the thread to finish")
    x.join()
    logging.info("Main  : all done")


