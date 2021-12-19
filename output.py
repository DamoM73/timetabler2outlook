import win32com.client

class Calendar:
    
    def __init__(self):
        self.outlook = win32com.client.Dispatch("Outlook.Application")
        
        
    def write_appointment(self, start, subject, duration, location, repeats):
        """
        start: str "YYYY-MM-DD HH:MM"
        subject: str
        duration: int
        location: str
        repeats: str
        """
        
        appt = self.outlook.CreateItem(1)
        appt.Start = start
        appt.Subject = subject
        appt.Duration = duration
        appt.Location = location
        appt.MeetingStatus = 1

        pattern = appt.GetRecurrencePattern()
        pattern.RecurrenceType = 1
        pattern.Occurrences = repeats

        appt.Save()
        appt.Send()
