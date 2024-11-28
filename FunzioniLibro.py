catalogo = []
libriprestati = []

def aggiuntaLibro():
    titolo = input("Inserisci il nome del libro che vuoi inserire: ")
    if titolo in catalogo:
        print ("Il libro è già presente nel catalogo")
    elif titolo in libriprestati:
        print("Il libro è già presente nel nostro catalogo e al momento è in prestito")
    else:        
        catalogo.append(titolo)
        print("Il libro ", titolo," è stato aggiunto alla libreria.")
    

def prestitoLibro():
    titolo = input("Inserisci il titolo del libro che vuoi prendere in prestito: ")
   
    if titolo in libriprestati:
        print("Il libro è stato già prestato")
    elif titolo in catalogo:
        catalogo.remove(titolo)
        libriprestati.append(titolo)
        print("Il libro ", titolo, " è stato prestato.")

    
def riportaLibro():
    titolo = input("Inserisci il titolo del libro che vuoi riportare: ")
    if titolo in catalogo:
        print("Il libro non è stato prestato")
    elif titolo in libriprestati:
        catalogo.append(titolo)
        libriprestati.remove(titolo)
        print("Il libro è stato riportato")
    else:
        print("Il libro non è presente nel nostro catalogo e non è stato prestato")
   
def disponibilitLibro():
    titolo = input("Inserisci il titolo del libro che che cerchi: ")
    if titolo in catalogo:
        print("Il libro è disponibile")
    elif titolo in libriprestati:
        print("Il libro attualmente è in prestito ad un altra persona :( , riprova più tardi)")
    else:
        print("Non abbiamo questo libro nella nostra libreria")

def disponibiliOra():
    print(catalogo)

def libriPrest():
    print(libriprestati)
