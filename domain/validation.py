def validare_interval(list, stanga, dreapta):
    '''
        Functia valideaza indicii 'stanga' si 'dreapta' pentru o lista 'list'

        input: list - lista de numere complexe
               stanga - numar intreg pozitiv, reprezinta capatul din stanga al intervalului
               dreapta - numar intreg pozitiv, reprezinta capatul din dreapta al intervalului
        output: -
                raises Exception:   "lista goala!\n" - daca lista nu contine niciun element
                                    "capat stanga invalid!\n" - daca 'stanga' < 0 sau 'stanga' > 'dreapta'
                                    "capat dreapta invalid!\n" - daca 'dreapta' < 'stanga' sau 'dreapta' > len(list)
    '''
    ex = ""
    if len(list) == 0:
        ex += "lista goala!\n"
    if stanga < 0 or stanga > dreapta:
        ex += "capat stanga invalid!\n"
    if dreapta > len(list)-1 or dreapta < stanga:
        ex += "capat dreapta invalid!\n"
    
    if len(ex) > 0:
        raise Exception(ex)

def validare_prim(number):
    '''
        Functia verifica daca numarul 'number' este prim

        input: number - numarul dat
        output: True - daca numarul este prim
                False- altfel
    '''

    intreg = int(number)
    if (abs(intreg - number) > 0.000001): return False #numarul dat nu este intreg
    if intreg < 2 or intreg > 2 and intreg % 2 == 0: return False
    d = 3
    while d*d <= intreg:
        if intreg % d == 0: return False
        d += 2
    return True

def validare_lista_semn(list, semn):
    '''
        Functia verifica daca lista 'list' contine elemente
        si daca 'semn' apartine de {'<', '=', '>'}

        input: list - lista cu elemente numere complexe de forma a+bi, a, b reale
               semn - {'<', '=', '>'}
        output: -
                raises Exception: "lista vida!\n" - daca lista este goala
                                  "semn invalid!\n" - daca semnul e invalid

    
    '''
    err = ""
    if len(list) == 0:
        err += "lista vida!\n"
    if not semn in ['<', '=', '>']:
        err += "semn invalid!\n"

    if len(err) > 0:
        raise Exception(err)

def validare_indice(list, indice):
    '''
        Functia verifica daca indicele 'indice' este valid pentru
        lista 'list'

        input: list - lista cu numere complexe a+bi, a, b reale
        output: -
                raises Exception: "indice invalid\n" - daca indicele 'indice'
                nu se incadreaza listei 'list'
    '''
    if indice < 0 or indice > len(list)-1:
        raise Exception("indice invalid\n")