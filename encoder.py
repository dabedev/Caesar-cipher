def encoder(text, n):
    n = int(n)
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encoded = ""
    for char in text:
        if char.lower() in arr:
            if char == char.lower():
                encoded += arr[arr.index(char.lower())+n]
            else:
                encoded += arr[arr.index(char.lower())+n].upper()
        else:
            encoded += " "
    return encoded
decoded = input("Escribe el texto a ser encriptado: ")
n = input("Escribe la cantidad de espacios hacia la derecha en el alfabeto: ")
print(encoder(decoded,n))