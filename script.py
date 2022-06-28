#i received a trades report at a particular time in an FTP folder, so I wrote this script to help me loop through the folder, read the report, and then send me an email to let me know if there was a trade above $100k for the day.

import os
import pandas as pd
from datetime import date
from smtplib import SMTP, SMTP_SSL
from email.message import EmailMessage

def email_func(email_content):
    email = EmailMessage()
    email['from'] = 'John Doe'
    email['to'] = 'recipient@email.com'
    email['subject'] = 'Some Email Subject'
    
    email.set_content(email_content)

    with SMTP(host='smtp.gmail.com', port = 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        
        smtp.login('sender@email.com', 'password123')
        smtp.send_message(email)
        print("all done")

def some_func():
	today = date.today()
	#folder name is in date format(yy-mm-dd)
	folder_name = today.strftime("%Y-%m-%d")
	file_path = "./"+ folder_name+"/"

	for file in os.listdir(file_path):
		if file.startswith("(first 4 chars of the file name)"):
			file_name = file.split(".")[0]
			print(file_path + file_name) #to confirm name is what you expected
			x=pd.read_csv(file)
			excel_file = x.to_excel(f'{file_name}.xlsx', index=0, header=True)
			
	file_data = pd.read_excel(f'{file_name}.xlsx')
	df = pd.DataFrame(file_data, columns = ["desired col"])
	
	max_value = df['desired col'].max()
	if max_value > int(target amount):
		email_content = "some text if any value is greater than target amount"
		email_func(email_content)
		

	else:
		email_content = "some text"
		
		email_func(email_content)
			
		
some_func()
			

