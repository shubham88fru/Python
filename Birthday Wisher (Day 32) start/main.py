import smtplib

my_email = "email@email.com"
password = "abcd1234()"
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="somemail@email.com", msg="Subject: Hi\n\nHello World!")