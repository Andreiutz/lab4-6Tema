def validare_interval(list, stanga, dreapta):
    '''
        Functia valideaza indicii 'stanga' si 'dreapta' pentru o lista 'list'

        input: list - lista de numere complexe
               stanga - numar intreg pozitiv, reprezinta capatul din stanga al intervalului
               dreapta - numar intreg pozitiv, reprezinta capatul din dreapta al intervalului
        output: -
                raises Exception: "capat stanga invalid!\n" - daca 'stanga' < 0 sau 'stanga' > 'dreapta'
                                  "capat dreapta invalid!\n" - daca 'dreapta' < 'stanga' sau 'dreapta' > len(list)
    '''
    ex = ""
    if stanga < 0 or stanga > dreapta:
        ex += "capat stanga invalid!\n"
    if dreapta > len(list)-1 or dreapta < stanga:
        ex += "capat dreapta invalid!\n"
    
    if len(ex) > 0:
        raise Exception(ex)
