import math

class ComplexNumber:
    def __init__(self, real, imaginar):
        self.real = real
        self.imaginar = imaginar

    def get_real(self):
        return self.real
    
    def get_imaginar(self):
        return self.imaginar

    def set_real(self, real):
        self.real = real

    def set_imaginar(self, imaginar):
        self.imaginar = imaginar
    
    def to_string(self):
        return "[" + str(self.real) + "+" + str(self.imaginar) + "i]" 



def modul_numar_complex(number1):
        '''
            Calculeaza modulul numarului complex numar, unde
            numar.real este partea reala si numar.imaginar este partea
            imagiara:

            input: numarul complex numar
            output: modului numarului complex numar
        '''
        pReal = number1.get_real()
        pImaginar = number1.get_imaginar()
        patrat = pReal*pReal + pImaginar*pImaginar
        return math.sqrt(patrat)

def egale(number1, number2):
    '''
        Functia verifica daca numarul complex number1 este egal cu 
        numarul complex number2

        input: - number1, numar complex de forma a+bi unde a si b numere reale
               - number2,  numar complex de forma a+bi unde a si b numere reale
        output: - True, daca number1 si number2 sunt egale
                - False altfel
    '''
    if abs(number1.get_real() - number2.get_real()) > 0.0001: return False
    if abs(number1.get_imaginar() - number2.get_imaginar()) > 0.0001: return False
    return True


def suma(number1, number2):
    '''
        Functia calculeaza suma dintre numerele complexe 'number1' si 'number2'

        input: number1 - numar complex de forma a+bi, a, b numere reale
               number2 - numar complex de forma a+bi, a, b numere reale
        output: suma celor doua numere complexe 'number1' si 'number2'
    '''
    real = number1.get_real() + number2.get_real()
    imaginar = number1.get_imaginar() + number2.get_imaginar()
    return ComplexNumber(real, imaginar)
    
def produs(number1, number2):
    '''
        Functia calculeaza produsul dintre numerele complexe 'number1' si
        'number2'

        input: number1 - numar complex de forma a+bi, a, b numere reale
               number2 - numar complex de forma a+bi, a, b numere reale
        output: produsul celor doua numere complexe 'number1' si 'number2'
    '''
    n1Real = number1.get_real()
    n1Imaginar = number1.get_imaginar()
    n2Real = number2.get_real()
    n2Imaginar = number2.get_imaginar()
    
    real = n1Real * n2Real - n1Imaginar*n2Imaginar
    imaginar = n1Real * n2Imaginar + n2Real * n1Imaginar
    return ComplexNumber(real, imaginar)

def diferenta(number1, number2):
    '''
        Functia calculeaza diferenta dintre numerele complexe 'number1' si 
        'number2'

        input: number1 - numar complex de forma a+bi, a, b reale
               number2 - numar complex de forma a+bi, a, b reale
        output: diferenta dintre cele doua numere complexe 'number1' si 'number2'
    '''
    real = number1.get_real() - number2.get_real()
    imaginar = number1.get_imaginar() - number2.get_imaginar()
    return ComplexNumber(real, imaginar)
