def conertor(num):
    if type(num) != int or num <= 0:
        return "ingrese un numero entero (positivo)"
    if num > 3999:
        return "Solo se pueden ingresar números hasta 3999."

    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    resultado = ""
    i = 0
    while num > 0:
        if num >= valores[i]:
            resultado += simbolos[i]
            num -= valores[i]
        else:
            i += 1
    return resultado

def numero_entero():
    try:
        numero = int(input("Ingresa un número entero (hasta 3999): "))
        return numero
    except ValueError:
        print("No se puede convertir lo que ingresaste")

if __name__ == "__main__":
    numeroara = numero_entero()
    numeroro = conertor(numeroara)
    print(f"Resultado: {numeroro}")

        
