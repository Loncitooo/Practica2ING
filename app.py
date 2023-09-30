
#Daniel Octavio Juarez Torres
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

# Esta poderosa funcion imprime el poderosisimo Oullea
def oullea():

    print('PruebaPalYisus')

    for i in range(0, 100):
        print("Oullea2")
    Master
    print("Oullea pal loncitoo")
    print("Oullea")

if __name__ == "__main__":
    text = input("Ingresa el texto a encriptar: ")
    shift = int(input("Ingresa el valor de desplazamiento: "))

    encrypted_text = encrypt(text, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print(f"Texto encriptado: {encrypted_text}")
    print(f"Texto desencriptado: {decrypted_text}")

