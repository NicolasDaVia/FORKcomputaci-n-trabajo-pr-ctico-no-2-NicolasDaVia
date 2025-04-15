def is_palindrome(texto):
  
    texto_limpio = ''.join(caracter for caracter in texto if caracter.isalnum()).lower()
    return texto_limpio == texto_limpio[::-1]

def main():
    entrada = input("Ingrese una palabra o frase: ")
    if is_palindrome(entrada):
        print("Es palíndrome.")
    else:
        print("No es palíndrome.")

if __name__ == '__main__':
    main()

