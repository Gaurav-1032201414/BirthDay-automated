##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.



# import statements

import pandas as pd
import datetime as dt
import smtplib
import random

MY_EMAIL = "MY_EMAIL"
MY_PASSWORD = "MY_PASSWORD"

birth_df = pd.read_csv("birthdays.csv")
# birth_df_dict = birth_df.to_dict(orient="records")

today = dt.datetime.now()
today_month = today.month
today_day = today.day

for index, row in birth_df.iterrows():
    if row["month"] == today_month and row["day"] == today_day:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", row["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs=row["email"], 
                msg=f"Subject: Happy Birthday!\n\n{letter}"
                )
