# Form implementation generated from reading ui file 'h:\GIT\timetabler2outlook\edit_lesson.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 179)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_ent = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_ent.setFont(font)
        self.name_ent.setObjectName("name_ent")
        self.verticalLayout.addWidget(self.name_ent)
        self.room_ent = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.room_ent.setFont(font)
        self.room_ent.setObjectName("room_ent")
        self.verticalLayout.addWidget(self.room_ent)
        self.category_ent = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.category_ent.setFont(font)
        self.category_ent.setObjectName("category_ent")
        self.verticalLayout.addWidget(self.category_ent)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout_2.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_2.addWidget(self.cancel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit Lesson Details"))
        self.label.setText(_translate("Dialog", "Edit Lesson Details"))
        self.label_2.setText(_translate("Dialog", "Lesson Name"))
        self.label_3.setText(_translate("Dialog", "Lesson Room"))
        self.label_4.setText(_translate("Dialog", "Category       "))
        self.ok_btn.setText(_translate("Dialog", "Ok"))
        self.cancel_btn.setText(_translate("Dialog", "Cancel"))
