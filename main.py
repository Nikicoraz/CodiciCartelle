import os, shutil


def CreaCodiceCartelle(root, profondita):
    if profondita == 0:
        return
    
    for i in range(10):
        cartella = root + "\\" + str(i)
        os.mkdir(cartella)
        CreaCodiceCartelle(cartella, profondita - 1)
    

if __name__ == "__main__":
    cartella = os.getcwd() + "\\" + input("Inserisci la cartella da spostare (invio per lasciare vuoto): ")
    codice = input("Inserisci il codice (ogni numero corrisponde a un layer di profondità): ")
    
    cartellaCodice = os.getcwd() + "\\Combinazione"
    os.mkdir("Combinazione")
    CreaCodiceCartelle(cartellaCodice , len(codice))
    dst = cartellaCodice
    for i in range(len(codice)):
        dst += "\\" + codice[i]
    if(cartella != os.getcwd() + "\\"):
        shutil.copytree(cartella, dst + "\\" + cartella.split("\\")[-1])
    input("Premi invio per uscire")