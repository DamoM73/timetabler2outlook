from PyQt6.QtWidgets import QDialog, QMessageBox
from Ui_term_settings import Ui_Dialog
from PyQt6.QtGui import QIcon


class TermSettings:
    
    def __init__(self,term_values):
        self.window = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.signals()
        self.term_values = term_values
        self.set_values()
        self.window.show()
        self.window.setWindowIcon(QIcon("crest.png"))
        self.window.exec()
        

    def signals(self):
        self.ui.ok_btn.clicked.connect(self.ok_btn)
        self.ui.cancel_btn.clicked.connect(self.cancel_btn)


    def set_values(self):
        # dates
        self.ui.term_1_start_dt.setDate(self.term_values.term_1_start)
        self.ui.term_1_end_dt.setDate(self.term_values.term_1_end)
        self.ui.term_2_start_dt.setDate(self.term_values.term_2_start)
        self.ui.term_2_end_dt.setDate(self.term_values.term_2_end)
        self.ui.term_3_start_dt.setDate(self.term_values.term_3_start)
        self.ui.term_3_end_dt.setDate(self.term_values.term_3_end)
        self.ui.term_4_start_dt.setDate(self.term_values.term_4_start)
        self.ui.term_4_end_dt.setDate(self.term_values.term_4_end)
        # check boxes
        self.ui.term_1_write_ck.setChecked(self.term_values.term_1_write)
        self.ui.term_2_write_ck.setChecked(self.term_values.term_2_write)
        self.ui.term_3_write_ck.setChecked(self.term_values.term_3_write)
        self.ui.term_4_write_ck.setChecked(self.term_values.term_4_write)


    def check_term_dates(self):
        if self.ui.term_1_write_ck.isChecked and self.ui.term_1_start_dt.date() >= self.ui.term_1_end_dt.date():
            return False
        elif self.ui.term_2_write_ck.isChecked and self.ui.term_2_start_dt.date() >= self.ui.term_2_end_dt.date():
            return False
        elif self.ui.term_3_write_ck.isChecked and self.ui.term_3_start_dt.date() >= self.ui.term_3_end_dt.date():
            return False
        elif self.ui.term_4_write_ck.isChecked and self.ui.term_4_start_dt.date() >= self.ui.term_4_end_dt.date():
            return False
        else:
            return True


    def error_msg(self):
        msg = QMessageBox()
        msg.setText("Error in dates!")
        msg.setInformativeText("Ensure term end dates are later than start dates")
        msg.setWindowTitle("Error")
        msg.exec()
        
    # ---- Slots ---- #
    def ok_btn(self):
        if self.check_term_dates():
            self.term_values.term_1_start = self.ui.term_1_start_dt.date()
            self.term_values.term_1_end = self.ui.term_1_end_dt.date()
            self.term_values.term_1_write = self.ui.term_1_write_ck.isChecked()
            self.term_values.term_2_start = self.ui.term_2_start_dt.date()
            self.term_values.term_2_end = self.ui.term_2_end_dt.date()
            self.term_values.term_2_write = self.ui.term_2_write_ck.isChecked()
            self.term_values.term_3_start = self.ui.term_3_start_dt.date()
            self.term_values.term_3_end = self.ui.term_3_end_dt.date()
            self.term_values.term_3_write = self.ui.term_3_write_ck.isChecked()
            self.term_values.term_4_start = self.ui.term_4_start_dt.date()
            self.term_values.term_4_end = self.ui.term_4_end_dt.date()
            self.term_values.term_4_write = self.ui.term_4_write_ck.isChecked()
            self.window.close()
        else:
            self.error_msg()
            


    def cancel_btn(self):
        self.window.close()


    
