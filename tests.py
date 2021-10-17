from complex_number import ComplexNumber, modul_numar_complex, egale
from list_management import  proprietate_parte_imaginara, adauga_element, cautare_numere, proprietate_modul_mai_mic_10, proprietate_modul_egal_10
from validation import validare_interval
from service import srv_adauga_numar, srv_cauta_numere


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
    

