from multiprocessing import Process,Queue,Pipe
from testpass1 import f

if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())