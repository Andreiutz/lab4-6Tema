from complex_number import ComplexNumber,produs,suma, modul_numar_complex, egale
from list_management import calcul_numere_interval, filtrare_modul, filtrare_p_reala_prim, modificare_elemente, pozitii_element, proprietate_parte_imaginara, adauga_element, cautare_numere, proprietate_modul_mai_mic_10, proprietate_modul_egal_10, sortare_desc_img, stergere_element, stergere_interval
from validation import validare_indice, validare_lista_semn, validare_interval, validare_prim
from service import srv_modificare_element, srv_stergere_interval, srv_stergere_element, srv_filtrare_modul, srv_filtrare_p_reala_prim, srv_sortare_desc_img, srv_adauga_numar, srv_calcul_numere_interval, srv_cauta_numere


def test_ComplexNumber():
    '''
        Functia verifica daca se creeaza corect obiectul
        de tip ComplexNumber

    '''
    number = ComplexNumber(12, 3.4)
    assert(number.get_imaginar() == 3.4)
    assert(number.get_real() == 12)

def test_modul_numar_complex():
    '''
        Functia testeaza daca functia modul_numar_complex
        calculeaza corect modulul unui nr complex
    '''
    number1 = ComplexNumber(3,4)
    number2 = ComplexNumber(0,3)
    assert(modul_numar_complex(number1) == 5)
    assert(modul_numar_complex(number2) == 3)

def test_adauga_element():
    '''
        Testeaza daca functia adauga_element adauga
        corect un element la o pozitie data in lista cu numere 
        complexe
    '''

    list = []
    number1 = ComplexNumber(22, 44)
    number2 = ComplexNumber(55, -1)
    number3 = ComplexNumber(0, -1)
    adauga_element(list, number1, 0)
    assert(len(list) == 1)
    assert(egale(list[0], number1))
    adauga_element(list, number2, 0)
    assert(len(list) == 2)
    assert(egale(list[0], number2))
    try:
        adauga_element(list, number3, 5)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "pozitie invalida!\n")

def test_validare_interval():
    '''
    Verifica daca functia validare_interval valideaza corect 
    capetele unui interval dintr-o lista 
    '''

    l = []
    try:
        validare_interval(l, 0, 0)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "lista goala!\ncapat dreapta invalid!\n")

    #    0 1 2 3 4 5 6 7 8 9    <- indicii listei 'l'
    l = [1,2,3,4,5,6,7,8,9,10]

    try:
        validare_interval(l, 1, 0)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "capat stanga invalid!\ncapat dreapta invalid!\n")

    try:
        validare_interval(l, -1, 5)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "capat stanga invalid!\n")

    try:
        validare_interval(l, 2, 15)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "capat dreapta invalid!\n")

def test_cautare_numere():
    '''
        Testare functie cautare_numere
    '''
    n0 = ComplexNumber(0, 0.5)
    n1 = ComplexNumber(6, 8)
    n2 = ComplexNumber(8, 6)
    n3 = ComplexNumber(4, 0)
    n4 = ComplexNumber(2, 2)

    list = [n0, n1, n2, n3, n4]

    assert(cautare_numere(list, 0, len(list)-1, proprietate_modul_mai_mic_10) == [n0, n3, n4])
    assert(cautare_numere(list, 0, len(list)-1, proprietate_modul_egal_10) == [n1, n2])
    assert(cautare_numere(list, 0, 2, proprietate_parte_imaginara) == [n0, n1, n2])

def test_srv_adauga_numar():
    '''
        Testare functie srv_adauga_numar
    '''
    list = []
    number1 = ComplexNumber(22, 44)
    number2 = ComplexNumber(55, -1)
    number3 = ComplexNumber(0, -1)
    srv_adauga_numar(list, number1, 0)
    assert(len(list) == 1)
    assert(egale(list[0], number1))
    srv_adauga_numar(list, number2, 0)
    assert(len(list) == 2)
    assert(egale(list[0], number2))
    try:
        srv_adauga_numar(list, number3, 5)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "pozitie invalida!\n")

def test_srv_cauta_numere():
    n0 = ComplexNumber(0, 0.5)
    n1 = ComplexNumber(6, 8)
    n2 = ComplexNumber(8, 6)
    n3 = ComplexNumber(4, 0)
    n4 = ComplexNumber(2, 2)

    list = [n0, n1, n2, n3, n4]

    assert(srv_cauta_numere(list, 0, len(list)-1, "modul < 10") == [n0, n3, n4])
    assert(srv_cauta_numere(list, 0, len(list)-1, "modul = 10") == [n1, n2])
    assert(srv_cauta_numere(list, 0, 2, "parte imaginara") == [n0, n1, n2])
    try:
        assert(srv_cauta_numere(list, 0, 2, "invalid") == [])
        assert(False)
    except Exception as ex:
        assert(str(ex) == "cerinta invalida!\n")

def test_suma():
    nr1 = ComplexNumber(5, 6)
    nr2 = ComplexNumber(3, 1)
    sum = suma(nr1, nr2)
    assert(sum.get_real() == 8)
    assert(sum.get_imaginar() == 7)

def test_produs():
    nr1 = ComplexNumber(5, 6)
    nr2 = ComplexNumber(3, 1)
    prod = produs(nr1, nr2)
    assert(prod.get_real() == 9)
    assert(prod.get_imaginar() == 23)

def test_calcul_numere_interval():
    n0 = ComplexNumber(1, 2)
    n1 = ComplexNumber(3, 2)
    n2 = ComplexNumber(1, 1)

    list = [n0, n1, n2]

    assert(egale(calcul_numere_interval(list, 0, 2, suma), ComplexNumber(5, 5)))
    assert(egale(calcul_numere_interval(list, 0, 1, produs), ComplexNumber(-1, 8)))
    try:
        calcul_numere_interval(list, -1, -2, suma)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "capat stanga invalid!\ncapat dreapta invalid!\n")

def test_srv_calcul_numere_interval():
    n0 = ComplexNumber(1, 2)
    n1 = ComplexNumber(3, 2)
    n2 = ComplexNumber(1, 1)

    list = [n0, n1, n2]

    assert(egale(srv_calcul_numere_interval(list, 0, 2, "suma"), ComplexNumber(5, 5)))
    assert(egale(srv_calcul_numere_interval(list, 0, 1, "produs"), ComplexNumber(-1, 8)))
    try:
        srv_calcul_numere_interval(list, -1, -2, "suma")
        assert(False)
    except Exception as ex:
        assert(str(ex) == "capat stanga invalid!\ncapat dreapta invalid!\n")
    try:
        srv_calcul_numere_interval(list, 0, 1, "invalid")
        assert(False)
    except Exception as ex:
        assert(str(ex) == "formula invalida!\n")

def test_sortare_desc_img():
    n0 = ComplexNumber(1,2)
    n1 = ComplexNumber(4,3)
    n2 = ComplexNumber(5,-4)
    n3 = ComplexNumber(9,10)
    n4 = ComplexNumber(0,0)
    n5 = ComplexNumber(3,7)

    list = [n0, n1, n2, n3, n4, n5]

    sorted_list = sortare_desc_img(list)

    assert (sorted_list == [n3, n5, n1, n0, n4, n2])

def test_srv_sortare_desc_img():
    n0 = ComplexNumber(1,2)
    n1 = ComplexNumber(4,3)
    n2 = ComplexNumber(5,-4)
    n3 = ComplexNumber(9,10)
    n4 = ComplexNumber(0,0)
    n5 = ComplexNumber(3,7)

    list = [n0, n1, n2, n3, n4, n5]

    sorted_list = srv_sortare_desc_img(list)

    assert (sorted_list == [n3, n5, n1, n0, n4, n2])

    list = []

    try:
        assert(srv_sortare_desc_img(list) == [])
        assert(False)
    except Exception as ex:
        assert(str(ex) == "lista vida!\n")

def test_validare_prim():
    assert(validare_prim(2) == True)
    assert(validare_prim(-1) == False)
    assert(validare_prim(3.4) == False)
    assert(validare_prim(7) == True)
    assert(validare_prim(9) == False)
    assert(validare_prim(101) == True)
    assert(validare_prim(17) == True)
    assert(validare_prim(25) == False)
    assert(validare_prim(2.02) == False)

def test_filtrare_p_reala_prim():
    n0 = ComplexNumber(1, 4)
    n1 = ComplexNumber(2, 6)
    n2 = ComplexNumber(7, -2)
    n3 = ComplexNumber(2.01, 6)
    n4 = ComplexNumber(10, -3)
    n5 = ComplexNumber(7, 4)

    list = [n0, n1, n2, n3, n4, n5]

    assert(filtrare_p_reala_prim(list) == [n0, n3, n4])

def test_srv_filtrare_p_reala_prim():
    n0 = ComplexNumber(1, 4)
    n1 = ComplexNumber(2, 6)
    n2 = ComplexNumber(7, -2)
    n3 = ComplexNumber(2.01, 6)
    n4 = ComplexNumber(10, -3)
    n5 = ComplexNumber(7, 4)

    list = [n0, n1, n2, n3, n4, n5]

    assert(srv_filtrare_p_reala_prim(list) == [n0, n3, n4])

    list = []

    try:
        srv_filtrare_p_reala_prim(list)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "lista vida!\n")

def test_filtrare_modul():
    n0 = ComplexNumber(1, 4)
    n1 = ComplexNumber(2, -19)
    n2 = ComplexNumber(7, -2)
    n3 = ComplexNumber(8, 6)
    n4 = ComplexNumber(10, 0)
    n5 = ComplexNumber(11, 4)

    list = [n0, n1, n2, n3, n4, n5]

    assert(filtrare_modul(list, 10, '<') == [n1,n3,n4,n5])
    assert(filtrare_modul(list, 10, '=') == [n0, n1, n2, n5])
    assert(filtrare_modul(list, 10, '>') == [n0, n2, n3, n4])
    assert(filtrare_modul(list, -1, '>') == [])

def test_srv_filtrare_modul():
    n0 = ComplexNumber(1, 4)
    n1 = ComplexNumber(2, -19)
    n2 = ComplexNumber(7, -2)
    n3 = ComplexNumber(8, 6)
    n4 = ComplexNumber(10, 0)
    n5 = ComplexNumber(11, 4)

    list = [n0, n1, n2, n3, n4, n5]

    assert(srv_filtrare_modul(list, 10, '<') == [n1,n3,n4,n5])
    assert(srv_filtrare_modul(list, 10, '=') == [n0, n1, n2, n5])
    assert(srv_filtrare_modul(list, 10, '>') == [n0, n2, n3, n4])
    assert(srv_filtrare_modul(list, -1, '>') == [])
    try:
        srv_filtrare_modul(list, -1, "garbage")
        assert(False)
    except Exception as ex:
        assert(str(ex) == "semn invalid!\n")
    
    list = []

    try:
        srv_filtrare_modul(list, -1, '<')
        assert(False)
    except Exception as ex:
        assert(str(ex) == "lista vida!\n")

    try:
        srv_filtrare_modul(list, -1, "garbage")
        assert(False)
    except Exception as ex:
        assert(str(ex) == "lista vida!\nsemn invalid!\n")

def test_validare_lista_semn():
    list = []
    try: 
        validare_lista_semn(list, '<')
        assert(False)
    except Exception as ex:
        assert(str(ex) == "lista vida!\n")

    try:
        validare_lista_semn(list, "garbage")
        assert(False)
    except Exception as ex:
        assert(str(ex) == "lista vida!\nsemn invalid!\n")

    list = [1]

    try:
        validare_lista_semn(list, "garbage")
        assert(False)
    except Exception as ex:
        assert(str(ex) == "semn invalid!\n")

def test_validare_indice():
    try:
        assert(validare_indice([], 0))
        assert(False)
    except Exception as ex:
        assert(str(ex) == "indice invalid\n")

    try:
        assert(validare_indice([1,2], -1))
        assert(False)
    except Exception as ex:
        assert(str(ex) == "indice invalid\n")    

    try:
        assert(validare_indice([1,2,3], 4))
        assert(False)
    except Exception as ex:
        assert(str(ex) == "indice invalid\n")   

def test_stergere_element():
    n0 = ComplexNumber(1, 4)
    n1 = ComplexNumber(2, -19)
    n2 = ComplexNumber(7, -2)
    n3 = ComplexNumber(8, 6)
    n4 = ComplexNumber(10, 0)
    n5 = ComplexNumber(11, 4)

    list = [n0, n1, n2, n3, n4, n5]

    stergere_element(list, 0)
    assert(list == [n1, n2, n3, n4, n5])

    stergere_element(list, 3)
    assert(list == [n1, n2, n3, n5])

    try:
        stergere_element(list, -1)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "indice invalid\n")
    
    try:
        stergere_element(list, 10)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "indice invalid\n")

def test_srv_stergere_element():
    n0 = ComplexNumber(1, 4)
    n1 = ComplexNumber(2, -19)
    n2 = ComplexNumber(7, -2)
    n3 = ComplexNumber(8, 6)
    n4 = ComplexNumber(10, 0)
    n5 = ComplexNumber(11, 4)

    list = [n0, n1, n2, n3, n4, n5]

    srv_stergere_element(list, 0)
    assert(list == [n1, n2, n3, n4, n5])

    srv_stergere_element(list, 3)
    assert(list == [n1, n2, n3, n5])

    try:
        srv_stergere_element(list, -1)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "indice invalid\n")
    
    try:
        srv_stergere_element(list, 10)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "indice invalid\n")

def test_stergere_interval():
    n0 = ComplexNumber(1, 4)
    n1 = ComplexNumber(2, -19)
    n2 = ComplexNumber(7, -2)
    n3 = ComplexNumber(8, 6)
    n4 = ComplexNumber(10, 0)
    n5 = ComplexNumber(11, 4)
    n6 = ComplexNumber(10, 11)
    n7 = ComplexNumber(-1, -4)

    list = [n0, n1, n2, n3, n4, n5, n6, n7]

    stergere_interval(list, 0, 0)
    assert(list == [n1, n2, n3, n4, n5, n6, n7])
    stergere_interval(list, 1, 3)
    assert(list == [n1, n5, n6, n7])
    
    try:
        stergere_interval(list, 1, 10)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "capat dreapta invalid!\n")
    
    try:
        stergere_interval(list, -1, 3)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "capat stanga invalid!\n")

    try:
        stergere_interval(list, -2, -3)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "capat stanga invalid!\ncapat dreapta invalid!\n")

    stergere_interval(list, 0, 3)
    assert(list == [])

    try:
        stergere_interval(list, -2, 0)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "lista goala!\ncapat stanga invalid!\ncapat dreapta invalid!\n")

def test_srv_stergere_interval():
    n0 = ComplexNumber(1, 4)
    n1 = ComplexNumber(2, -19)
    n2 = ComplexNumber(7, -2)
    n3 = ComplexNumber(8, 6)
    n4 = ComplexNumber(10, 0)
    n5 = ComplexNumber(11, 4)
    n6 = ComplexNumber(10, 11)
    n7 = ComplexNumber(-1, -4)

    list = [n0, n1, n2, n3, n4, n5, n6, n7]

    srv_stergere_interval(list, 0, 0)
    assert(list == [n1, n2, n3, n4, n5, n6, n7])
    stergere_interval(list, 1, 3)
    assert(list == [n1, n5, n6, n7])
    
    try:
        srv_stergere_interval(list, 1, 10)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "capat dreapta invalid!\n")
    
    try:
        srv_stergere_interval(list, -1, 3)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "capat stanga invalid!\n")

    try:
        srv_stergere_interval(list, -2, -3)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "capat stanga invalid!\ncapat dreapta invalid!\n")

    srv_stergere_interval(list, 0, 3)
    assert(list == [])

    try:
        srv_stergere_interval(list, -2, 0)
        assert(False)
    except Exception as ex:
        assert(str(ex) == "lista goala!\ncapat stanga invalid!\ncapat dreapta invalid!\n")

def test_pozitii_element():
    n0 = ComplexNumber(0,0)
    n1 = ComplexNumber(1,1)
    n2 = ComplexNumber(0,0)
    n3 = ComplexNumber(2,2)
    n4 = ComplexNumber(0,0)
    n5 = ComplexNumber(3,3)
    n6 = ComplexNumber(3,3)
    n7 = ComplexNumber(4,4)
    n8 = ComplexNumber(0,0)

    list = [n0, n1, n2, n3, n4, n5, n6, n7, n8]

    assert(pozitii_element(list, ComplexNumber(0,0)) == [0,2,4,8])
    assert(pozitii_element(list, ComplexNumber(1,1)) == [1])
    assert(pozitii_element(list, ComplexNumber(3,3)) == [5,6])
    assert(pozitii_element(list, ComplexNumber(1,2)) == [])

def test_modificare_elemente():
    n0 = ComplexNumber(0,0)
    n1 = ComplexNumber(1,1)
    n2 = ComplexNumber(0,0)
    n3 = ComplexNumber(2,2)
    n4 = ComplexNumber(0,0)
    n5 = ComplexNumber(3,3)
    n6 = ComplexNumber(3,3)
    n7 = ComplexNumber(4,4)
    n8 = ComplexNumber(0,0)

    list = [n0, n1, n2, n3, n4, n5, n6, n7, n8]

    nm1 = ComplexNumber(-1, -1)
    nm2 = ComplexNumber(-2, -2)

    modificare_elemente(list, n0, nm1)
    assert(list == [nm1, n1, nm1, n3, nm1, n5, n6, n7, nm1])
    modificare_elemente(list, n3, nm2)
    assert(list == [nm1, n1, nm1, nm2, nm1, n5, n6, n7, nm1])

    try:
        modificare_elemente(list, ComplexNumber(-100, -100), ComplexNumber(0,0))
        assert(False)
    except Exception as ex:
        assert(str(ex) == "numarul nu are nicio aparitie!\n")

def test_srv_modificare_interval():
    n0 = ComplexNumber(0,0)
    n1 = ComplexNumber(1,1)
    n2 = ComplexNumber(0,0)
    n3 = ComplexNumber(2,2)
    n4 = ComplexNumber(0,0)
    n5 = ComplexNumber(3,3)
    n6 = ComplexNumber(3,3)
    n7 = ComplexNumber(4,4)
    n8 = ComplexNumber(0,0)

    list = [n0, n1, n2, n3, n4, n5, n6, n7, n8]

    nm1 = ComplexNumber(-1, -1)
    nm2 = ComplexNumber(-2, -2)

    srv_modificare_element(list, n0, nm1)
    assert(list == [nm1, n1, nm1, n3, nm1, n5, n6, n7, nm1])
    srv_modificare_element(list, n3, nm2)
    assert(list == [nm1, n1, nm1, nm2, nm1, n5, n6, n7, nm1])

    try:
        srv_modificare_element(list, ComplexNumber(-100, -100), ComplexNumber(0,0))
        assert(False)
    except Exception as ex:
        assert(str(ex) == "numarul nu are nicio aparitie!\n")


def run_tests():
    '''
    Functia apeleaza toate celelalte functii care
    se ocupa de testarea functionalitatilor
    programului
    '''
    test_ComplexNumber()
    test_modul_numar_complex()
    test_adauga_element()
    test_validare_interval()
    test_cautare_numere()
    test_srv_adauga_numar()
    test_srv_cauta_numere()
    test_suma()
    test_produs()
    test_calcul_numere_interval()
    test_srv_calcul_numere_interval()
    test_sortare_desc_img()
    test_srv_sortare_desc_img()
    test_validare_prim()
    test_filtrare_p_reala_prim()
    test_srv_filtrare_p_reala_prim()
    test_filtrare_modul()
    test_srv_filtrare_modul()
    test_validare_lista_semn()
    test_validare_indice()
    test_stergere_element()
    test_srv_stergere_element()
    test_stergere_interval()
    test_srv_stergere_interval()
    test_pozitii_element()
    test_modificare_elemente()
    test_srv_modificare_interval()