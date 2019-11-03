# Schedule Library imported 
import schedule 
import time as tm
from datetime import date, time, datetime, timedelta
from dateutil import parser, tz
import requests
import ezgmail
import twilio
import requests
from twilio.rest import Client

client = Client("AC066315c83117e061bea099233dab0a37", "5c04635c2f9ea9fe2bcf65142d41fe4d")
phone = input("What's your phone number? Phone Number: ")
email = input("What's your email? Email: ")

ask = "both"

def texting():
    client.messages.create(to=f"+1{phone}", from_="+19548591750", body=f"This period ends in {negtimin} minutes.")
    print("Text has been sent")

def emailing():
    subject = 'Reminder'
    text = (f"This period ends in {negtimin} minutes")
    ezgmail.send(email, subject, text)
    print("Email has been sent")

ask = input("Do you want the reminder to be in the form of an email and/or text? Write email, text, or both. Answer: ")



#brady.markson@pinecrest.edu




negtimin = input("How many minutes before do you want the notification to be? Minute(s): ")

negtimin_int = int(negtimin)




negative_x_min = timedelta(minutes=-negtimin_int)

url = 'http://pcbellschedule.azurewebsites.net/api/ftl/middleschool/schedule/'

headers = {'Accept': 'application/json'}

r = requests.get(url, headers=headers)
schedule_json = r.json()




def main():
  print("")
  print(f"Current time: {datetime.now()}")
  print("")
  print("Times used for Scheduling:")
  print("")
  for period in schedule_json['periods']:
    #print(f"End Time: {parser.parse(period['end_time'])}")
    scheduled_time = parser.parse(period['end_time']).astimezone(tz.UTC) + negative_x_min
    print(f"{negtimin} Minutes before end: {scheduled_time}")
    
    print(f"scheduled a task for {scheduled_time.strftime('%H:%M')}") 
    schedule.every().day.at(scheduled_time.strftime('%H:%M')).do(bedtime) 

def bedtime(): 
  if ask == "text":
    texting()

  elif ask == "email":
    emailing()

  elif ask == "both":
    emailing()
    texting()

if negtimin_int <= 60:
  if __name__=="__main__":
    main()
else:
  print(f"{negtimin_int} is not valid")




while True: 
  schedule.every().day.at(00:00).do(main())
  schedule.run_pending()
  tm.sleep(1)
  


#https://www.geeksforgeeks.org/python-schedule-library/