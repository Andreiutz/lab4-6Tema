from lab4Tema.utils import service


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
    print("")
    print("1) 'sterge_element'    - pentru a sterge un element de pe o pozitie data")
    print("2) 'sterge_interval'   - pentru a sterge elemente dintr-un interval dat")
    print("3) 'inlocuire_numar'   - pentru a modifica toate aparitiile unui numar dat cu altul" )
    print("")
    pass

def ui_optiuni_cautare(): #3
    #afisare in meniu
    print("")
    print("1) 'parte_imaginara  - pentru afisarea partii imaginare a tuturor numerelor din lista'")
    print("2) 'modul_m10'       - pentru afisarea numerelor cu modului < 10")
    print("3) 'modul_10         - pentru afisarea numerelor cu modului = 10")
    print("")

def ui_optiuni_operatii(): #4
    #afisare in meniu
    print("")
    print("1) 'suma'        - pentru calcularea sumei dintr-un interval")
    print("2) 'produs'      - pentru calcularea produsului dintr-un interval")
    print("3) 'sort_desc_im'- pentru afisarea listei ordonata desc. dupa partea imaginara")
    print("4) 'diferenta'   - pentru calcularea diferentei dintr-un interval dat")
    print("")

def ui_optiuni_filtrare(): #5
    #afisare in meniu
    print("")
    print("1) 'filtrare_p_reala'    - pentru eliminarea din lista a numerelor complexe cu parte reala numar prim")
    print("2) 'filtrare_modul'      - pentru eliminarea din lista a numerelor care au modulul <, =, > decat un nr. dat")
    print("")
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

def ui_adauga_numar(list, history):
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

    numar = service.srv_creare_numar(real, imaginar)
    ui_optiuni_adauga()
    pozitie = input(">>>")
    if pozitie == "pozitie":
        try:
            poz = int(input("dati pozitia: "))
        except ValueError:
            print("pozitie invalida!\n")
            return
        service.srv_adauga_numar(list, numar, poz, history)
    elif pozitie == "capat":
        service.srv_adauga_numar(list, numar, len(list), history)
    else: 
        print("valoare invalida\n")
        return

def ui_modifica_lista(list, history):
    ui_optiuni_modificare()
    cmd = input(">>>")
    if cmd == "sterge_element":
        try:
            pozitie = int(input("pozitia= "))
        except ValueError:
            print("pozitie invalida!\n")
            return
        try:
            service.srv_stergere_element(list, pozitie, history)
        except Exception as ex:
            print(ex)
            return 
    if cmd == "sterge_interval":
        try:
            stanga, dreapta = ui_citire_indici()
        except Exception as ex:
            print(ex)
            return  
        try:
            service.srv_stergere_interval(list, stanga, dreapta, history)
        except Exception as ex:
            print(ex)
            return
    if cmd == "inlocuire_numar":
        try:
            real = float(input("parte reala numar de schimbat = "))
        except ValueError:
            print("Parte reala invalida")
            return 

        try:
            imaginar = float(input("parte imaginara numar de schimbat = "))
        except ValueError:
            print("Parte imaginara invalida\n")
            return

        try:
            realNou = float(input("parte reala numar nou = "))
        except ValueError:
            print("Parte reala invalida")
            return 

        try:
            imaginarNou = float(input("parte imaginara numar nou = "))
        except ValueError:
            print("Parte imaginara invalida\n")
            return
        try:
            service.srv_modificare_element(list, service.srv_creare_numar(real, imaginar), service.srv_creare_numar(realNou, imaginarNou), history)
        except Exception as ex:
            print(ex)
            return

def ui_afisare_lista(lista):
    rez = "["
    elem = False
    for number in lista:
        rez += number.to_string() + ","
        elem = True
    if elem: rez += "\b"
    rez += "]"
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
        try:
            secventa = service.srv_cauta_numere(list, 0, len(list)-1, "modul < 10")
            ui_afisare_lista(secventa)
        except Exception as ex:
            print(ex)
            return
    if cmd == "modul_10":
        try:
            secventa = service.srv_cauta_numere(list, 0, len(list)-1, "modul = 10")
            ui_afisare_lista(secventa)
        except Exception as ex:
            print(ex)
            return

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
    elif cmd == "produs":
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
    elif cmd == "sort_desc_im":
        try:
            sorted_list = service.srv_sortare_desc_img(list)
        except Exception as ex:
            print(ex)
            return
        ui_afisare_lista(sorted_list)
    elif cmd == "diferenta":
        try:
            stanga, dreapta = ui_citire_indici()
        except Exception as ex:
            print(ex)
            return
        try:
            dif = service.srv_calcul_numere_interval(list, stanga, dreapta, "diferenta")
        except Exception as ex:
            print(ex)
            return
        print("Diferenta = " + dif.to_string()) 
        

def ui_filtrare_lista(list):
    ui_optiuni_filtrare()
    cmd = input(">>>")
    if cmd == 'filtrare_p_reala':
        try:
            rez = service.srv_filtrare_p_reala_prim(list)
        except Exception as ex:
            print(ex)
            return
        ui_afisare_lista(rez)
    if cmd == 'filtrare_modul':
        try:
            numar = float(input("numar = "))
        except ValueError:
            print("numar invalid!\n")
            return
        semn = input("semn = ")
        try:
            rez = service.srv_filtrare_modul(list, numar, semn)
        except Exception as ex:
            print(ex)
            return
        ui_afisare_lista(rez)

def ui_undo(list, history):
    try:
        service.srv_undo_list(list, history)
        ui_afisare_lista(list)
    except Exception as ex:
        print(ex)

def run():
    list = []
    history = []
    while True:
        ui_optiuni_meniu_principal()
        cmd = input(">>>")
        if cmd == "adauga_numar":
            try:
                ui_adauga_numar(list, history) #1. Adauga numar in lista
            except Exception as ex:
                print(ex)
        elif cmd == "modifica_lista":
            ui_modifica_lista(list, history)
        elif cmd == "cautare_numere":     #3. Cautare numere
            ui_cautare_numere(list)
        elif cmd == "operatii_lista":     #4. Operatii cu numere din lista
            ui_operatii_lista(list)
        elif cmd == "filtrare_lista":     #5. Filtrare lista
            ui_filtrare_lista(list)
        elif cmd == "afisare_lista":
            ui_afisare_lista(list)
        elif cmd == "undo":
            ui_undo(list, history)
        if cmd == "exit":
            return
        
           
