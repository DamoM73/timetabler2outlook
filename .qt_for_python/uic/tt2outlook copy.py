# Form implementation generated from reading ui file 'h:\GIT\timetabler2outlook\tt2outlook copy.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(899, 816)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.period_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.period_lb.setFont(font)
        self.period_lb.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 255);")
        self.period_lb.setObjectName("period_lb")
        self.horizontalLayout.addWidget(self.period_lb)
        self.mon_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.mon_lb.setFont(font)
        self.mon_lb.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 255);")
        self.mon_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mon_lb.setObjectName("mon_lb")
        self.horizontalLayout.addWidget(self.mon_lb)
        self.tues_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tues_lb.setFont(font)
        self.tues_lb.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 255);")
        self.tues_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.tues_lb.setObjectName("tues_lb")
        self.horizontalLayout.addWidget(self.tues_lb)
        self.wed_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.wed_lb.setFont(font)
        self.wed_lb.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 255);")
        self.wed_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wed_lb.setObjectName("wed_lb")
        self.horizontalLayout.addWidget(self.wed_lb)
        self.thurs_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.thurs_lb.setFont(font)
        self.thurs_lb.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 255);")
        self.thurs_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.thurs_lb.setObjectName("thurs_lb")
        self.horizontalLayout.addWidget(self.thurs_lb)
        self.fri_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.fri_lb.setFont(font)
        self.fri_lb.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 170, 255);")
        self.fri_lb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fri_lb.setObjectName("fri_lb")
        self.horizontalLayout.addWidget(self.fri_lb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bs_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bs_lb.setFont(font)
        self.bs_lb.setObjectName("bs_lb")
        self.horizontalLayout_5.addWidget(self.bs_lb)
        self.mon_bs_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_bs_btn.setFont(font)
        self.mon_bs_btn.setText("")
        self.mon_bs_btn.setFlat(False)
        self.mon_bs_btn.setObjectName("mon_bs_btn")
        self.horizontalLayout_5.addWidget(self.mon_bs_btn)
        self.tues_bs_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_bs_btn.setFont(font)
        self.tues_bs_btn.setText("")
        self.tues_bs_btn.setFlat(False)
        self.tues_bs_btn.setObjectName("tues_bs_btn")
        self.horizontalLayout_5.addWidget(self.tues_bs_btn)
        self.wed_bs_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_bs_btn.setFont(font)
        self.wed_bs_btn.setText("")
        self.wed_bs_btn.setFlat(False)
        self.wed_bs_btn.setObjectName("wed_bs_btn")
        self.horizontalLayout_5.addWidget(self.wed_bs_btn)
        self.thurs_bs_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_bs_btn.setFont(font)
        self.thurs_bs_btn.setText("")
        self.thurs_bs_btn.setFlat(False)
        self.thurs_bs_btn.setObjectName("thurs_bs_btn")
        self.horizontalLayout_5.addWidget(self.thurs_bs_btn)
        self.fri_bs_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_bs_btn.setFont(font)
        self.fri_bs_btn.setText("")
        self.fri_bs_btn.setFlat(False)
        self.fri_bs_btn.setObjectName("fri_bs_btn")
        self.horizontalLayout_5.addWidget(self.fri_bs_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bf_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bf_lb.setFont(font)
        self.bf_lb.setObjectName("bf_lb")
        self.horizontalLayout_6.addWidget(self.bf_lb)
        self.mon_bf_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_bf_btn.setFont(font)
        self.mon_bf_btn.setText("")
        self.mon_bf_btn.setFlat(False)
        self.mon_bf_btn.setObjectName("mon_bf_btn")
        self.horizontalLayout_6.addWidget(self.mon_bf_btn)
        self.tues_bf_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_bf_btn.setFont(font)
        self.tues_bf_btn.setText("")
        self.tues_bf_btn.setFlat(False)
        self.tues_bf_btn.setObjectName("tues_bf_btn")
        self.horizontalLayout_6.addWidget(self.tues_bf_btn)
        self.wed_bf_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_bf_btn.setFont(font)
        self.wed_bf_btn.setText("")
        self.wed_bf_btn.setFlat(False)
        self.wed_bf_btn.setObjectName("wed_bf_btn")
        self.horizontalLayout_6.addWidget(self.wed_bf_btn)
        self.thurs_bf_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_bf_btn.setFont(font)
        self.thurs_bf_btn.setText("")
        self.thurs_bf_btn.setFlat(False)
        self.thurs_bf_btn.setObjectName("thurs_bf_btn")
        self.horizontalLayout_6.addWidget(self.thurs_bf_btn)
        self.fri_bf_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_bf_btn.setFont(font)
        self.fri_bf_btn.setText("")
        self.fri_bf_btn.setFlat(False)
        self.fri_bf_btn.setObjectName("fri_bf_btn")
        self.horizontalLayout_6.addWidget(self.fri_bf_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.f_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.f_lb.setFont(font)
        self.f_lb.setObjectName("f_lb")
        self.horizontalLayout_19.addWidget(self.f_lb)
        self.mon_f_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_f_btn.setFont(font)
        self.mon_f_btn.setText("")
        self.mon_f_btn.setFlat(False)
        self.mon_f_btn.setObjectName("mon_f_btn")
        self.horizontalLayout_19.addWidget(self.mon_f_btn)
        self.tues_f_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_f_btn.setFont(font)
        self.tues_f_btn.setText("")
        self.tues_f_btn.setFlat(False)
        self.tues_f_btn.setObjectName("tues_f_btn")
        self.horizontalLayout_19.addWidget(self.tues_f_btn)
        self.wed_f_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_f_btn.setFont(font)
        self.wed_f_btn.setText("")
        self.wed_f_btn.setFlat(False)
        self.wed_f_btn.setObjectName("wed_f_btn")
        self.horizontalLayout_19.addWidget(self.wed_f_btn)
        self.thurs_f_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_f_btn.setFont(font)
        self.thurs_f_btn.setText("")
        self.thurs_f_btn.setFlat(False)
        self.thurs_f_btn.setObjectName("thurs_f_btn")
        self.horizontalLayout_19.addWidget(self.thurs_f_btn)
        self.fri_f_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_f_btn.setFont(font)
        self.fri_f_btn.setText("")
        self.fri_f_btn.setFlat(False)
        self.fri_f_btn.setObjectName("fri_f_btn")
        self.horizontalLayout_19.addWidget(self.fri_f_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.p1_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p1_lb.setFont(font)
        self.p1_lb.setObjectName("p1_lb")
        self.horizontalLayout_7.addWidget(self.p1_lb)
        self.mon_p1_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_p1_btn.setFont(font)
        self.mon_p1_btn.setText("")
        self.mon_p1_btn.setFlat(False)
        self.mon_p1_btn.setObjectName("mon_p1_btn")
        self.horizontalLayout_7.addWidget(self.mon_p1_btn)
        self.tues_p1_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_p1_btn.setFont(font)
        self.tues_p1_btn.setText("")
        self.tues_p1_btn.setFlat(False)
        self.tues_p1_btn.setObjectName("tues_p1_btn")
        self.horizontalLayout_7.addWidget(self.tues_p1_btn)
        self.wed_p1_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_p1_btn.setFont(font)
        self.wed_p1_btn.setText("")
        self.wed_p1_btn.setFlat(False)
        self.wed_p1_btn.setObjectName("wed_p1_btn")
        self.horizontalLayout_7.addWidget(self.wed_p1_btn)
        self.thurs_p1_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_p1_btn.setFont(font)
        self.thurs_p1_btn.setText("")
        self.thurs_p1_btn.setFlat(False)
        self.thurs_p1_btn.setObjectName("thurs_p1_btn")
        self.horizontalLayout_7.addWidget(self.thurs_p1_btn)
        self.fri_p1_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_p1_btn.setFont(font)
        self.fri_p1_btn.setText("")
        self.fri_p1_btn.setFlat(False)
        self.fri_p1_btn.setObjectName("fri_p1_btn")
        self.horizontalLayout_7.addWidget(self.fri_p1_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.p2_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p2_lb.setFont(font)
        self.p2_lb.setObjectName("p2_lb")
        self.horizontalLayout_8.addWidget(self.p2_lb)
        self.mon_p2_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_p2_btn.setFont(font)
        self.mon_p2_btn.setText("")
        self.mon_p2_btn.setFlat(False)
        self.mon_p2_btn.setObjectName("mon_p2_btn")
        self.horizontalLayout_8.addWidget(self.mon_p2_btn)
        self.tues_p2_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_p2_btn.setFont(font)
        self.tues_p2_btn.setText("")
        self.tues_p2_btn.setFlat(False)
        self.tues_p2_btn.setObjectName("tues_p2_btn")
        self.horizontalLayout_8.addWidget(self.tues_p2_btn)
        self.wed_p2_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_p2_btn.setFont(font)
        self.wed_p2_btn.setText("")
        self.wed_p2_btn.setFlat(False)
        self.wed_p2_btn.setObjectName("wed_p2_btn")
        self.horizontalLayout_8.addWidget(self.wed_p2_btn)
        self.thurs_p2_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_p2_btn.setFont(font)
        self.thurs_p2_btn.setText("")
        self.thurs_p2_btn.setFlat(False)
        self.thurs_p2_btn.setObjectName("thurs_p2_btn")
        self.horizontalLayout_8.addWidget(self.thurs_p2_btn)
        self.fri_p2_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_p2_btn.setFont(font)
        self.fri_p2_btn.setText("")
        self.fri_p2_btn.setFlat(False)
        self.fri_p2_btn.setObjectName("fri_p2_btn")
        self.horizontalLayout_8.addWidget(self.fri_p2_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.fbfh_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fbfh_lb.setFont(font)
        self.fbfh_lb.setObjectName("fbfh_lb")
        self.horizontalLayout_9.addWidget(self.fbfh_lb)
        self.mon_fbfh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_fbfh_btn.setFont(font)
        self.mon_fbfh_btn.setText("")
        self.mon_fbfh_btn.setFlat(False)
        self.mon_fbfh_btn.setObjectName("mon_fbfh_btn")
        self.horizontalLayout_9.addWidget(self.mon_fbfh_btn)
        self.tues_fbfh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_fbfh_btn.setFont(font)
        self.tues_fbfh_btn.setText("")
        self.tues_fbfh_btn.setFlat(False)
        self.tues_fbfh_btn.setObjectName("tues_fbfh_btn")
        self.horizontalLayout_9.addWidget(self.tues_fbfh_btn)
        self.wed_fbfh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_fbfh_btn.setFont(font)
        self.wed_fbfh_btn.setText("")
        self.wed_fbfh_btn.setFlat(False)
        self.wed_fbfh_btn.setObjectName("wed_fbfh_btn")
        self.horizontalLayout_9.addWidget(self.wed_fbfh_btn)
        self.thurs_fbfh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_fbfh_btn.setFont(font)
        self.thurs_fbfh_btn.setText("")
        self.thurs_fbfh_btn.setFlat(False)
        self.thurs_fbfh_btn.setObjectName("thurs_fbfh_btn")
        self.horizontalLayout_9.addWidget(self.thurs_fbfh_btn)
        self.fri_fbfh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_fbfh_btn.setFont(font)
        self.fri_fbfh_btn.setText("")
        self.fri_fbfh_btn.setFlat(False)
        self.fri_fbfh_btn.setObjectName("fri_fbfh_btn")
        self.horizontalLayout_9.addWidget(self.fri_fbfh_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.fbsh_lb_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fbsh_lb_2.setFont(font)
        self.fbsh_lb_2.setObjectName("fbsh_lb_2")
        self.horizontalLayout_10.addWidget(self.fbsh_lb_2)
        self.mon_fbsh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_fbsh_btn.setFont(font)
        self.mon_fbsh_btn.setText("")
        self.mon_fbsh_btn.setFlat(False)
        self.mon_fbsh_btn.setObjectName("mon_fbsh_btn")
        self.horizontalLayout_10.addWidget(self.mon_fbsh_btn)
        self.tues_fbsh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_fbsh_btn.setFont(font)
        self.tues_fbsh_btn.setText("")
        self.tues_fbsh_btn.setFlat(False)
        self.tues_fbsh_btn.setObjectName("tues_fbsh_btn")
        self.horizontalLayout_10.addWidget(self.tues_fbsh_btn)
        self.wed_fbsh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_fbsh_btn.setFont(font)
        self.wed_fbsh_btn.setText("")
        self.wed_fbsh_btn.setFlat(False)
        self.wed_fbsh_btn.setObjectName("wed_fbsh_btn")
        self.horizontalLayout_10.addWidget(self.wed_fbsh_btn)
        self.thurs_fbsh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_fbsh_btn.setFont(font)
        self.thurs_fbsh_btn.setText("")
        self.thurs_fbsh_btn.setFlat(False)
        self.thurs_fbsh_btn.setObjectName("thurs_fbsh_btn")
        self.horizontalLayout_10.addWidget(self.thurs_fbsh_btn)
        self.fri_fbsh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_fbsh_btn.setFont(font)
        self.fri_fbsh_btn.setText("")
        self.fri_fbsh_btn.setFlat(False)
        self.fri_fbsh_btn.setObjectName("fri_fbsh_btn")
        self.horizontalLayout_10.addWidget(self.fri_fbsh_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.p3_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p3_lb.setFont(font)
        self.p3_lb.setObjectName("p3_lb")
        self.horizontalLayout_11.addWidget(self.p3_lb)
        self.mon_p3_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_p3_btn.setFont(font)
        self.mon_p3_btn.setText("")
        self.mon_p3_btn.setFlat(False)
        self.mon_p3_btn.setObjectName("mon_p3_btn")
        self.horizontalLayout_11.addWidget(self.mon_p3_btn)
        self.tues_p3_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_p3_btn.setFont(font)
        self.tues_p3_btn.setText("")
        self.tues_p3_btn.setFlat(False)
        self.tues_p3_btn.setObjectName("tues_p3_btn")
        self.horizontalLayout_11.addWidget(self.tues_p3_btn)
        self.wed_p3_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_p3_btn.setFont(font)
        self.wed_p3_btn.setText("")
        self.wed_p3_btn.setFlat(False)
        self.wed_p3_btn.setObjectName("wed_p3_btn")
        self.horizontalLayout_11.addWidget(self.wed_p3_btn)
        self.thurs_p3_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_p3_btn.setFont(font)
        self.thurs_p3_btn.setText("")
        self.thurs_p3_btn.setFlat(False)
        self.thurs_p3_btn.setObjectName("thurs_p3_btn")
        self.horizontalLayout_11.addWidget(self.thurs_p3_btn)
        self.fri_p3_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_p3_btn.setFont(font)
        self.fri_p3_btn.setText("")
        self.fri_p3_btn.setFlat(False)
        self.fri_p3_btn.setObjectName("fri_p3_btn")
        self.horizontalLayout_11.addWidget(self.fri_p3_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.p4_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p4_lb.setFont(font)
        self.p4_lb.setObjectName("p4_lb")
        self.horizontalLayout_12.addWidget(self.p4_lb)
        self.mon_p4_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_p4_btn.setFont(font)
        self.mon_p4_btn.setText("")
        self.mon_p4_btn.setFlat(False)
        self.mon_p4_btn.setObjectName("mon_p4_btn")
        self.horizontalLayout_12.addWidget(self.mon_p4_btn)
        self.tues_p4_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_p4_btn.setFont(font)
        self.tues_p4_btn.setText("")
        self.tues_p4_btn.setFlat(False)
        self.tues_p4_btn.setObjectName("tues_p4_btn")
        self.horizontalLayout_12.addWidget(self.tues_p4_btn)
        self.wed_p4_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_p4_btn.setFont(font)
        self.wed_p4_btn.setText("")
        self.wed_p4_btn.setFlat(False)
        self.wed_p4_btn.setObjectName("wed_p4_btn")
        self.horizontalLayout_12.addWidget(self.wed_p4_btn)
        self.thurs_p4_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_p4_btn.setFont(font)
        self.thurs_p4_btn.setText("")
        self.thurs_p4_btn.setFlat(False)
        self.thurs_p4_btn.setObjectName("thurs_p4_btn")
        self.horizontalLayout_12.addWidget(self.thurs_p4_btn)
        self.fri_p4_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_p4_btn.setFont(font)
        self.fri_p4_btn.setText("")
        self.fri_p4_btn.setFlat(False)
        self.fri_p4_btn.setObjectName("fri_p4_btn")
        self.horizontalLayout_12.addWidget(self.fri_p4_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.sbfh_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sbfh_lb.setFont(font)
        self.sbfh_lb.setObjectName("sbfh_lb")
        self.horizontalLayout_13.addWidget(self.sbfh_lb)
        self.mon_sbfh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_sbfh_btn.setFont(font)
        self.mon_sbfh_btn.setText("")
        self.mon_sbfh_btn.setFlat(False)
        self.mon_sbfh_btn.setObjectName("mon_sbfh_btn")
        self.horizontalLayout_13.addWidget(self.mon_sbfh_btn)
        self.tues_sbfh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_sbfh_btn.setFont(font)
        self.tues_sbfh_btn.setText("")
        self.tues_sbfh_btn.setFlat(False)
        self.tues_sbfh_btn.setObjectName("tues_sbfh_btn")
        self.horizontalLayout_13.addWidget(self.tues_sbfh_btn)
        self.wed_sbfh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_sbfh_btn.setFont(font)
        self.wed_sbfh_btn.setText("")
        self.wed_sbfh_btn.setFlat(False)
        self.wed_sbfh_btn.setObjectName("wed_sbfh_btn")
        self.horizontalLayout_13.addWidget(self.wed_sbfh_btn)
        self.thurs_sbfh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_sbfh_btn.setFont(font)
        self.thurs_sbfh_btn.setText("")
        self.thurs_sbfh_btn.setFlat(False)
        self.thurs_sbfh_btn.setObjectName("thurs_sbfh_btn")
        self.horizontalLayout_13.addWidget(self.thurs_sbfh_btn)
        self.fri_sbfh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_sbfh_btn.setFont(font)
        self.fri_sbfh_btn.setText("")
        self.fri_sbfh_btn.setFlat(False)
        self.fri_sbfh_btn.setObjectName("fri_sbfh_btn")
        self.horizontalLayout_13.addWidget(self.fri_sbfh_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.sbsh_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sbsh_lb.setFont(font)
        self.sbsh_lb.setObjectName("sbsh_lb")
        self.horizontalLayout_14.addWidget(self.sbsh_lb)
        self.mon_sbsh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_sbsh_btn.setFont(font)
        self.mon_sbsh_btn.setText("")
        self.mon_sbsh_btn.setFlat(False)
        self.mon_sbsh_btn.setObjectName("mon_sbsh_btn")
        self.horizontalLayout_14.addWidget(self.mon_sbsh_btn)
        self.tues_sbsh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_sbsh_btn.setFont(font)
        self.tues_sbsh_btn.setText("")
        self.tues_sbsh_btn.setFlat(False)
        self.tues_sbsh_btn.setObjectName("tues_sbsh_btn")
        self.horizontalLayout_14.addWidget(self.tues_sbsh_btn)
        self.wed_sbsh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_sbsh_btn.setFont(font)
        self.wed_sbsh_btn.setText("")
        self.wed_sbsh_btn.setFlat(False)
        self.wed_sbsh_btn.setObjectName("wed_sbsh_btn")
        self.horizontalLayout_14.addWidget(self.wed_sbsh_btn)
        self.thurs_sbsh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_sbsh_btn.setFont(font)
        self.thurs_sbsh_btn.setText("")
        self.thurs_sbsh_btn.setFlat(False)
        self.thurs_sbsh_btn.setObjectName("thurs_sbsh_btn")
        self.horizontalLayout_14.addWidget(self.thurs_sbsh_btn)
        self.fri_sbsh_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_sbsh_btn.setFont(font)
        self.fri_sbsh_btn.setText("")
        self.fri_sbsh_btn.setFlat(False)
        self.fri_sbsh_btn.setObjectName("fri_sbsh_btn")
        self.horizontalLayout_14.addWidget(self.fri_sbsh_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.p5_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p5_lb.setFont(font)
        self.p5_lb.setObjectName("p5_lb")
        self.horizontalLayout_15.addWidget(self.p5_lb)
        self.mon_p5_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_p5_btn.setFont(font)
        self.mon_p5_btn.setText("")
        self.mon_p5_btn.setFlat(False)
        self.mon_p5_btn.setObjectName("mon_p5_btn")
        self.horizontalLayout_15.addWidget(self.mon_p5_btn)
        self.tues_p5_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_p5_btn.setFont(font)
        self.tues_p5_btn.setText("")
        self.tues_p5_btn.setFlat(False)
        self.tues_p5_btn.setObjectName("tues_p5_btn")
        self.horizontalLayout_15.addWidget(self.tues_p5_btn)
        self.wed_p5_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_p5_btn.setFont(font)
        self.wed_p5_btn.setText("")
        self.wed_p5_btn.setFlat(False)
        self.wed_p5_btn.setObjectName("wed_p5_btn")
        self.horizontalLayout_15.addWidget(self.wed_p5_btn)
        self.thurs_p5_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_p5_btn.setFont(font)
        self.thurs_p5_btn.setText("")
        self.thurs_p5_btn.setFlat(False)
        self.thurs_p5_btn.setObjectName("thurs_p5_btn")
        self.horizontalLayout_15.addWidget(self.thurs_p5_btn)
        self.fri_p5_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_p5_btn.setFont(font)
        self.fri_p5_btn.setText("")
        self.fri_p5_btn.setFlat(False)
        self.fri_p5_btn.setObjectName("fri_p5_btn")
        self.horizontalLayout_15.addWidget(self.fri_p5_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.p6_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.p6_lb.setFont(font)
        self.p6_lb.setObjectName("p6_lb")
        self.horizontalLayout_17.addWidget(self.p6_lb)
        self.mon_p6_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_p6_btn.setFont(font)
        self.mon_p6_btn.setText("")
        self.mon_p6_btn.setFlat(False)
        self.mon_p6_btn.setObjectName("mon_p6_btn")
        self.horizontalLayout_17.addWidget(self.mon_p6_btn)
        self.tues_p6_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_p6_btn.setFont(font)
        self.tues_p6_btn.setText("")
        self.tues_p6_btn.setFlat(False)
        self.tues_p6_btn.setObjectName("tues_p6_btn")
        self.horizontalLayout_17.addWidget(self.tues_p6_btn)
        self.wed_p6_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_p6_btn.setFont(font)
        self.wed_p6_btn.setText("")
        self.wed_p6_btn.setFlat(False)
        self.wed_p6_btn.setObjectName("wed_p6_btn")
        self.horizontalLayout_17.addWidget(self.wed_p6_btn)
        self.thurs_p6_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_p6_btn.setFont(font)
        self.thurs_p6_btn.setText("")
        self.thurs_p6_btn.setFlat(False)
        self.thurs_p6_btn.setObjectName("thurs_p6_btn")
        self.horizontalLayout_17.addWidget(self.thurs_p6_btn)
        self.fri_p6_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_p6_btn.setFont(font)
        self.fri_p6_btn.setText("")
        self.fri_p6_btn.setFlat(False)
        self.fri_p6_btn.setObjectName("fri_p6_btn")
        self.horizontalLayout_17.addWidget(self.fri_p6_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.as_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.as_lb.setFont(font)
        self.as_lb.setObjectName("as_lb")
        self.horizontalLayout_18.addWidget(self.as_lb)
        self.mon_as_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mon_as_btn.setFont(font)
        self.mon_as_btn.setText("")
        self.mon_as_btn.setFlat(False)
        self.mon_as_btn.setObjectName("mon_as_btn")
        self.horizontalLayout_18.addWidget(self.mon_as_btn)
        self.tues_as_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tues_as_btn.setFont(font)
        self.tues_as_btn.setText("")
        self.tues_as_btn.setFlat(False)
        self.tues_as_btn.setObjectName("tues_as_btn")
        self.horizontalLayout_18.addWidget(self.tues_as_btn)
        self.wed_as_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wed_as_btn.setFont(font)
        self.wed_as_btn.setText("")
        self.wed_as_btn.setFlat(False)
        self.wed_as_btn.setObjectName("wed_as_btn")
        self.horizontalLayout_18.addWidget(self.wed_as_btn)
        self.thurs_as_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.thurs_as_btn.setFont(font)
        self.thurs_as_btn.setText("")
        self.thurs_as_btn.setFlat(False)
        self.thurs_as_btn.setObjectName("thurs_as_btn")
        self.horizontalLayout_18.addWidget(self.thurs_as_btn)
        self.fri_as_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fri_as_btn.setFont(font)
        self.fri_as_btn.setText("")
        self.fri_as_btn.setFlat(False)
        self.fri_as_btn.setObjectName("fri_as_btn")
        self.horizontalLayout_18.addWidget(self.fri_as_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.excel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.excel_btn.setObjectName("excel_btn")
        self.horizontalLayout_2.addWidget(self.excel_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.categories_ck = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.categories_ck.setFont(font)
        self.categories_ck.setObjectName("categories_ck")
        self.horizontalLayout_2.addWidget(self.categories_ck)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.term_settings_btn = QtWidgets.QPushButton(self.centralwidget)
        self.term_settings_btn.setObjectName("term_settings_btn")
        self.horizontalLayout_2.addWidget(self.term_settings_btn)
        self.write_btn = QtWidgets.QPushButton(self.centralwidget)
        self.write_btn.setObjectName("write_btn")
        self.horizontalLayout_2.addWidget(self.write_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Time Tabler to Outlook"))
        self.period_lb.setText(_translate("MainWindow", "Period"))
        self.mon_lb.setText(_translate("MainWindow", "Mon"))
        self.tues_lb.setText(_translate("MainWindow", "Tues"))
        self.wed_lb.setText(_translate("MainWindow", "Wed"))
        self.thurs_lb.setText(_translate("MainWindow", "Thurs"))
        self.fri_lb.setText(_translate("MainWindow", "Fri"))
        self.bs_lb.setText(_translate("MainWindow", "Before School"))
        self.bf_lb.setText(_translate("MainWindow", "Before Form"))
        self.f_lb.setText(_translate("MainWindow", "Form"))
        self.p1_lb.setText(_translate("MainWindow", "Period 1"))
        self.p2_lb.setText(_translate("MainWindow", "Period 2"))
        self.fbfh_lb.setText(_translate("MainWindow", "1st Break 1st Half"))
        self.fbsh_lb_2.setText(_translate("MainWindow", "1st Break 2nd Half"))
        self.p3_lb.setText(_translate("MainWindow", "Period 3"))
        self.p4_lb.setText(_translate("MainWindow", "Period 4"))
        self.sbfh_lb.setText(_translate("MainWindow", "2nd Break 1st Half"))
        self.sbsh_lb.setText(_translate("MainWindow", "2nd Break 2nd Half"))
        self.p5_lb.setText(_translate("MainWindow", "Period 5"))
        self.p6_lb.setText(_translate("MainWindow", "Period 6"))
        self.as_lb.setText(_translate("MainWindow", "After School"))
        self.excel_btn.setText(_translate("MainWindow", "Load Excel File"))
        self.categories_ck.setText(_translate("MainWindow", "Use Categories"))
        self.term_settings_btn.setText(_translate("MainWindow", "Term Settings"))
        self.write_btn.setToolTip(_translate("MainWindow", "Send lessons to Outllook Calendar"))
        self.write_btn.setText(_translate("MainWindow", "To Calendar"))
