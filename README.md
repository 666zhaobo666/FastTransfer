# FastTransfer
​	快速上传文件，使用提取码即可实现指定文件的快速下载。

## 开发环境

​	Python 3.10.6

​	PyQt 5.15.2

## 项目说明

​	整个项目分为客户端代码和服务端代码

### 	客户端：

- 采用TCP协议将文件传输至服务端，采用分块传输

- 通过paramiko模块实现远程服务器的连接与SFTP的连接，实现文件下载

### 	服务端：

- 使用SQLite存储文件的相关信息与提取码的配对
- 不定时删除过期文件，文件在服务端的保存时间为1天

## 使用说明：

### 	文件修改：

#### 		服务端：

```python
        ######################################################
        ##############  将下列IP与PORT改为自己的  ###############
        self.server_host = 'xxxxxxx'
        self.server_port = xxxx
        self.server_download_port = xxxx
        ######################################################
        ######################################################
```

​			将tcpserver.py中的上述代码改为自己服务器的本地ip与端口，记得开放端口权限！！

#### 		客户端：

```python
#####################################################################
        # 远程服务器用户名与密码
        self.user = 'root'
        self.passwd = 'xxxxxxx'
        self.port = xxxx
        self.download_port = xxxx
#####################################################################
```

​			将client.py中的上述代码改为自己服务器的用户名和密码

### 	界面使用：

![11](/11.png)

###     使用方法：
将server文件夹放在服务器，运行sermain.py;  将client文件夹放在本地，运行main.py
## 提示：

如果运行不了请查看相应的库是否安装完整！
文件保存在服务器的/tcpfiles/文件夹下，如果想自定义文件夹请自行更改。
