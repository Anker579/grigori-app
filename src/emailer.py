import smtplib


class email_bot():
    
    def __init__(self):
        self.my_email = "testanguspython@gmail.com"
        self.password = "rfhetrkxkluhfnfv"
    #this email is only used for this so dont even think about it.

    def email_me(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email, to_addrs="angushoward03@gmail.com", msg="Subject:Weather Collection Failed\n\nnull")
    
if __name__ == "__main__":
    my_email_bot = email_bot()
    my_email_bot.email_me()
