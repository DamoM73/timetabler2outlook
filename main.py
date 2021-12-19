from output import Calendar, Lesson
from datastore import Datastore

def get_lesson_and_room(raw):
    """
    extracts the lesson name and the room name from the value sent
    """
    if raw.find("\n") == -1:
        return(raw,None)
    else:
        name = raw[:raw.find("\n")]
        less_lesson = raw[raw.find("\n") + 1:]
        room = less_lesson[:less_lesson.find("\n")]
        return(name,room)


# ---- extract information from the spreadsheet
db = Datastore("Sheet1.xlsx")

periods = db.get_period_names()
days = db.get_time_table()

# ---- Create the lessons ---- #
lessons = []
day_names = ["Mon", "Tues", "Wed", "Thurs", "Fri"]
lesson_times = [("",0),("08:00",20),("08:20",10,),("08:30",55),("09:25",55),("10:20",15),("10:35",15),
                ("10:50",55),("11:45",55),("12:40",20),("13:00",20),("13:20",55),("14:15",55),("3:10",20)]

for day_num, day in enumerate(days):
    for period_num, lesson in enumerate(day):
        if lesson != "":
            lesson_day = day_names[day_num]
            lesson_period = periods[period_num]
            lesson_time = lesson_times[period_num][0]
            lesson_duration = lesson_times[period_num][1]
            lesson_name, lesson_room = get_lesson_and_room(lesson)
                
            lessons.append(Lesson(lesson_day, lesson_period, lesson_name, lesson_time, lesson_duration, lesson_room))
            
for lesson in lessons:
    lesson.show_lesson()