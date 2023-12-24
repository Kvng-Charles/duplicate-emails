import pandas as pd


mail_list = []
person_dict = {}

#---------------------------COLLECT USER DATA--------------------------------#

for n in range (3):
    mail = input("What is your email? /n")
    mail_list.append(mail)

#----------------------------------------------------------------------------#
#------------------------------CREATE TABLE----------------------------------#

person_dict["email"] = mail_list

person_table = pd.DataFrame(person_dict)

#----------------------------------------------------------------------------#
#------------------------DELETE DUPLICATE EMAILS-----------------------------#

table_list = []

for index, row in person_table.iterrows():
    if row['email'] in table_list:
        person_table.drop(index, inplace=True)
    else:
        table_list.append(row['email'])

print(person_table)
#----------------------------------------------------------------------------#