import pandas as pd
import random
import datetime as dt
import smtplib

USER_MAIL = "briankipkemboi47@gmail.com"
PASSWORD = 'mnlfzmghyifmqrmc'


now = dt.datetime.now()
today = (now.month, now.day)

# Reading the file
data = pd.read_csv('birthdays.csv')

birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

# Check if the birthday exists
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER_MAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=USER_MAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n {contents}"
        )
