from complex_number import ComplexNumber, suma, modul_numar_complex
from validation import validare_interval



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
        if (proprietate(complex_num)): rezultat.append(complex_num)
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