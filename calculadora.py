def sumar(a,b):
    return(a+b)

def restar(a,b):
    return(a-b)


def multiplicar(a,b):
    return (a*b)

def dividir(a,b):
    if b==0:
        return "No se puede dividir entre cero"
    return a/b

numero1=10
numero2=5

print("suma: ",sumar(numero1,numero2))
print("Resta: ",restar(numero1,numero2))
print("Multiplicacion: ",multiplicar(numero1,numero2))
print("Dividir",dividir(numero1,numero2)) #control s