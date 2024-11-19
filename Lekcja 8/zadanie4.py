import re
#4. pastebin.com/LKAnxzWU -tresc zadania 
# (Znajdź wszystkie daty w formacie DD-MM-YYYY z tekstu 
# "Dzisiaj jest 20-10-2024, a jutro będzie 21-10-2024.")
# WSZYSTKIE - findAll
# jak wyglada findAll ? chatgpt albo rozwiazanie drugiego zadania :)

sentence = "Dzisiaj jest 20-10-2024, a jutro będzie 21-10-2024."
pattern = r"\b\d{2}-\d{2}-\d{4}\b"

result = re.findall(pattern, sentence)
print(result)

# regexr.com - cheatsheet  albo po prostu chatgpt do generowania regexow
