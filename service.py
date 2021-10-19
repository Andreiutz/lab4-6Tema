from complex_number import ComplexNumber, suma, produs
from list_management import calcul_numere_interval, proprietate_modul_egal_10, proprietate_modul_mai_mic_10, proprietate_parte_imaginara ,adauga_element, cautare_numere, sortare_desc_img
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
                        Exception "cerinta invalida!\n" daca proprietatea 'proprietate' primita din ui este invalida
    '''
    if proprietate == "parte imaginara":
        prp = proprietate_parte_imaginara
    elif proprietate == "modul < 10":
        prp = proprietate_modul_mai_mic_10
    elif proprietate == "modul = 10":
        prp = proprietate_modul_egal_10
    else: raise Exception("cerinta invalida!\n")
    secventa = cautare_numere(list, stanga, dreapta, prp)
    return secventa

def srv_calcul_numere_interval(list, stanga, dreapta, calcul):
    '''
        Comunicare dintre ui si program. Functia primeste 2 indici, 'stanga' si 'dreapta'
        Valideaza acesti indici si executa operatiile corespunzatoare pe intervalul 
        ['stanga', 'dreapta']

        input: list - sir de numere complexe de forma a+bi, a, b reale
               stanga - indicele stang al intervalului
               dreapta - indicele drept al intervalului
               calcul - operatia care trebuie aplicata sirului. Poate fi 'suma'/'produs'
        output: rezultat - numar complex de forma a+bi, a, b reale
                raises Exception: "capat stanga invalid!\n" si/sau "capat dreapta invalid!\n" daca indicii intervalului
                                    nu sunt valizi
                                  "formula invalida!\n" daca parametrul 'calcul' nu are valoarea 'suma'
                                    sau 'produs'
    '''
    if calcul == "suma":
        clc = suma
    elif calcul == "produs":
        clc = produs
    else:
        raise Exception("formula invalida!\n")
    rezultat = calcul_numere_interval(list, stanga, dreapta, clc)
    return rezultat

def srv_sortare_desc_img(list):
    '''
        Comunicare dintre ui si program. Functia primeste din ui lista de numere complexe 
        si o returneaza sortata dupa proprietatea ceruta

        input: list - lista cu numere complexe de forma a+bi, a, b reale
        output: sorted_list - lista sortata 
                raises Exception: "lista vida!\n" daca lista 'list' nu contine elemente
    '''

    if len(list) == 0:
        raise Exception("lista vida!\n")
    sorted_list = sortare_desc_img(list)
    return sorted_list

    pass