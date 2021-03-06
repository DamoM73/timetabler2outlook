from PyQt6.QtWidgets import QDialog
from Ui_edit_lesson import Ui_Dialog
from PyQt6.QtGui import QIcon


class EditLesson:
    
    def __init__(self,lesson):
        self.window = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.setWindowIcon(QIcon("crest.png"))
        self.window.show()
        self.lesson = lesson
        self.ui.name_ent.setText(self.lesson.subject)
        self.ui.room_ent.setText(self.lesson.location)
        self.ui.category_ent.setText(self.lesson.category)
        self.signals()
        self.window.exec()
        

    def signals(self):
        self.ui.ok_btn.clicked.connect(self.ok_btn)
        self.ui.cancel_btn.clicked.connect(self.cancel_btn)
        

    # ---- Slots ---- #
    def ok_btn(self):
        self.lesson.subject = self.ui.name_ent.text()
        self.lesson.location = self.ui.room_ent.text()
        self.lesson.category = self.ui.category_ent.text()
        self.window.close()


    def cancel_btn(self):
        self.window.close()
        
        