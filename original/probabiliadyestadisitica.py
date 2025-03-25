import pandas as pd
import random
import math

def generar_numeros(n, m):
    numeros = []
    for i in range(n):
        numeros.append(random.choice(range(m)))
    return numeros

def calcular_media(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

def calcular_varianza(lst):
    media_val = calcular_media(lst)
    varianza = 0
    for num in lst:
        varianza += (num - media_val) ** 2
    return varianza / (len(lst) - 1)

def calcular_mediana(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

def calcular_moda(lst):
    contador = {}
    for num in lst:
        if num in contador:
            contador[num] += 1
        else:
            contador[num] = 1
    moda = max(contador, key=contador.get)
    return moda

def calcular_desviacion_estandar(lst):
    var = calcular_varianza(lst)
    return math.sqrt(var)

def suma_de_lista(lst):
    total = 0
    for num in lst:
        total += num
    return total

def simulacion_binomial(trials, n):
    resultado = []
    for i in range(trials):
        cuenta = 0
        for j in range(n):
            if random.random() < 0.5:
                cuenta += 1
        resultado.append(cuenta)
    return resultado

def distribucion_normal(n):
    resultado = []
    for i in range(n):
        resultado.append(random.gauss(0, 1))
    return resultado

def tirar_moneda(trials):
    resultado = []
    for i in range(trials):
        if random.random() < 0.5:
            resultado.append("Cara")
        else:
            resultado.append("Sello")
    return resultado

def tirar_dado(trials):
    resultado = []
    for i in range(trials):
        resultado.append(random.randint(1, 6))
    return resultado

def muestras_seno(n):
    resultado = []
    for i in range(n):
        resultado.append(math.sin(random.random() * math.pi))
    return resultado

def principal():
    a = generar_numeros(100, 10)
    b = simulacion_binomial(1000, 100)
    c = distribucion_normal(500)
    d = tirar_dado(50)
    e = tirar_moneda(100)
    f = muestras_seno(200)

    print("Media de a:", calcular_media(a))
    print("Varianza de a:", calcular_varianza(a))
    print("Mediana de a:", calcular_mediana(a))
    print("Moda de a:", calcular_moda(a))
    print("Desviación estándar de a:", calcular_desviacion_estandar(a))
    print("Suma de a:", suma_de_lista(a))
    
    print("Media de b:", calcular_media(b))
    print("Varianza de b:", calcular_varianza(b))
    print("Mediana de b:", calcular_mediana(b))
    print("Moda de b:", calcular_moda(b))
    print("Desviación estándar de b:", calcular_desviacion_estandar(b))
    
    print("Media de c:", calcular_media(c))
    print("Varianza de c:", calcular_varianza(c))
    print("Mediana de c:", calcular_mediana(c))
    print("Moda de c:", calcular_moda(c))
    print("Desviación estándar de c:", calcular_desviacion_estandar(c))
    
    print("Media de d:", calcular_media(d))
    print("Varianza de d:", calcular_varianza(d))
    print("Mediana de d:", calcular_mediana(d))
    print("Moda de d:", calcular_moda(d))
    print("Desviación estándar de d:", calcular_desviacion_estandar(d))
    
    print("Media de e:", calcular_media([1 if x == "Cara" else 0 for x in e]))
    print("Varianza de e:", calcular_varianza([1 if x == "Cara" else 0 for x in e]))
    print("Moda de e:", calcular_moda([1 if x == "Cara" else 0 for x in e]))
    
    print("Media de f:", calcular_media(f))
    print("Varianza de f:", calcular_varianza(f))
    print("Mediana de f:", calcular_mediana(f))
    print("Moda de f:", calcular_moda(f))
    print("Desviación estándar de f:", calcular_desviacion_estandar(f))

if __name__ == "__main__":
    principal()
