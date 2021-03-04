def decoder(text, n):
    n = int(n)
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decoded = ""
    for char in text:
        if char.lower() in arr:
            if char == char.lower():
                decoded += arr[arr.index(char.lower())-n]
            else:
                decoded += arr[arr.index(char.lower())-n].upper()
        else:
            decoded += " "
    return decoded
encoded = input("Escribe el texto a ser desencriptado: ")
n = input("Escribe la cantidad de espacios hacia la derecha en el alfabeto: ")
print(decoder(encoded,n))