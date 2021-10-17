from complex_number import ComplexNumber
from list_management import proprietate_modul_egal_10, proprietate_modul_mai_mic_10, proprietate_parte_imaginara ,adauga_element, cautare_numere
from validation import validare_interval

def srv_adauga_numar(list, number, poz):
    '''
        Comunicare dintre ui si program. Adauga numarul 'number'

        input: list - sir de numere complexe
               number - numarul complex de forma a+bi, a, b numere reale
               poz - pozitia la care se insereaza elementul 'number'
        output: -
                raises Exception: "pozitie invalida!\n" - daca pozitia introdusa este invalida
    '''
    adauga_element(list, number, poz)

def srv_cauta_numere(list, stanga, dreapta, proprietate):
    '''
        Comunicare dintre ui si program. Functia genereaza o lista de numere cu o anumita proprietate
        si o returneaza

        input: list - sir de numere complexe
               stanga - capatul stang al intervalului cautat
               dreapta - capatul drept al intervalului cautat
               proprietate - o caracteristica in functie de care se aleg numerele
        output: rezultat - sirul numerelor cu proprietatea ceruta din intervalul ['stanga','dreapta']
                raises: Exception "capat stanga invalid!\n" si/sau "capat dreapta invalid!\n" daca indicii intervalului
                        nu sunt valizi
    '''
    if proprietate == "parte imaginara":
        prp = proprietate_parte_imaginara
    if proprietate == "modul < 10":
        prp = proprietate_modul_mai_mic_10
    if proprietate == "modul = 10":
        prp = proprietate_modul_egal_10
    secventa = cautare_numere(list, stanga, dreapta, prp)
    return secventa