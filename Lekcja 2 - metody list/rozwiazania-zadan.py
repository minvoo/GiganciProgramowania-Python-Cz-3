### 1 
lista1 = [1,2,3]
lista2 = [4,50,6]
### 2 
lista1.extend(lista2)

### 3
# [1,2,3,4,5,6] < wartosci listy
# [0,1,2,3,4,5] <indeksy listy
lista1.pop(5)
# [1,2,4,5,6]
# [0,1,2,3,4] # zostaly 4 indeksy
lista1.pop(2)
print(lista1)

### 4
lista1.remove(min(lista1))
lista1.remove(max(lista1))


### 5
lista1.append(666)

### 6
lista1.sort()
print(lista1)

### 7
kopia = lista1.copy()

### 8
kopia.reverse()

### 9
lista1 = [1,2,3]
lista2 = [4,50,6]

for i in range(len(lista1)):
    lista1[i] = lista1[i]+1
#   lista1[i] += 1

for i in range(len(lista2)):
    #lista2[i] = lista2[i] - 1
    lista2[i] -= 1

### 10
print(lista1)
print(lista2)





zmienna = 1
zmienna = zmienna + 10 #11
zmienna += 10 # 21