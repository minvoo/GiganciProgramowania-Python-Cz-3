kontakty = {
    'Tomek': '123-456',
    'Anna': '987-654',
    'Kasia': '654-321'
}

if 'Anna' in kontakty:
    kontakty.pop('Anna')
    kontakty.setdefault('Piotr', '987-321')
    print(kontakty)