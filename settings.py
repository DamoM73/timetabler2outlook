from PyQt6.QtCore import QDate

class TermValues:
    
    def __init__(self):
        self.term_1_start = QDate.currentDate()
        self.term_1_end = QDate.currentDate().addDays(1)
        self.term_1_write = False
        self.term_2_start = QDate.currentDate()
        self.term_2_end = QDate.currentDate().addDays(1)
        self.term_2_write = False
        self.term_3_start = QDate.currentDate()
        self.term_3_end = QDate.currentDate().addDays(1)
        self.term_3_write = False
        self.term_4_start = QDate.currentDate()
        self.term_4_end = QDate.currentDate().addDays(1)
        self.term_4_write = False
        

class UserOptions:
    
    def __init__(self):
        self.categories = False