# https://pastebin.com/PL3HQ5TD

import json
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os 
import dotenv #pip install python-dotenv

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
    print('Ktora picke chcesz zamowic?')
    for pizza_name in list_of_pizza_names:
        print(f'{list_of_pizza_names.index(pizza_name)+1}. {pizza_name}')
    
    try:
        pizza_name_number = input = int(input('Podaj numer picki: '))
        if pizza_name_number > len(list_of_pizza_names) or pizza_name_number < 1:
            print('Picka o takim nr nie istnieje!')
            return_to_main_page()
    except:
        show_number_warning()
    try:
        pizza_amount = int(input('Ile pizz chcesz zamowic?: '))
        if pizza_amount < 1:
            print('Nalezy zamowic co najmniej jedna picke')
            return_to_main_page()
        else:
            pass
    except:
        show_number_warning()

def show_number_warning():
    print('Nalezy podac liczbe calkowita')
    return_to_main_page()


def return_to_main_page():
    time.sleep(3)
    main_page()


def send_order():
    print('')

main_page()