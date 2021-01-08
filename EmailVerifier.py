
#Type this in your command prompt if you dont have these installed 


from emailverifier import Client		#pip install email-verifier
from emailverifier import exceptions
import re    							#pip install regex 

client = Client('at_1bTGUCnOaIIaxviZfTVSSFhCEJWd6')

#Regular Experessions
gmail_reg = '^[a-z0-9](\.?[a-z0-9]){5,30}@g(oogle)?mail\.com$'
hotmail_reg = '^[a-zA-Z0-9-_\.+]{5,}@(live|hotmail)(\.[a-z]{2,3}){1,2}'

#You can add the required domains yourself
doms = ['@hotmail.com', '@gmail.com']

#Temporary Class to facilitate better handling 
class data:
	smtp_check = 'False'


#Enter the name of the file the mail should be stored in
writeToFile = open("AvailableEmail.txt", "w")
            
with open("Names.txt", "r") as NamesFile:
	for name in NamesFile:
		name = name.rstrip()
		for domain in doms:
  
			mail = name + domain

			if re.search(gmail_reg, mail) or re.search(hotmail_reg, mail):  

				try:
					data = client.get(mail)
					
				except Exception as e:
					print("dadadadad")
					data.smtp_check = 'False'
					print(e.with_traceback)
            
				if str(data.smtp_check) == 'True':
				
					print("{} : The chosen username is already in use by someone".format(mail))
				else:
					print("{} : The mail is available".format(mail))
					writeToFile.write(mail + '\n')
			
			else:
				print("{} : Invalid Username".format(mail))

