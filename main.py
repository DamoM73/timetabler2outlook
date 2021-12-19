from output import Calendar
from datastore import Datastore

#cal = Calendar()

#cal.write_appointment("2021-12-17 22:00", "Test", 30, "Home", "2")

db = Datastore("Sheet1.xlsx")

#print(db.get_value("A4"))
db.get_time_table()