import random
import datetime

current_time = datetime.datetime.now()
day = current_time.weekday()
print(day)

with open("quotes.txt", "r") as file:
    number = random.randint(1, 103)
    motivation = [i for i in file.readlines()]
    motivation_sentence_of_day = motivation[number]
    if day == 2:
        import smtplib

        my_email = "0furkangolpinar@gmail.com"
        password = "samanye415"

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="furkangolpinar@yahoo.com",
                            msg=f"{motivation_sentence_of_day}")
        connection.close()













