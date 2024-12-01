import pandas as pd
import random
import datetime as dt
import smtplib

now = dt.datetime.now()
today_month = now.month
today_day = now.day

today = (today_month, today_day)
print(today)

# Reading the file
data = pd.read_csv('birthdays.csv')

#birthday_dict = {birthday_month: birthday_day for (index, data_roe) in data.iterrows()}



# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




