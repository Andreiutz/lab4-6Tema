from complex_number import ComplexNumber
import service


def ui_optiuni_meniu_principal():
    print("")
    print("---Meniu Principal---")
    print("1) 'adauga_numar'    - pentru adaugarea unui numar nou")
    print("2) 'modifica_lista'  - pentru modificarea listei de elemente")
    print("3) 'cautare_numere'  - pentru cautarea unor numere din lista")
    print("4) 'operatii_lista'  - pentru efectuarea unor operatii pe numerele din lista")
    print("5) 'filtrare_lista'  - pentru filtrarea listei")
    print("6) 'undo'            - pentru refacerea ultima operatie")
    print("7) 'afisare_lista'   - pentru afisarea listei")
    print("8) 'exit'            - pentru iesire program")
    print("")

def ui_optiuni_adauga(): #1
    #afisare in meniu
    print("")
    print("1) 'pozitie' - pentru adaugarea numarului la o pozitie data")
    print("2) 'capat'   - pentru adaugarea numarului la capatul listei")
    print("")

def ui_optiuni_modificare(): #2
    #afisare in meniu
    pass

def ui_optiuni_cautare(): #3
    #afisare in meniu
    print("")
    print("1) 'parte_imaginara  -  pentru afisarea partii imaginare a tuturor numerelor din lista'")
    print("2) 'modul_m10'       - pentru afisarea numerelor cu modului < 10")
    print("3) 'modul_10         - pentru afisarea numerelor cu modului = 10")
    print("")

def ui_optiuni_operatii(): #4
    #afisare in meniu
    print("")
    print("1) 'suma'        - pentru calcularea sumei dintr-un interval")
    print("2) 'produs'      - pentru calcularea produsului dintr-un interval")
    print("3) 'sort_desc_im'- pentru afisarea listei ordonata desc. dupa partea imaginara")
    print("")

def ui_optiuni_filtrare(): #5
    #afisare in meniu
    pass

def ui_optiuni_undo(): #6
    #afisare in meniu
    pass

def ui_citire_indici():
    try:
        stanga = int(input("capat stanga: "))
    except ValueError:
        raise Exception("indice invalid!")
    try: 
        dreapta = int(input("capat dreapta: "))
    except ValueError:
        raise Exception("indice invalid!")
    l = [stanga, dreapta]
    return l

def ui_adauga_numar(list):
    try:
        real = float(input("parte reala = "))
    except ValueError:
        print("Parte reala invalida")
        return 

    try:
        imaginar = float(input("parte imaginara = "))
    except ValueError:
        print("Parte imaginara invalida\n")
        return

    numar = ComplexNumber(real, imaginar)
    ui_optiuni_adauga()
    pozitie = input(">>>")
    if pozitie == "pozitie":
        try:
            poz = int(input("dati pozitia: "))
        except ValueError:
            print("pozitie invalida!\n")
            return
        service.srv_adauga_numar(list, numar, poz)
    elif pozitie == "capat":
        service.srv_adauga_numar(list, numar, len(list))
    else: 
        print("valoare invalida\n")
        return

def ui_afisare_lista(lista):
    rez = ""
    for number in lista:
        rez += number.to_string() + " "
    print(rez)
    
def ui_afisare_lista_real(lista):
    rez = []
    for number in lista:
        rez.append(number.get_real())
    print(rez)

def ui_afisare_lista_imaginar(lista):
    rez = []
    for number in lista:
        rez.append(number.get_imaginar())
    print(rez)

def ui_cautare_numere(list):
    ui_optiuni_cautare()
    cmd = input(">>>")
    if cmd == "parte_imaginara":
        try:
            stanga, dreapta = ui_citire_indici()
        except Exception as ex:
            print(ex)
            return  
        try:
            secventa = service.srv_cauta_numere(list, stanga, dreapta, "parte imaginara")
        except Exception as ex:
            print(ex)
            return 
        ui_afisare_lista_imaginar(secventa)
    if cmd == "modul_m10":
        secventa = service.srv_cauta_numere(list, 0, len(list)-1, "modul < 10")
        ui_afisare_lista(secventa)
    if cmd == "modul_10":
        secventa = service.srv_cauta_numere(list, 0, len(list)-1, "modul = 10")
        ui_afisare_lista(secventa)

def ui_operatii_lista(list):
    ui_optiuni_operatii()
    cmd = input(">>>")
    if cmd == "suma":
        try:
            stanga, dreapta = ui_citire_indici()
        except Exception as ex:
            print(ex)
            return
        try:    
            suma = service.srv_calcul_numere_interval(list, stanga, dreapta, "suma")
        except Exception as ex:
            print(ex)
            return
        print("Suma = " + suma.to_string())
    if cmd == "produs":
        try:
            stanga, dreapta = ui_citire_indici()
        except Exception as ex:
            print(ex)
            return
        try:
            produs = service.srv_calcul_numere_interval(list, stanga, dreapta, "produs")
        except Exception as ex:
            print(ex)
            return
        print("Produsul = " + produs.to_string())  
    if cmd == "sort_desc_im":
        pass



def run():
    list = []
    while True:
        ui_optiuni_meniu_principal()
        cmd = input(">>>")
        if cmd == "adauga_numar":
            try:
                ui_adauga_numar(list) #1. Adauga numar in lista
            except Exception as ex:
                print(ex)
        if cmd == "afisare_lista":
            ui_afisare_lista(list)
        if cmd == "cautare_numere":     #3. Cautare numere
            ui_cautare_numere(list)
        if cmd == "operatii_lista":
            ui_operatii_lista(list)
        if cmd == "exit":
            return
        
           
