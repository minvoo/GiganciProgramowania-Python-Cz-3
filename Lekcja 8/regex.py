import re

sentence = "Ala ma kota"
result = re.match(r"Ala", "Ala ma kota")
print(f"Wyszukiwanie elementu Ala {result}")



napis = "Ala ma 123 jabłka"
result = re.search(r"\d+", napis)
print(f"Wyszukiwanie liczby zakończone, wykryto: {result}")


napis = "Ala i Kuba jadą na wycieCzkę do Warszawy"
result = re.findall(r"\b[A-Z][a-z]+", napis)
print(f"Wyszukiwanie wyrazów zaczynających się wielką literą zakończone, wykryto:{result}")


text = "Valorant to najlepsza strzelanka na świecie"
pattern = "Valorant"
replacement = "CS"
new_text = re.sub(pattern, replacement, text)
print(new_text)

