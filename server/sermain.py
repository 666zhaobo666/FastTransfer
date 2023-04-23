from tcpserver import Server
import threading
import time

if __name__ == '__main__':
    server = Server()
    server.code_set_socket()
    server.setsocket()
    server.connectconn()
    server.creat_conn()
    def revfile():
        while True:
            server.listen()
            server.recv()
    def codeserver():
        while True:
            server.code_listen()
            server.findcode()
            server.code_return()

    def remove_file():
            server.remove_oldfiles()

    t1 = threading.Thread(target=revfile)
    t2 = threading.Thread(target=codeserver)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

