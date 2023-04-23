import socket
import sqlite3
import time
import os
import logging

class Server:
    # 定义服务器参数
    def __init__(self):
        ######################################################
        ##############  将下列IP与PORT改为自己的  ###############
        self.server_host = 'xxxxxxx'
        self.server_port = 1234
        ######################################################
        ######################################################
        # 间隔符
        self.SEPARATOR = '<SEPARATOR>'
        # 文件块的大小
        self.chunksize = 1024
        # 文件保存路径
        self.dir = '/tcpfiles'

    # 配置日志记录
    logging.basicConfig(filename='example.log', level=logging.INFO)

    # 连接数据库
    def connectconn(self):
        # 数据库
        self.conn = sqlite3.connect('file_info.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    # 创建文件存储表
    def creat_conn(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS files
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            code TEXT NOT NULL, 
                            filename TEXT NOT NULL,
                            save_time INT NOT NULL);''')
    def code_set_socket(self):
        self.scode = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.scode.bind((self.server_host,2234))
        # 监听数
        self.scode.listen(128)

    def code_listen(self):
        print("等待code接收：...")
        self.code_socket,self.ip= self.scode.accept()
        self.revcode = self.code_socket.recv(self.chunksize).decode()
        print(self.revcode)


    def findcode(self):
        self.cursor.execute(f"SELECT * FROM files WHERE code='{self.revcode}'")
        result = self.cursor.fetchone()
        self.filename = result[2]

    def code_return(self):
        self.code_socket.sendall(self.filename.encode())



    def setsocket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.server_host,self.server_port))
        # 监听数
        self.s.listen(128)
    # 服务器socket设置
    def listen(self):
        # 接受客户端连接
        print("等待连接中......")
        self.client_socket, self.client_ip = self.s.accept()
        print("来自",self.client_ip,"的连接")
        # 接受客户端信息
        self.received = self.client_socket.recv(self.chunksize).decode()
        self.code,self.filename,self.filesize = self.received.split(self.SEPARATOR)
        # 记录消息
        logging.info('文件添加:',self.code,'--',self.filename)
        print("提取码：",self.code)
        
    # 文件信息和提取码接收
    def recv(self):
        self.filename = os.path.basename(self.filename)
        self.filesize = int(self.filesize)

        # 存储文件和提取码到数据库
        save_time = int(time.time()) + 1*24*3600  # 设置保存时间为1天
        self.cursor.execute("INSERT INTO files (code, filename, save_time) VALUES (?, ?, ?)", (self.code, self.filename, save_time))
        self.conn.commit()
    

        # 写入文件
        with open(os.path.join(self.dir,self.filename),'wb')as f:
            while True:
                data = self.client_socket.recv(self.chunksize)
                if not data:
                    break
                f.write(data)

        self.remove_oldfiles()
        print("文件保存成功!")

    def remove_oldfiles(self):
        now = int(time.time())
        logging.info('清除文件......')
        # 遍历数据库
        circle = self.cursor.execute(f"SELECT id,code,filename,save_time FROM files")
        try:
            for filemsg in circle:
                filetime = filemsg[3]
                if filetime < now:
                    fileid = filemsg[0]
                    filename = filemsg[2]
                    filepath = os.path.join(self.dir,filename)
                    try:
                        os.remove(filepath)
                        self.cursor.execute(f"DELETE FROM files WHERE id='{fileid}'")
                        self.conn.commit()
                        logging.info('文件清除成功！')
                    except Exception as e:
                        logging.info('错误:'+str(e))
        except Exception as e:
            logging.info('错误:'+str(e))

    def close(self):
        self.s.close()
        # 关闭数据库连接
        self.conn.close()
