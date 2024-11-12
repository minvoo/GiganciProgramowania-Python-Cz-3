import re

#1 Sprawdz czy w tekscie "Uczę się programowania w języku python3"
#występuje cyfra

sentence = "Ucze sie programowania w jezyku python"
pattern = r"\d+"

result = re.search(pattern, sentence)
if result is not None:
    print(f'W zdaniu {sentence} wystepuje cyfra')
else:
    print(f'W zdaniu {sentence} nie wystepuje cyfra')

