from Ui_edit_lesson import Ui_Dialog
from PyQt6 import QtCore, QtGui, QtWidgets


class LessonEdit:
    
    def __init__(self,lesson):
        self.lesson = lesson
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ui.name_ent.setText(lesson.subject)
        ui.room_ent.setText(lesson.location)
        
        Dialog.show()
        rsp = Dialog.exec()
        
        