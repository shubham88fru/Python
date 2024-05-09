import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

my_email = "email@email.com"
password = "abcd1234()"

if weekday == 0:
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="somemail@email.com",
                            msg=f"Subject: Monday Motivation\n\n{quote}"
                            )
