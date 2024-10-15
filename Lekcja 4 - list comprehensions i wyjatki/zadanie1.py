#Na podstawie podanej listy slowa = ["ala", "kot", "pies", "kamilslimak",
#"zebra", "madam", "Adam"] stwórz listę zawierającą same palindromy
#(wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do
#lewej).

slowa = ["ala", "kot", "pies", "kamilslimak","zebra", "madam", "Adam"]

# podpowiedz - jak sprawdzic czy cos jest palindromem w prosty sposob?    warunek  slowo[::-1]
palindromy = [slowo for slowo in slowa if slowo[::-1]]
print(palindromy)


# Na podstawie listy krotek zawierającej długości boków trójkąta  ##### 
# stwórz listę
#zawierającą tylko krotki z których można skonstruować trójkąt (warunek: 2*max(trojkat) < sum(trojkat)
#najdłuższy bok musi być krótszy niż suma dwóch pozostałych).
trojkaty = [(1,3,5), (2,2,3), (3,1,8), (3,4,5)]
#poprawne = []
#for trojkat in trojkaty: # for item in iterable
#    if (2*max(trojkat) < sum(trojkat)): #condition
#        # expression

poprawne_trojkaty = [trojkat for trojkat in trojkaty if 2*max(trojkat) < sum(trojkat)]

print(poprawne_trojkaty)