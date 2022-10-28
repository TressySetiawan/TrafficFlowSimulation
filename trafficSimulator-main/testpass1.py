from multiprocessing import Process,Pipe

present = 0

def f(child_conn):
    child_conn.send(present)
    child_conn.close()

while True :
    present += 1