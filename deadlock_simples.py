import threading
import time

recurso_A = threading.Lock()
recurso_B = threading.Lock()

def thread_1():
    with recurso_A:
        print("Thread 1 tem o recurso A")
        time.sleep(1) # Simula trabalho
        with recurso_B:
            print("Thread 1 tem os recursos A e B")

#função sem deadlock

def thread_2():
    with recurso_A: # Mudança aqui: ambas as threads adquirem A primeiro
        print("Thread 2 tem o recurso A")
        time.sleep(1) # Simula trabalho
        with recurso_B:
            print("Thread 2 tem os recursos A e B")


#função com deadLock (primeiro pega a A e depois B, impedindo que a thread 1 pegue o A)

"""def thread_2():
    with recurso_A: # Mudança aqui: ambas as threads adquirem A primeiro
        print("Thread 2 tem o recurso A")
        time.sleep(1) # Simula trabalho
        with recurso_B:
            print("Thread 2 tem os recursos A e B")"""


t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Fim do programa")