while True:
    numero = int(input("Informe um número: "))
    
    if numero == 10:
        break  #sair do codigo , "continue pula o valor dentro da sequencia"

    if numero % 2 == 0:
       continue

    print(numero, end=", ")

