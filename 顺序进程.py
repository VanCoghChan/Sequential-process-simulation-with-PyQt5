import os, sys, time
import subprocess,threading
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPainter,QBrush,QPen
from PyQt5.QtCore import *
from PyQt5 import *
from Ui_untitled import *

button_style = ''' 
                     QPushButton
                     {text-align : center;
                     background-color : white;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 15px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 18px;}

                     QPushButton:pressed
                     {text-align : center;
                     background-color : light gray;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 18px;
                     padding: 16px;
                     height : 14px;
                     border-style: outset;
                     font : 14px;}

                     QPushButton:hover
                     {
                     background:#C0C0C0;}
                     '''

close_style = '''QPushButton{background:#F76677;border-radius:10px;}
                QPushButton:hover{background:red;} 
                '''

class mywindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton.setStyleSheet(button_style)
        self.pushButton_2.setStyleSheet(button_style)
        self.pushButton_3.setStyleSheet(button_style)
        self.pushButton_4.setStyleSheet(button_style)
        self.pushButton_close.setStyleSheet(close_style)
        self.pushButton_close.setIcon(QIcon("./关闭.png"))
        self.pushButton_close.clicked.connect(self.close)

        self.thread1 = threading.Thread(target=self.label_move)
        self.thread2 = threading.Thread(target=self.label2_move)
        self.thread3 = threading.Thread(target=self.label3_move)
        self.thread4 = threading.Thread(target=self.label4_move)
        self.pushButton.clicked.connect(self.start_threads)
        self.pushButton_2.clicked.connect(self.suspend_threads)
        self.pushButton_3.clicked.connect(self.resume_threads)
        self.pushButton_4.clicked.connect(self.restart)


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
             
    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        # pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(75, 65, 380, 65)
        qp.setPen(pen)
        qp.drawLine(75, 115, 380, 115)
        qp.setPen(pen)
        qp.drawLine(75, 65, 75, 115)

        qp.setPen(pen)
        qp.drawLine(75, 145, 380, 145)
        qp.setPen(pen)
        qp.drawLine(75, 195, 380, 195)
        qp.setPen(pen)
        qp.drawLine(75, 145, 75, 195)

        qp.setPen(pen)
        qp.drawLine(75, 225, 380, 225)
        qp.setPen(pen)
        qp.drawLine(75, 275, 380, 275)
        qp.setPen(pen)
        qp.drawLine(75, 225, 75, 275)

        qp.setPen(pen)
        qp.drawLine(75, 305, 380, 305)
        qp.setPen(pen)
        qp.drawLine(75, 355, 380, 355)
        qp.setPen(pen)
        qp.drawLine(75, 305, 75, 355)

        qp.setPen(pen)
        qp.drawLine(380, 185, 615, 185)
        qp.setPen(pen)
        qp.drawLine(380, 235, 615, 235)


    def start_threads(self):
        self.pushButton.hide()
        print("Threads num: {}".format(threading.activeCount()))
        if threading.activeCount() >= 2:
            pass
        else:
            self.thread1.suspended = threading.Event()
            self.thread1.suspended.set()
            self.thread2.suspended = threading.Event()
            self.thread2.suspended.set()
            self.thread3.suspended = threading.Event()
            self.thread3.suspended.set()
            self.thread4.suspended = threading.Event()
            self.thread4.suspended.set()
            self.thread1.start()
            self.thread2.start()
            self.thread3.start()
            self.thread4.start()

    def suspend_threads(self):
        for i in range(1,5):
            self.thread_suspend(eval("self.thread" + str(i)))

    def resume_threads(self):
        for i in range(1,5):
            self.thread_resume(eval("self.thread" + str(i)))

    def label_move(self): 
        for i in range(80,340,10):
            self.thread1.suspended.wait()
            self.label.move(i,70)
            time.sleep(0.18)
        self.thread_suspend(self.thread1)
        self.label.setGeometry(QtCore.QRect(513, 190, 41, 41))
    
    def label2_move(self):
        for i in range(80,340,10):
            self.thread2.suspended.wait()
            self.label_2.move(i,150)
            time.sleep(0.28)
        self.thread_suspend(self.thread2)
        self.label_2.setGeometry(QtCore.QRect(390, 190, 41, 41))
        self.InStack()
        
    def label3_move(self):
        for i in range(80,340,10):
            self.thread3.suspended.wait()
            self.label_3.move(i,230)
            time.sleep(0.25)
        self.thread_suspend(self.thread3)
        self.label_3.setGeometry(QtCore.QRect(431, 190, 41, 41))
    
    def label4_move(self):
        for i in range(80,340,10):
            self.thread4.suspended.wait()
            self.label_4.move(i,310)
            time.sleep(0.20)
        self.thread_suspend(self.thread4)
        self.label_4.setGeometry(QtCore.QRect(472, 190, 41, 41))

    def thread_suspend(self,thread):
        if not thread.suspended.is_set():
            return
        thread.suspended.clear()
    
    def thread_resume(self,thread):
        if thread.suspended.is_set():
            return
        thread.suspended.set()

    #1,4,3,2el
    def InStack(self):
        i1, i4, i3, i2 = 513, 472, 431, 390 
        while i2 <= 620 :
            if i1>620:
                self.label.setStyleSheet("QLabel{background:#F0F0F0;}")
            if i2>=620:
                self.label_2.setStyleSheet("QLabel{background:#F0F0F0;}")
            if i3>620:
                self.label_3.setStyleSheet("QLabel{background:#F0F0F0;}")
            if i4>620:
                self.label_4.setStyleSheet("QLabel{background:#F0F0F0;}")
            self.label.move(i1,190)
            self.label_2.move(i2,190)
            self.label_3.move(i3,190)
            self.label_4.move(i4,190)
            i1 += 10
            i2 += 10
            i3 += 10
            i4 += 10
            time.sleep(0.3)
    

    def restart(self):
        os.system("python 顺序进程.py")
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mywindow()
    w.show()
    sys.exit(app.exec_())
