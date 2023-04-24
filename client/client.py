from PyQt5 import QtCore,QtWidgets
from tcpclient import Tcpclient
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #####################################################################
        # 远程服务器用户名与密码
        self.user = 'root'
        self.passwd = 'xxxxxxx'
        self.port = xxxx
        self.download_port = xxxx
        #####################################################################
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 397)
        MainWindow.setMinimumSize(QtCore.QSize(985, 397))
        MainWindow.setMaximumSize(QtCore.QSize(985, 397))
        MainWindow.setWindowIcon(QIcon("./01.ico"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(401, 31, 84, 16))
        self.label.setObjectName("label")
        self.lineEdit_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ip.setGeometry(QtCore.QRect(490, 30, 451, 24))
        self.lineEdit_ip.setMinimumSize(QtCore.QSize(451, 24))
        self.lineEdit_ip.setMaximumSize(QtCore.QSize(451, 24))
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 80, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit_file = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_file.setGeometry(QtCore.QRect(490, 80, 451, 21))
        self.lineEdit_file.setMinimumSize(QtCore.QSize(451, 21))
        self.lineEdit_file.setMaximumSize(QtCore.QSize(451, 21))
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.toolButton_file = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file.setGeometry(QtCore.QRect(940, 80, 31, 21))
        self.toolButton_file.setMinimumSize(QtCore.QSize(31, 21))
        self.toolButton_file.setMaximumSize(QtCore.QSize(31, 21))
        self.toolButton_file.setObjectName("toolButton_file")
        self.button_send = QtWidgets.QPushButton(self.centralwidget)
        self.button_send.setGeometry(QtCore.QRect(400, 310, 121, 41))
        self.button_send.setMinimumSize(QtCore.QSize(121, 41))
        self.button_send.setMaximumSize(QtCore.QSize(121, 41))
        self.button_send.setObjectName("button_send")
        self.button_download = QtWidgets.QPushButton(self.centralwidget)
        self.button_download.setGeometry(QtCore.QRect(810, 310, 121, 41))
        self.button_download.setMinimumSize(QtCore.QSize(121, 41))
        self.button_download.setMaximumSize(QtCore.QSize(121, 41))
        self.button_download.setObjectName("button_download")
        self.text = QtWidgets.QTextBrowser(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(20, 20, 351, 331))
        self.text.setObjectName("text")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 130, 72, 15))
        self.label_3.setObjectName("label_3")
        self.lineEdit_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_path.setGeometry(QtCore.QRect(490, 130, 451, 21))
        self.lineEdit_path.setMinimumSize(QtCore.QSize(451, 21))
        self.lineEdit_path.setMaximumSize(QtCore.QSize(451, 21))
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.toolButton_path = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_path.setGeometry(QtCore.QRect(940, 130, 31, 21))
        self.toolButton_path.setMinimumSize(QtCore.QSize(31, 21))
        self.toolButton_path.setMaximumSize(QtCore.QSize(31, 21))
        self.toolButton_path.setObjectName("toolButton_path")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 190, 72, 15))
        self.label_4.setObjectName("label_4")
        self.lineEdit_code = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_code.setGeometry(QtCore.QRect(490, 190, 211, 21))
        self.lineEdit_code.setMinimumSize(QtCore.QSize(211, 21))
        self.lineEdit_code.setMaximumSize(QtCore.QSize(211, 21))
        self.lineEdit_code.setObjectName("lineEdit_code")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(370, 20, 20, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(380, 220, 601, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(610, 320, 131, 20))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # tcp类的传入
        self.tcpclient = Tcpclient()

        # 按钮绑定
        self.button_send.clicked.connect(self.send)
        self.button_download.clicked.connect(self.download)
        self.toolButton_file.clicked.connect(self.choosefile)
        self.toolButton_path.clicked.connect(self.choosepath)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BOGE文件互传"))
        self.label.setText(_translate("MainWindow", "远程主机IP:"))
        self.label_2.setText(_translate("MainWindow", "选择文件:"))
        self.toolButton_file.setText(_translate("MainWindow", "..."))
        self.button_send.setText(_translate("MainWindow", "发送"))
        self.button_download.setText(_translate("MainWindow", "下载"))
        self.label_3.setText(_translate("MainWindow", "保存路径:"))
        self.toolButton_path.setText(_translate("MainWindow", "..."))
        self.label_4.setText(_translate("MainWindow", "提取码:"))
        self.label_5.setText(_translate("MainWindow", "Designed by 赵博"))

    # 发送文件
    def send(self):
        host = self.lineEdit_ip.text()
        filename = self.lineEdit_file.text()
        if len(host) == 0 or len(filename) == 0:
            self.text.append('警告：主机IP地址、选择发送的文件路径无效，请检查！！！')
        else:
            self.tcpclient.setcode()
            self.lineEdit_code.setText(self.tcpclient.code)
            self.text.append('该文件提取码为:'+self.tcpclient.code+'，'+'请妥善保存！')
            self.tcpclient.connect(host,self.port)
            self.tcpclient.send(filename)
            self.text.append('文件上传成功！')
            self.tcpclient.close()
    # 选择文件
    def choosefile(self):
        file = QFileDialog.getOpenFileName()
        filepath = file[0]
        self.lineEdit_file.setText(filepath)
        self.text.append('文件选择成功！')

    # 选择下载路径
    def choosepath(self):
        filepath = QFileDialog.getExistingDirectory()
        self.lineEdit_path.setText(filepath)
        self.text.append('文件下载路径选择成功！')

    # 下载文件
    def download(self):
        code = self.lineEdit_code.text()
        host = self.lineEdit_ip.text()
        local_file = self.lineEdit_path.text()
        remote_file = '/tcpfiles'
        if host and local_file and code:
            self.text.append('请耐心等待，文件正在下载中...')
            self.tcpclient.download(code,host,self.download_port,self.user,self.passwd,remote_file,local_file)
            self.text.append('文件下载完成√√')
        else:
            self.text.append('警告：主机IP地址、提取码、保存路径无效，请检查！！！')



