from openpyxl import load_workbook

class Datastore:
    
    def __init__(self,file):
        self.workbook = load_workbook(filename = file)
        self.sheet = self.workbook.active
                
                
    def get_value(self,cell):
        return self.sheet[cell].value
    
    def get_time_table(self):
        for row in self.sheet.iter_rows(min_row = 4,
                                       max_row = 8, 
                                       min_col = 2,
                                       max_col = 15,
                                       values_only = True):
            print(row)


class Session:
    
    def __init__(self)