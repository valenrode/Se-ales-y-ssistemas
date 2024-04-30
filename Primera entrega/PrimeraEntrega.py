##SE ENTREGA EL 7 DE MAYO
import numpy as np
from matplotlib import pyplot as plt


def get_data():
    f1 = int(input('Ingrese frecuencia inferior:'))
    f2 = int(input('Ingrese frecuencia superior:'))
    T = int(input('Ingrese T: '))
    print(f1,f2,T)
    return f1,f2,T

def signal_gen(f1,f2,T):
    w1=2*np.pi*f1
    w2=2*np.pi*f2   
    R = np.log(w2/w1)
    K = float((T*w1)/R) 
    L = T/R
    fs=10000
    t = np.linspace(0,T,T*fs)
    f = np.sin(K*(np.exp(t/L)-1))
    return t,f
def get_plot(t,f):
    plt.plot(t,f)
    plt.show()
    return
def test_1():
    try:
        get_data()
    except:
        print("Error en el test 1")
    return("Prueba exitosa")


if __name__ == '__main__':
    # este es el main
    print('ejecutando 1° test: ...')
    test_1()



# Filtro Inverso
"""""
def filtro_inv_gen(signal_gen()):
    wt = (K/L)*np.exp(t/L)
    mt = w1/(2*np.pi*wt)
    R1 = np.log(w1/w2)
    L1 = T/R1
    f1 = np.sin(K*(np.exp(t/L1)-1))
    kt = mt*f1

plt.plot(t,f)
plt.show()
plt.plot(t,kt)
plt.show()
conv = np.convolve(f,kt)
plt.plot(t,conv)
plt.show

"""""



