from lab4Tema.domain.complex_number import modul_numar_complex, egale
from lab4Tema.domain.validation import validare_indice, validare_interval, validare_prim

def adauga_element(list, element, pozitie):
    '''
        Functia adauga numarul complex nou 'element' la o pozitia 'pozitie'
        in lista 'list'

        input: - list, lista cu numerele complexe
               - element, numar complex de forma a+bi, unde a si b numere reale
               - pozitie, pozitia din lista la care se vrea adaugarea numarului nou
        output: - 
                raises: Exception 
                        "pozitie invalida!\n" - daca pozitia ceruta este mai mare decat lungimea listei 

    '''

    if pozitie > len(list):
        raise Exception("pozitie invalida!\n")

    list.insert(pozitie, element)

def proprietate_parte_imaginara(complex_num):
    return True

def proprietate_modul_mai_mic_10(complex_num):
    '''
        Proprietate care verifica daca numarul complex 'complex_num'
        are modulul < 10

        input: complex_num: nr complex de forma a+bi, a, b numere reale
        output: True, daca modulul numarului 'complex_num' < 10
                False, altfel
    '''
    if modul_numar_complex(complex_num) < 10: return True
    return False

def proprietate_modul_egal_10(complex_num):
    '''
        Proprietate care verifica daca numarul complex 'complex_num' 
        are modulul = 10

        input: complex_num: nr complex de forma a+bi, a, b numere reale
        output: True, daca modulul numarului 'complex_num' - 10,
                False, altfel
    '''
    if abs(10 - modul_numar_complex(complex_num)) < 0.0001: return True
    return False

def cautare_numere(list, stanga, dreapta, proprietate):
    '''
        Functia genereaza o lista de numere complexe cu proprietatea 'proprietate'
        input: list - sir de numere complexe
               stanga - capatul stang al intervalului cautat
               dreapta - capatul drept al intervalului cautat
               proprietate - o caracteristica in functie de care se aleg numerele
        output: rezultat - sirul numerelor cu proprietatea ceruta din intervalul ['stanga','dreapta']
                raises: Exception "capat stanga invalid!\n" si/sau "capat dreapta invalid!\n" daca indicii intervalului
                        nu sunt valizi
    '''
    rezultat = []
    validare_interval(list, stanga, dreapta)
    for complex_num in list[stanga: dreapta+1]:
        if proprietate(complex_num): rezultat.append(complex_num)
    return rezultat

def calcul_numere_interval(list, stanga, dreapta, calcul):
    '''
        Functia se foloseste de functia 'calcul' pentru a calcula
        un rezultat din intervalul ['stanga', 'dreapta']

        input: list - lista cu numere complexe de forma a+bi, a, b reale
               stanga - numar intreg pozitiv, capatul stang al intervalului
               dreapta - numar intreg pozitiv, capatul drept al intervalului
               calcul - functie de calcul
    '''
    validare_interval(list, stanga, dreapta)
    rez = list[stanga]
    for number in list[stanga+1:dreapta+1]:
        rez = calcul(rez, number)
    return rez
    
def sortare_desc_img(list):
    '''
        Functia sorteaza descrescator lista 'list' formata din 
        numere complexe a+bi, a, b numere reale dupa partea imaginara

        input: list - lista cu numere complexe de forma a+bi, a, b reale
        output: sorted_list - lista sortata cu proprietatea ceruta
    '''

    sorted_list = list
    sortat = False
    #BubbleSort
    while not sortat:
        sortat = True
        for i in range(0, len(sorted_list)-1):
            if sorted_list[i].get_imaginar() < sorted_list[i+1].get_imaginar():
                aux = sorted_list[i]
                sorted_list[i] = sorted_list[i+1]
                sorted_list[i+1] = aux
                sortat = False
    return sorted_list


def stergere_element(list, poz):
    '''
        Functia sterge elementul de pe pozitia 'poz' din lista 'list'

        input: list - lista cu numere complexe de forma a+bi, a, b reale
               poz - pozitia de la care se vrea stergerea
        output: -
    '''
    validare_indice(list, poz)
    del list[poz]        
   
def stergere_interval(list, stanga, dreapta):
    '''
        Functia sterge toate elementele dintre pozitiile 'stanga' si 'dreapta'
        din lista 'list'

        input: list - lista cu numere complexe de forma a+bi, a, b reale
               stanga - capatul stang al intervalului care trebuie sters
               dreapta - capatul drept al intervalului care trebuie sters
               raises Exception:   "lista goala!\n" - daca lista nu contine niciun element
                                    "capat stanga invalid!\n" - daca 'stanga' < 0 sau 'stanga' > 'dreapta'
                                    "capat dreapta invalid!\n" - daca 'dreapta' < 'stanga' sau 'dreapta' > len(list)
    '''
    validare_interval(list, stanga, dreapta)
    while stanga <= dreapta:
        del list[dreapta]
        dreapta -= 1
    pass

def pozitii_element(list, numar):
    '''
        Functia gaseste toate pozitiile pe care se afla numarul 'numar'
        in lista 'list'

        input: list - lista cu numere complexe de forma a+bi, a, b reale
               numar - numar complex de forma a+bi, a, b reale
        output: pozitii - lista cu pozitiile pe care se afla numarul 'numar' in lista 'list'
    '''
    pozitii = []
    for i in range(0, len(list)):
        if egale(list[i], numar):
            pozitii.append(i)
    return pozitii


def modificare_elemente(list, numar, nou):
    '''
        Functia inlocuieste toate aparitiile numarului complex 'numar' din lista 'list'
        cu numarul complex 'nou'

        input: list - lista cu numere complexe de forma a+bi, a, b reale
               numar - numarul care se cauta pentru a fi inlocuit
               nou - numarul cu care se inlocuieste numarul 'numar'
        output: -
                raises Exception: "numarul nu are nicio aparitie!\n" - daca numarul 'numar' nu apare in 
                                    lista 'list'
    '''
    pozitii = pozitii_element(list, numar)
    if len(pozitii) == 0:
        raise Exception("numarul nu are nicio aparitie!\n")
    for poz in pozitii:
        list[poz] = nou

def filtrare_p_reala_prim(list):
    '''
        Functia filtreaza lista 'list' astfel incat se elimina
        toate numerele complexe pentru care partea reala este un numar 
        prim

        input: list - lista cu numere complexe de forma a+bi, a, b reale
        output: rez - lista filtrata
    '''

    rez = []

    for number in list:
        if validare_prim(number.get_real()) == False:
            rez.append(number)
    return rez

def filtrare_modul(list, numar, semn):
    '''
        Functia filtreaza lista 'list' astfel incat se elimina toate numerele
        complexe pentru care modului este <, = sau > decat un numar dat 'numar'

        input: list - lista cu numere complexe de forma a+bi, a, b reale
               numar - numarul fata de care se filtreaza lista
               semn - are valoarea '<', '=' sau '>'

    '''
    rez = []
    if semn == '<':
        for compl in list:
            if not(modul_numar_complex(compl) < numar): 
                rez.append(compl)
    elif semn == '=':
        for compl in list:
            if not(abs(modul_numar_complex(compl) - numar) < 0.00001): 
                rez.append(compl)
    elif semn == '>':
        for compl in list:
            if not(modul_numar_complex(compl) > numar): 
                rez.append(compl) 
    else: raise Exception("semn invalid!\n") 
    return rez

def copy_list(list):
    '''
        Functia returneaza o copie a listei 'list'

        input: list - lista de elemente
        output: rez - lista rezultata
    '''

    rez = []

    for element in list:
        rez.append(element)
    return rez
