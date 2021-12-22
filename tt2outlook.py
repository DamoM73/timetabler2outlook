import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Ui_tt2outlook import Ui_MainWindow
from outlook_utils import Calendar, Lesson, TermValues
from datastore import Datastore
from edit_lesson import EditLesson
from term_settings import TermSettings



class MainWindow:
    def __init__(self):
        # ---- Initialise GUI elements ----#
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        
        # ---- Extract details from Datastore
        self.db = Datastore()
        self.lessons = self.db.create_lessons()
        
        # ---- Variables ---- #
        self.term_values = TermValues()
        
        self.write_lessons()
        self.signals()


    def show(self):
        self.main_win.show()

        
    def test_data(self):
        for lesson in self.lessons:
            if lesson != None:
                lesson.show_lesson()
            else:
                print(None)


    def write_to_button(self,button,lesson):
        if lesson != None:
            button.setText(lesson.subject+"\n"+lesson.location)


    def write_lessons(self):
        self.write_to_button(self.ui.mon_bs_btn,self.lessons[0])
        self.write_to_button(self.ui.mon_bf_btn,self.lessons[1])
        self.write_to_button(self.ui.mon_f_btn,self.lessons[2])
        self.write_to_button(self.ui.mon_p1_btn,self.lessons[3])
        self.write_to_button(self.ui.mon_p2_btn,self.lessons[4])
        self.write_to_button(self.ui.mon_fbfh_btn,self.lessons[5])
        self.write_to_button(self.ui.mon_fbsh_btn,self.lessons[6])
        self.write_to_button(self.ui.mon_p3_btn,self.lessons[7])
        self.write_to_button(self.ui.mon_p4_btn,self.lessons[8])
        self.write_to_button(self.ui.mon_sbfh_btn,self.lessons[9])
        self.write_to_button(self.ui.mon_sbsh_btn,self.lessons[10])
        self.write_to_button(self.ui.mon_p5_btn,self.lessons[11])
        self.write_to_button(self.ui.mon_p6_btn,self.lessons[12])
        self.write_to_button(self.ui.mon_as_btn,self.lessons[13])
        self.write_to_button(self.ui.tues_bs_btn,self.lessons[14])
        self.write_to_button(self.ui.tues_bf_btn,self.lessons[15])
        self.write_to_button(self.ui.tues_f_btn,self.lessons[16])
        self.write_to_button(self.ui.tues_p1_btn,self.lessons[17])
        self.write_to_button(self.ui.tues_p2_btn,self.lessons[18])
        self.write_to_button(self.ui.tues_fbfh_btn,self.lessons[19])
        self.write_to_button(self.ui.tues_fbsh_btn,self.lessons[20])
        self.write_to_button(self.ui.tues_p3_btn,self.lessons[21])
        self.write_to_button(self.ui.tues_p4_btn,self.lessons[22])
        self.write_to_button(self.ui.tues_sbfh_btn,self.lessons[23])
        self.write_to_button(self.ui.tues_sbsh_btn,self.lessons[24])
        self.write_to_button(self.ui.tues_p5_btn,self.lessons[25])
        self.write_to_button(self.ui.tues_p6_btn,self.lessons[26])
        self.write_to_button(self.ui.tues_as_btn,self.lessons[27])
        self.write_to_button(self.ui.wed_bs_btn,self.lessons[28])
        self.write_to_button(self.ui.wed_bf_btn,self.lessons[29])
        self.write_to_button(self.ui.wed_f_btn,self.lessons[30])
        self.write_to_button(self.ui.wed_p1_btn,self.lessons[31])
        self.write_to_button(self.ui.wed_p2_btn,self.lessons[32])
        self.write_to_button(self.ui.wed_fbfh_btn,self.lessons[33])
        self.write_to_button(self.ui.wed_fbsh_btn,self.lessons[34])
        self.write_to_button(self.ui.wed_p3_btn,self.lessons[35])
        self.write_to_button(self.ui.wed_p4_btn,self.lessons[36])
        self.write_to_button(self.ui.wed_sbfh_btn,self.lessons[37])
        self.write_to_button(self.ui.wed_sbsh_btn,self.lessons[38])
        self.write_to_button(self.ui.wed_p5_btn,self.lessons[39])
        self.write_to_button(self.ui.wed_p6_btn,self.lessons[40])
        self.write_to_button(self.ui.wed_as_btn,self.lessons[41])
        self.write_to_button(self.ui.thurs_bs_btn,self.lessons[42])
        self.write_to_button(self.ui.thurs_bf_btn,self.lessons[43])
        self.write_to_button(self.ui.thurs_f_btn,self.lessons[44])
        self.write_to_button(self.ui.thurs_p1_btn,self.lessons[45])
        self.write_to_button(self.ui.thurs_p2_btn,self.lessons[46])
        self.write_to_button(self.ui.thurs_fbfh_btn,self.lessons[47])
        self.write_to_button(self.ui.thurs_fbsh_btn,self.lessons[48])
        self.write_to_button(self.ui.thurs_p3_btn,self.lessons[49])
        self.write_to_button(self.ui.thurs_p4_btn,self.lessons[50])
        self.write_to_button(self.ui.thurs_sbfh_btn,self.lessons[51])
        self.write_to_button(self.ui.thurs_sbsh_btn,self.lessons[52])
        self.write_to_button(self.ui.thurs_p5_btn,self.lessons[53])
        self.write_to_button(self.ui.thurs_p6_btn,self.lessons[54])
        self.write_to_button(self.ui.thurs_as_btn,self.lessons[55])
        self.write_to_button(self.ui.fri_bs_btn,self.lessons[56])
        self.write_to_button(self.ui.fri_bf_btn,self.lessons[57])
        self.write_to_button(self.ui.fri_f_btn,self.lessons[58])
        self.write_to_button(self.ui.fri_p1_btn,self.lessons[59])
        self.write_to_button(self.ui.fri_p2_btn,self.lessons[60])
        self.write_to_button(self.ui.fri_fbfh_btn,self.lessons[61])
        self.write_to_button(self.ui.fri_fbsh_btn,self.lessons[62])
        self.write_to_button(self.ui.fri_p3_btn,self.lessons[63])
        self.write_to_button(self.ui.fri_p4_btn,self.lessons[64])
        self.write_to_button(self.ui.fri_sbfh_btn,self.lessons[65])
        self.write_to_button(self.ui.fri_sbsh_btn,self.lessons[66])
        self.write_to_button(self.ui.fri_p5_btn,self.lessons[67])
        self.write_to_button(self.ui.fri_p6_btn,self.lessons[68])
        self.write_to_button(self.ui.fri_as_btn,self.lessons[69])
                

    def format_date(self,date):
        day = date.day()
        month = date.month()
        year = date.year()
        
        if day < 10:
            day = "0" + str(day)
        else:
            day = str(day)
            
        if month < 10:
            month = "0" + str(month)
        else:
            month = str(month)
            
        return f"{year}-{month}-{day}"



    def signals(self):
        # ---- control buttons ---- #
        self.ui.term_settings_btn.clicked.connect(lambda: self.term_settings(self.term_values))
        # ---- lessons buttons ---- #
        self.ui.mon_bs_btn.clicked.connect(lambda: self.edit_lesson(0))
        self.ui.mon_bf_btn.clicked.connect(lambda: self.edit_lesson(1))
        self.ui.mon_f_btn.clicked.connect(lambda: self.edit_lesson(2))
        self.ui.mon_p1_btn.clicked.connect(lambda: self.edit_lesson(3))
        self.ui.mon_p2_btn.clicked.connect(lambda: self.edit_lesson(4))
        self.ui.mon_fbfh_btn.clicked.connect(lambda: self.edit_lesson(5))
        self.ui.mon_fbsh_btn.clicked.connect(lambda: self.edit_lesson(6))
        self.ui.mon_p3_btn.clicked.connect(lambda: self.edit_lesson(7))
        self.ui.mon_p4_btn.clicked.connect(lambda: self.edit_lesson(8))
        self.ui.mon_sbfh_btn.clicked.connect(lambda: self.edit_lesson(9))
        self.ui.mon_sbsh_btn.clicked.connect(lambda: self.edit_lesson(10))
        self.ui.mon_p5_btn.clicked.connect(lambda: self.edit_lesson(11))
        self.ui.mon_p6_btn.clicked.connect(lambda: self.edit_lesson(12))
        self.ui.mon_as_btn.clicked.connect(lambda: self.edit_lesson(13))
        self.ui.tues_bs_btn.clicked.connect(lambda: self.edit_lesson(14))
        self.ui.tues_bf_btn.clicked.connect(lambda: self.edit_lesson(15))
        self.ui.tues_f_btn.clicked.connect(lambda: self.edit_lesson(16))
        self.ui.tues_p1_btn.clicked.connect(lambda: self.edit_lesson(17))
        self.ui.tues_p2_btn.clicked.connect(lambda: self.edit_lesson(18))
        self.ui.tues_fbfh_btn.clicked.connect(lambda: self.edit_lesson(19))
        self.ui.tues_fbsh_btn.clicked.connect(lambda: self.edit_lesson(20))
        self.ui.tues_p3_btn.clicked.connect(lambda: self.edit_lesson(21))
        self.ui.tues_p4_btn.clicked.connect(lambda: self.edit_lesson(22))
        self.ui.tues_sbfh_btn.clicked.connect(lambda: self.edit_lesson(23))
        self.ui.tues_sbsh_btn.clicked.connect(lambda: self.edit_lesson(24))
        self.ui.tues_p5_btn.clicked.connect(lambda: self.edit_lesson(25))
        self.ui.tues_p6_btn.clicked.connect(lambda: self.edit_lesson(26))
        self.ui.tues_as_btn.clicked.connect(lambda: self.edit_lesson(27))
        self.ui.wed_bs_btn.clicked.connect(lambda: self.edit_lesson(28))
        self.ui.wed_bf_btn.clicked.connect(lambda: self.edit_lesson(29))
        self.ui.wed_f_btn.clicked.connect(lambda: self.edit_lesson(30))
        self.ui.wed_p1_btn.clicked.connect(lambda: self.edit_lesson(31))
        self.ui.wed_p2_btn.clicked.connect(lambda: self.edit_lesson(32))
        self.ui.wed_fbfh_btn.clicked.connect(lambda: self.edit_lesson(33))
        self.ui.wed_fbsh_btn.clicked.connect(lambda: self.edit_lesson(34))
        self.ui.wed_p3_btn.clicked.connect(lambda: self.edit_lesson(35))
        self.ui.wed_p4_btn.clicked.connect(lambda: self.edit_lesson(36))
        self.ui.wed_sbfh_btn.clicked.connect(lambda: self.edit_lesson(37))
        self.ui.wed_sbsh_btn.clicked.connect(lambda: self.edit_lesson(38))
        self.ui.wed_p5_btn.clicked.connect(lambda: self.edit_lesson(39))
        self.ui.wed_p6_btn.clicked.connect(lambda: self.edit_lesson(40))
        self.ui.wed_as_btn.clicked.connect(lambda: self.edit_lesson(41))
        self.ui.thurs_bs_btn.clicked.connect(lambda: self.edit_lesson(42))
        self.ui.thurs_bf_btn.clicked.connect(lambda: self.edit_lesson(43))
        self.ui.thurs_f_btn.clicked.connect(lambda: self.edit_lesson(44))
        self.ui.thurs_p1_btn.clicked.connect(lambda: self.edit_lesson(45))
        self.ui.thurs_p2_btn.clicked.connect(lambda: self.edit_lesson(46))
        self.ui.thurs_fbfh_btn.clicked.connect(lambda: self.edit_lesson(47))
        self.ui.thurs_fbsh_btn.clicked.connect(lambda: self.edit_lesson(48))
        self.ui.thurs_p3_btn.clicked.connect(lambda: self.edit_lesson(49))
        self.ui.thurs_p4_btn.clicked.connect(lambda: self.edit_lesson(50))
        self.ui.thurs_sbfh_btn.clicked.connect(lambda: self.edit_lesson(51))
        self.ui.thurs_sbsh_btn.clicked.connect(lambda: self.edit_lesson(52))
        self.ui.thurs_p5_btn.clicked.connect(lambda: self.edit_lesson(53))
        self.ui.thurs_p6_btn.clicked.connect(lambda: self.edit_lesson(54))
        self.ui.thurs_as_btn.clicked.connect(lambda: self.edit_lesson(55))
        self.ui.fri_bs_btn.clicked.connect(lambda: self.edit_lesson(56))
        self.ui.fri_bf_btn.clicked.connect(lambda: self.edit_lesson(57))
        self.ui.fri_f_btn.clicked.connect(lambda: self.edit_lesson(58))
        self.ui.fri_p1_btn.clicked.connect(lambda: self.edit_lesson(59))
        self.ui.fri_p2_btn.clicked.connect(lambda: self.edit_lesson(60))
        self.ui.fri_fbfh_btn.clicked.connect(lambda: self.edit_lesson(61))
        self.ui.fri_fbsh_btn.clicked.connect(lambda: self.edit_lesson(62))
        self.ui.fri_p3_btn.clicked.connect(lambda: self.edit_lesson(63))
        self.ui.fri_p4_btn.clicked.connect(lambda: self.edit_lesson(64))
        self.ui.fri_sbfh_btn.clicked.connect(lambda: self.edit_lesson(65))
        self.ui.fri_sbsh_btn.clicked.connect(lambda: self.edit_lesson(66))
        self.ui.fri_p5_btn.clicked.connect(lambda: self.edit_lesson(67))
        self.ui.fri_p6_btn.clicked.connect(lambda: self.edit_lesson(68))
        self.ui.fri_as_btn.clicked.connect(lambda: self.edit_lesson(69))
        
    
    
    # ---- Slots ---- #
    def edit_lesson(self,lesson_num):
        lesson = self.lessons[lesson_num]
        EditLesson(lesson)
        self.write_lessons()
        
    def term_settings(self,term_values):
        TermSettings(term_values)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())