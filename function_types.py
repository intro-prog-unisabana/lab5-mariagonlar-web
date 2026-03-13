def list_shift(lista, valor):
    for i in range(len(lista)):
        lista[i] += valor

def calc_avg (lista):
    if len(lista) == 0:
        return 0.0
    return sum(lista) / len(lista)

def print_normalized(lista):
    print(lista)

if __name__ == "__main__":
    datos = [2.0, 4.0, 6.0, 8.0]

    prom = calc_avg(datos)      
    list_shift(datos, -prom)    
    print_normalized(datos)








