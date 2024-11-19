import re

'''
#2 Znajdź wszystkie daty w zdaniu "Juliusz Słowacki herbu Leliwa
(ur. 4 września 1809 w Krzemieńcu, zm. 3 kwietnia 1849 w
Paryżu[1]) – polski poeta, dramaturg i epistolograf. Obok Adama
Mickiewicza i Zygmunta Krasińskiego określany jako jeden z
polskich wieszczów narodowych. Twórca filozofii genezyjskiej
(pneumatycznej), epizodycznie związany z mesjanizmem polskim, był
też mistykiem. Obok Adama Mickiewicza uznawany powszechnie za
największego przedstawiciela polskiego romantyzmu."
'''


sentence = """Juliusz Słowacki herbu Leliwa (ur. 4 września 1809 w Krzemieńcu, 
zm. 3 kwietnia 1849 w Paryżu[1]) – polski poeta, dramaturg i epistolograf. 
Obok Adama Mickiewicza i Zygmunta Krasińskiego określany jako jeden z polskich 
wieszczów narodowych. Twórca filozofii genezyjskiej (pneumatycznej), 
epizodycznie związany z mesjanizmem polskim, był też mistykiem. 
Obok Adama Mickiewicza uznawany powszechnie za największego przedstawiciela 
polskiego romantyzmu."""

pattern = r"\d+\s\w+\s\d{4}"  # pastebin.com/nc89i0bK
result = re.findall(pattern, sentence)
print(result)

#3. zamien wszystkie daty z tekstu wyzej na tekst "2137"
replecament = "2137"
nowy_tekst = re.sub(pattern, replecament, sentence)
print(nowy_tekst)

