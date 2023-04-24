import socket
import os
import random
import paramiko

class Tcpclient:

    # 定义参数
    def __init__(self):
        self.SEPARATOR = '<SEPARATOR>'
        # 文件块的大小
        self.chunksize = 1024

    # 生成随机提取码
    def setcode(self):
        self.code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

    # 服务器连接
    def connect(self,host,port):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((host,port))

    # socket数据发送
    def send(self,filename):
        # 获取文件大小
        file_size = os.path.getsize(filename)
        # 发送提取码和文件名
        self.s.sendall(f'{self.code}{self.SEPARATOR}{filename}{self.SEPARATOR}{file_size}'.encode())
        # 发送文件数据
        with open(filename,'rb') as f:
            while True:
                data = f.read(self.chunksize)
                if not data:
                    break
                self.s.sendall(data)

    # 关闭socket
    def close(self):
        self.s.close()

    # 文件下载
    def download(self,code,host,dport,user,passwd,remote_file,local_file):
        # 从远程服务器获取文件名
        self.connect(host,dport)
        self.s.sendall(f'{code}'.encode())
        response = self.s.recv(1024)
        response = response.decode()
        self.s.close()
        # 创建SSH客户端对象
        ssh = paramiko.SSHClient()
        # 自动添加远程主机名和密钥到本地“known_hosts”文件
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接远程Linux服务器
        ssh.connect(hostname=host,port=22,username=user, password=passwd)
        # 创建SFTP客户端对象
        sftp = ssh.open_sftp()
        # 合并路径
        remote_file = os.path.join(remote_file, response)
        local_file = os.path.join(local_file, response)
        remote_file = os.path.normpath(remote_file)
        local_file = os.path.normpath(local_file)
        remote_file = remote_file.replace("\\","/")
        # 从远程服务器下载文件
        sftp.get(remote_file, local_file)
        # 关闭SFTP客户端
        sftp.close()
        # 关闭SSH客户端
        ssh.close()


        
                
            


