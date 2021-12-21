import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Ui_tt2outlook import Ui_MainWindow
from outlook_utils import Calendar, Lesson
from datastore import Datastore


class MainWindow:
    def __init__(self):
        # ---- Initialise GUI elements ----#
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        # ---- Extract details from Datastore
        self.db = Datastore()
        self.lessons = self.db.create_lessons()
        #self.test_data()
        
        

    def show(self):
        self.main_win.show()
        
    def test_data(self):
        for lesson in self.lessons:
            if lesson != None:
                lesson.show_lesson()
            else:
                print(None)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
    
    
    

            
