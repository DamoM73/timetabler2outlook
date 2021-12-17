import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application")

appt = outlook.CreateItem(1) # AppointmentItem
appt.Start = "2021-12-17 16:00" # yyyy-MM-dd hh:mm
appt.Subject = "Subject of the meeting"
appt.Duration = 60 # In minutes (60 Minutes)
appt.Location = "Location Name"
appt.MeetingStatus = 1 # 1 - olMeeting; Changing the appointment to meeting. Only after changing the meeting status recipients can be added

pattern = appt.GetRecurrencePattern()
pattern.RecurrenceType = 1
pattern.Occurrences = "2"

appt.Save()
appt.Send()