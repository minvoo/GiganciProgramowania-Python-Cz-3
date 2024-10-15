### WYJATKI  ### 

#try:
    #fragment kodu ktory ma byc sprawdzany pod wzgledem bledow
#pass
#except Exception as e: 
    #kod ktory ma sie wykonac w przypdku bledu programu - czyli kiedy program rzuci wyjatek
#pass
#else:
    #kod wykonywany jesli nie zgloszono zadnego wyjatku
#pass
#finally: 
    # kod wykonywany zawsze, niezaleznie czy wyjatek wystapi czy nie 
#pass

### Cwiczenia ###
# napisz funkcje dzielenie_i_mnozenie przyjmujaca dwa argumenty: a oraz b.
# funkcja ma wyswietlic wynik dzialania a/b    i      a*b
# W przypadku bledu wyswietl napis "Blad!: " i komunikat bledu.

def dzielenie_i_mnozenie(a,b):
    try:
        #fragment kodu ktory ma byc sprawdzany pod wzgledem bledow
        a/b
    except ZeroDivisionError as cokolwiek: 
        print(f'Nie dzielimy przez 0!!!!')
    except Exception as cokolwiek:
        print('Blad!!!!')
    else:
        print(f'Wynik dzielnia to {a/b}')
    finally:
        print(f'Wynik mnozenia to {a*b}')

dzielenie_i_mnozenie(1,2)
dzielenie_i_mnozenie(21,"3")
dzielenie_i_mnozenie(5,0)
dzielenie_i_mnozenie(2,1)

