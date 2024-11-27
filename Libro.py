from FunzioniLibro import*
scelta = 9

while scelta != 0:
    print("-----------------------------------------------------------------------")
    print("Benvenui in libreria")
    print("Digita 1 per aggiungere un nuovo libro in libreria")
    print("Digita 2 per effetuare un preestito")
    print("Digita 3 per riportare un libro")
    print("Digita 4 per vedere la disponibilità di un libro")
    print("Digita 5 per vedere tutti i libri disponibili nella libreria")
    print("Digita 6 per vedere i libri in prestito attualmente")
    print("Digita 0 per terminare il programma libreria")

    scelta = int(input("Inserire un numero per effettuare un operazione: "))

    if scelta == 1:
        aggiuntaLibro()

    elif scelta == 2:
        prestitoLibro()

    elif scelta == 3:
        riportaLibro()

    elif scelta == 4:
        disponibilitLibro()
    
    elif scelta == 5:
        disponibiliOra()

    elif scelta == 6:
        libriPrest()



print("Hai scelto di terminare il programma ")


