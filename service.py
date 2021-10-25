from complex_number import ComplexNumber, suma, produs
from list_management import calcul_numere_interval, filtrare_modul, filtrare_p_reala_prim, modificare_elemente, proprietate_modul_egal_10, proprietate_modul_mai_mic_10, proprietate_parte_imaginara ,adauga_element, cautare_numere, sortare_desc_img, stergere_element, stergere_interval
from validation import validare_interval, validare_lista_semn

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

def srv_filtrare_p_reala_prim(list):
    '''
        Comunicare dintre ui si program. Functia primeste din ui lista de numere complexe
        si elimina din aceasta numerele care au partea reala un numar prim

        input: list - lista cu numere complexe de forma a+bi, a, b reale
        output: rez - lista sortata
                raises Exception: "lista vida!\n" daca lista 'list' nu contine elemente
    '''
    if len(list) == 0:
        raise Exception("lista vida!\n")
    filter_list = filtrare_p_reala_prim(list)
    return filter_list
    
def srv_filtrare_modul(list, numar, semn):
    '''
        Comunicare dintre ui si program. Functia filtreaza lista 'list'
        astfel incat sa ramana doar numerele care au modului <, =, > decat
        modulul numarului 'numar'

        input: list - lista cu numere complexe de forma a+bi, a, b reale
               numar - numarul real fata de care se raporteaza modulul
               semn - conditia de comparatie ('<', '=' sau '>')
               raises Exception: "lista vida!\n" daca lista este vida
                                 "semn invalid!\n" daca semnul nu are una dintre valorile {'<', '=', '>'}
    '''
    validare_lista_semn(list, semn)
    rez = filtrare_modul(list, numar, semn)
    return rez

def srv_stergere_element(list, indice):
    '''
        Comunicare dintre ui si program. Functia primeste indicele intreg 'indice'
        si sterge elementul din lista 'list' de la acea pozitie
    
        input: list - lista cu numere complexe a+bi, a, b reale
               indice - numar intreg >= 0 si mai mic decat lungimea listei
        output: - 
                raises Exception: ("indice invalid\n") daca indicele e 
                invalid
    '''
    stergere_element(list, indice)
    
def srv_stergere_interval(list, stanga, dreapta):
    '''
        Comunicare dintre ui si program. Functia primeste indicii indicii intregi 'stanga' si
        'dreapta' si sterge toate elementele din lista 'list' ce se gasesc in intervalul
        ['stanga', 'dreapta']

        input: list - lista cu numere complexe a+bi, a, b reale
               stanga - capatul stang al intervalului care trebuie sters
               dreapta - capatul drept al intervalului care trebuie sters
        output: -
                raises Exception:   "lista goala!\n" - daca lista nu contine niciun element
                                    "capat stanga invalid!\n" - daca 'stanga' < 0 sau 'stanga' > 'dreapta'
                                    "capat dreapta invalid!\n" - daca 'dreapta' < 'stanga' sau 'dreapta' > len(list)
    '''
    stergere_interval(list, stanga, dreapta)
    pass

def srv_modificare_element(list, numar, nou):
    '''
        Comunicare dintre ui si program. Functia inlocuieste toate aparitiile numarului 'numar'
        cu numarul 'nou' in lista 'list'

        input: list - lista cu numere complexe de forma a+bi, a, b reale
               numar - numarul care se cauta pentru a fi inlocuit
               nou - numarul cu care se inlocuieste numarul 'numar'
        output: -
                raises Exception: "numarul nu are nicio aparitie!\n" - daca numarul 'numar' nu apare in 
                                    lista 'list'
    '''
    modificare_elemente(list, numar, nou)
    pass