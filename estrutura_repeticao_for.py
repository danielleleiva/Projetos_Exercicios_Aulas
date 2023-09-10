texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#Exemplo utiizando um iterável
for letra in texto:
    #trasnforma a váriavel em upper case e verifica se o objeto iterável esta dentro da varivel "VOGAIS"
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")

#Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=", ") #"end serve para colocar os objetos da lista um ao lado do outro com um espaço/caractere/letra"


