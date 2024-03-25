# Birthday Email Sender

This project automates the process of sending birthday emails to individuals whose birthdays match the current date. It follows these steps:

1. Updates the `birthdays.csv` file with new data if necessary.
2. Checks if today's date matches a birthday in the `birthdays.csv`.
3. If there's a match, it selects a random letter template and replaces `[NAME]` with the person's actual name from `birthdays.csv`.
4. Sends the generated letter to the person's email address.

## Setup

1. **Python Environment**: Ensure you have Python installed on your system. This project was developed using Python 3. 

2. **Dependencies**: Install the required dependencies using the following command:
    `pip install pandas smtplib`

3. **Google Account Configuration**: You need a Gmail account to send emails. Enable "Less Secure Apps" access for your Google account or set up an app password if you have two-factor authentication enabled.

4. **Data Setup**: Modify the `birthdays.csv` file with the birthdays and email addresses of the individuals you want to send birthday emails to.

5. **Letter Templates**: Customize the letter templates in the `letter_templates` directory. Ensure they have placeholders like `[NAME]` that will be replaced with the recipient's name.

6. **Run the Script**: Execute the `birthday_email_sender.py` script to check for birthdays and send emails.


**Note**: Replace `MY_EMAIL` and `MY_PASSWORD` by you own email and app password to make the code to work.