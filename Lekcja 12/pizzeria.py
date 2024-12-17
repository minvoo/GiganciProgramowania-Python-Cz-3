import json
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os 
import dotenv #pip install python-dotenv
import re

order = []
with open('menu.json', 'r', encoding='utf-8') as file:
    menu = json.load(file)
list_of_pizzas = menu["menu"]

list_of_pizza_names = []
for pizza in list_of_pizzas:
    list_of_pizza_names.append(pizza['pizza'])

def main_page():
    print('Witaj na stronie pizzerii "U Vita"')
    print('Wybierz akcje')
    print('1. Wyswietl menu')
    print('2. Dodaj picke do zamowienia')
    print('3. Wyczysc zamowienie')
    print('4. Wyslij zamowienie')
    print('5. Zakoncz ')
    option = input("")
    if option == '1':
        display_menu()
    elif option == '2':
        add_to_order()
    elif option == '3':
        order.clear()
        main_page()
    elif option == '4':
        send_order()
        main_page()
    elif option == '5':
        quit()
    else:
        print('Podano zla opcje!')
        main_page()


def display_menu():
    for pizza in list_of_pizzas:
        print(f'Pizza: {pizza['pizza']}')
        print(f'Skladniki: {', '.join(pizza['dodatki'])}')
        print(f'Ceny: Mala: {pizza['ceny']['S']} zł    Srednia: {pizza['ceny']['M']} zł      Duza: {pizza['ceny']['L']} zł  ')
        print('')
    input('Wcisnij cos aby wrocic do ekranu glownego')
    main_page()

def add_to_order():
    print("Którą pizzę chcesz zamówić: ")
    for pizza_name in list_of_pizza_names:
        print(f"{list_of_pizza_names.index(pizza_name)+1}.{pizza_name}")
    try:
        pizza_name_number = int(input("Podaj numer pizzy: "))
        if pizza_name_number > len(list_of_pizza_names) or pizza_name_number < 1:
            print("Pizza o podanym numerze nie istnieje")
            return_to_main_page()
    except:
        print("Należy wprowadzić liczbę całkowitą")
        return_to_main_page()

    try:
        pizza_amount = int(input("Ile pizz chcesz zamówić: "))
        if pizza_amount < 1:
            print("Należy zamówić co najmniej jedną pizze")
            return_to_main_page()
        else:
            pass
    except:
        print("Należy wprowadzić liczbę całkowitą")
        return_to_main_page()

    size = input("Jakie rozmiary mają być pizze (S/M/L): ")
    if size.upper() not in "SML":
        print("Podano zły rozmiar pizzy")
        return_to_main_page()
    else:
        size = size.upper()

    order.append({'size':size, 'pizza_amount':pizza_amount, 'pizza_name':list_of_pizza_names[pizza_name_number-1]})
    print(f"Dodano {pizza_amount} x {list_of_pizza_names[pizza_name_number-1]}[{size}] do zamowienia")
    return_to_main_page()


def calculate_cost(ordered_pizza):
    for pizza in list_of_pizzas:
        if pizza['pizza'] == ordered_pizza['pizza_name']:
            cost = int(ordered_pizza['pizza_amount']) * int(pizza["ceny"][ordered_pizza['size']])
    return cost

def send_email(message_txt, recipient_email):
    dotenv.load_dotenv()
    subject = "Pizzeria u Vita - potwierdzenia zamowienia"
    sender_email = os.getenv('sender_email')
    sender_password = os.getenv('sender_password')
    smtp_server = "smtp.wp.pl"
    smtp_port = 587  
    
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email
    body_part = MIMEText(message_txt)
    message.attach(body_part)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())


def send_order():
    if not order:
        print("Nie można zrealizować pustego zamówienia")
        return_to_main_page()

    recipient_mail = prompt_for_email()
    tekst = "Dziękujemy za wybranie pizzeri u Vita, oto podsumowanie Twojego zamówinia:\n"
    total_cost = 0
    for pizza in order:
        cost = calculate_cost(pizza)
        tekst+=f"{pizza['pizza_amount']} x {pizza['pizza_name']}[{pizza['size']}] : {cost}zł\n"
        total_cost += cost
    tekst += f"Łączny koszt: {total_cost} zł"
    send_email(tekst, recipient_mail)
    print("Zamówienie zostało złożone")
    input("Wciśnij enter aby kontynuować")

def show_number_warning():
    print('Nalezy podac liczbe calkowita')
    return_to_main_page()


def return_to_main_page():
    time.sleep(3)
    main_page()

def prompt_for_email():
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    while True:
        email = input("Podaj swój adres email (wyslemy na niego zamowienie): ")
        if re.match(email_regex, email):
            print("Podano prawidłowy adres email.")
            return email
        else:
            print("Nieprawidłowy adres email. Spróbuj ponownie.")

main_page()