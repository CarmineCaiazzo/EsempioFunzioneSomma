#Programma che calcola la somma grazie a una funzione.
#Funzione.

def Benvenuto():
    print ('Ciao! Il mio nome e Carmine')
    print ('E questo e un esercizio su come creare le funzioni!!')
    print ('In questo esercizio vedremo come si fa per stampare una somma grazie alla funzione!!')
    print ('------------------------------------------------------------------------------------')

def somma (a,b):
    return a + b


#Main
Benvenuto()
a = input ("Inserisci Numero 1: ")
a = int (a)
b = input ("Inserisci Numero 2: ")
b = int (b)

S1 = somma (a,b)
S2 = somma (7,10)
print (S1)
print (S2)

#in alternativa abbiamo come metodo per stampare la Funzione:
#somma (a,b)
#print (somma(a,b))

print (S1 * S2)
