import pandas as pd
import random
import math

def generar_numeros(n, m):
    return [random.choice(range(m)) for _ in range(n)]

def calcular_media(lst):
    return sum(lst) / len(lst)

def calcular_varianza(lst):
    media_val = calcular_media(lst)
    return sum((num - media_val) ** 2 for num in lst) / (len(lst) - 1)

def calcular_mediana(lst):
    lst.sort()
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (lst[mid - 1] + lst[mid]) / 2
    return lst[mid]

def calcular_moda(lst):
    return pd.Series(lst).mode()[0]

def calcular_desviacion_estandar(lst):
    return math.sqrt(calcular_varianza(lst))

def suma_de_lista(lst):
    return sum(lst)

def simulacion_binomial(trials, n):
    return [sum(1 for _ in range(n) if random.random() < 0.5) for _ in range(trials)]

def distribucion_normal(n):
    return [random.gauss(0, 1) for _ in range(n)]

def tirar_moneda(trials):
    return ["Cara" if random.random() < 0.5 else "Sello" for _ in range(trials)]

def tirar_dado(trials):
    return [random.randint(1, 6) for _ in range(trials)]

def muestras_seno(n):
    return [math.sin(random.random() * math.pi) for _ in range(n)]

def principal():
    a = generar_numeros(100, 10)
    b = simulacion_binomial(1000, 100)
    c = distribucion_normal(500)
    d = tirar_dado(50)
    e = tirar_moneda(100)
    f = muestras_seno(200)

    datasets = {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': [1 if x == "Cara" else 0 for x in e],
        'f': f
    }

    for name, data in datasets.items():
        print(f"Media de {name}:", calcular_media(data))
        print(f"Varianza de {name}:", calcular_varianza(data))
        print(f"Mediana de {name}:", calcular_mediana(data))
        print(f"Moda de {name}:", calcular_moda(data))
        print(f"Desviación estándar de {name}:", calcular_desviacion_estandar(data))

if __name__ == "__main__":
    principal()
