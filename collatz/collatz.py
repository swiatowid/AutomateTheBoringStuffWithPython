# Collatz!

print('Wpisz jakąś liczbę')

#Sprawdza, czy podna wartość faktycznie jest liczbą
while True:
    try:
        number = int(input())
        break
    except ValueError:
        print('Nalegam na liczbę...') 
        continue   

#Funkcja oblicza kolejne działania dla podanej liczby modyfikując GLOBALNĄ zmienną
def collatz(n):
    global number
    if n % 2 == 0:
        print(n // 2)
        number = n // 2
        return n // 2

    else: 
        print(n * 3 + 1)
        number = n * 3 + 1
        return n * 3 + 1

#Wyowałanie funkcji
while collatz(number) != 1:
    collatz(number)