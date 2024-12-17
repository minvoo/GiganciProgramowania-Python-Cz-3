import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv  # pip install python-dotenv
import re

recipient = ""  # Globalna zmienna na email

def app():
    print('Email spammer')
    menu()

def menu():
    global recipient  # Deklaracja użycia globalnej zmiennej
    print('1. Podaj maila docelowego')
    print('2. Wyslij wiadomosc')
    option = input("")
    if option == '1':
        prompt_for_email()
        menu()
    elif option == '2':
        process_send()
    else:
        print('Podano nieprawidłową liczbę')
        menu()

def process_send():
    global recipient  # Deklaracja użycia globalnej zmiennej
    if not recipient:  # Sprawdzenie, czy recipient jest pusty
        print('Nie podałeś maila')
        prompt_for_email()

    try:
        amount = int(input('Ile maili wysłać?: '))
        if amount > 0:
            send_email(amount)
        else:
            print('Liczba wysłanych maili musi wynosić przynajmniej 1')
            menu()
    except ValueError:
        print("Należy wprowadzić liczbę całkowitą")
        menu()

def send_email(amount):
    dotenv.load_dotenv()
    subject = "Przykładowy temat"
    sender_email = os.getenv('sender_email')
    sender_password = os.getenv('sender_password')
    smtp_server = "smtp.wp.pl"
    smtp_port = 587

    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient
    body_part = MIMEText("To jest wiadomość")
    message.attach(body_part)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        for i in range(amount):
            server.sendmail(sender_email, recipient, message.as_string())
    print('Maile wysłane')

def prompt_for_email():
    global recipient  # Deklaracja użycia globalnej zmiennej
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    while True:
        email = input("Podaj email, na który wysłać maile: ")
        if re.match(email_regex, email):
            print("Podano prawidłowy adres email.")
            recipient = email  # Przypisanie do globalnej zmiennej
            return
        else:
            print("Nieprawidłowy adres email. Spróbuj ponownie.")

app()