catalogo = []
libriprestati = []

def aggiuntaLibro():
    titolo = input("Inserisci il nome del libro che vuoi inserire: ")
    catalogo.append(titolo)
    print("Il libro ", titolo," è stato aggiunto alla libreria.")
    

def prestitoLibro():
    titolo = input("Inserisci il titolo del libro che vuoi prendere in prestito: ")
    catalogo.remove(titolo)
    libriprestati.append(titolo)
    print("Il libro ", titolo, " è stato prestato.")
    
def riportaLibro():
    titolo = input("Inserisci il titolo del libro che vuoi riportare: ")
    catalogo.append(titolo)
    libriprestati.remove(titolo)
   
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