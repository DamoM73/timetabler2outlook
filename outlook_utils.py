import win32com.client

class Calendar:
    
    def __init__(self):
        self.outlook = win32com.client.Dispatch("Outlook.Application")
        
        
    def write_appointment(self, start, subject, duration, location):
        """
        start: str "YYYY-MM-DD HH:MM"
        subject: str
        duration: int
        location: str
        """
        
        appt = self.outlook.CreateItem(1)
        appt.Start = start
        appt.Subject = subject
        appt.Duration = duration
        appt.Location = location
        appt.MeetingStatus = 1

        appt.Save()
        appt.Send()

class Lesson:
    
    def __init__(self, day, period, subject, start, duration, location):
        self.day = day
        self.period = period
        self.subject = subject
        self.start = start
        self.duration = duration
        self.location = location
        
    
    def show_lesson(self):
        print(self.day, self.period, self.subject, self.start, self.duration, self.location)