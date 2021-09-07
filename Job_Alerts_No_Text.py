#Where you are sourcing info from. Can Add additional contacts via excel file at any time without updating code
import pandas as pd
#Change out excel file below in same format (excel file must be saved in JunkInTheTrunk folder)
df = pd.read_excel("Labor_Contacts2.xlsx")

#Twilio Info for SMS Messaging, your computer must be connected to wifi
from twilio.rest import Client
accountSID = 'AC457e11a230554d7a9478b7e2f4ead262'
authToken = '1622ed7ecb95666f4d35c5b89b0332ff'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '7205717898'

#Input from Arnold
confirmation = ""
while confirmation != 'YES':
    job_type = input("Hello Arnold, what skill level do you need for this job? SMALL, MEDIUM, or LARGE?")
    job_link = input("Please Copy and paste the link to this job. After pasting link hit space bar then enter")
    job_description = input("What would you like the text to say? Example New Job in High Point! If you get 404 error job has been claimed")
    confirmation = input("Does everything look okay? YES or NO")
    confirmation = confirmation.strip().upper()

#Pulling info from matching abilities to send texts to correct groups
job_ability = job_type.strip().upper()
job_link = job_link.strip()
job_description = job_description.strip()
contractors = len(df)
print(contractors)
x = 0
if job_ability == 'LARGE':
    while contractors > 0:
        if (df.iloc[x, 4]).upper() == 'LARGE':
            cell_phone = df.iloc[x,2]
            try:
                #message = twilioCli.messages.create(body=f'{job_description} {job_link}', from_=myTwilioNumber, to=cell_phone)
                print(f"text sent to {df.iloc[x,0]}, {df.iloc[x, 2]}")
            except:
                print(f"Unable to send to {df.iloc[x,0]}, {df.iloc[x, 2]} number not verified on Twilio")
            contractors = contractors - 1
            x = x + 1
        else:
            contractors = contractors - 1
            x = x + 1
elif job_ability == 'MEDIUM':
    while contractors > 0:
        if (df.iloc[x, 4]).upper() == 'LARGE':
            cell_phone = df.iloc[x, 2]
            try:
                message = twilioCli.messages.create(body=f'{job_description} {job_link}', from_=myTwilioNumber, to=cell_phone)
                print(f"text sent to {df.iloc[x,0]}, {df.iloc[x, 2]}")
            except:
                print(f"Unable to send to {df.iloc[x,0]}, {df.iloc[x, 2]} number not verified")
            contractors = contractors - 1
            x = x + 1
        elif (df.iloc[x, 4]).upper() == 'MEDIUM':
            cell_phone = df.iloc[x, 2]
            try:
                message = twilioCli.messages.create(body=f'{job_description} {job_link}', from_=myTwilioNumber, to=cell_phone)
                print(f"text sent to {df.iloc[x,0]}, {df.iloc[x, 2]}")
            except:
                print(f"Unable to send to {df.iloc[x,0]}, {df.iloc[x, 2]} number not verified")
            contractors = contractors - 1
            x = x + 1
        else:
            contractors = contractors - 1
            x = x + 1
elif job_ability == 'SMALL':
    while contractors > 0:
        cell_phone = df.iloc[x, 2]
        try:
            message = twilioCli.messages.create(body=f'New Job Available {job_link}', from_=myTwilioNumber, to=cell_phone)
            print(f"text sent to {df.iloc[x, 0]}, {df.iloc[x, 2]}")
        except:
            print(f"Unable to send to {df.iloc[x, 0]}, {df.iloc[x, 2]} number not verified")
        contractors = contractors - 1
        x = x + 1
else:
    print("No texts sent, be sure you specified a correct job type")
